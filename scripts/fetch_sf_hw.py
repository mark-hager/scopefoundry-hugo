#  Queries GitHub for all ScopeFoundry hardware component repos and updates the cache file.
import datetime
import json
import os
from dataclasses import dataclass
from pathlib import Path

import requests


HW_PREFIX = "HW_"  # all hardware component repos appear to/should start with HW_...
CACHE_FILE = "cached_repos.json"

# check both "official" SF repo and collaborator forks for hw submodules
# GitHub API differentiates users and orgs
@dataclass
class Owners:
    fork_users: list
    fork_orgs: list
    main_org: str = "ScopeFoundry"

    def __post_init__(self):
        self.users = self.fork_users
        self.orgs = [self.main_org] + self.fork_orgs

    def __iter__(self):
        return ((x, self.is_org(x)) for x in (self.users + self.orgs))

    def is_org(self, owner):
        return owner in self.orgs


# when number collaboraters exceed 59 we need a TOKEN
# without TOKEN we get 60 requests per hour
# we need one request per user to get all repos
# and one per repository that needs to be updated

try:
    GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
except KeyError:
    GITHUB_TOKEN = None  # "your_github_token_here"
    # or raise an error if it's not available so that the workflow fails


QUERY_COUNTER = 0


def query_github(api_url):
    headers = {"Accept": "application/vnd.github.raw+json"}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"token {GITHUB_TOKEN}"
    global QUERY_COUNTER
    QUERY_COUNTER += 1
    print(f"#{QUERY_COUNTER}: querying GitHub API: {api_url}")
    return requests.get(api_url, headers=headers, timeout=100)


def fetch_readme(repo_url: str):
    """
    Fetches the readme file from a given repository using the GitHub API
    https://docs.github.com/en/rest/repos/contents?apiVersion=2022-11-28#get-a-repository-readme
    """
    api_url = (
        repo_url.replace("https://github.com", "https://api.github.com/repos")
        + "/contents/README.md"
    )
    response = query_github(api_url)
    if response.status_code == 200:
        return response.text
    return "README could not be retrieved."


def fetch_repo_info(repo_url: str):
    """
    Fetches all information from a given repository
    """
    api_url = repo_url.replace("https://github.com", "https://api.github.com/repos")
    response = query_github(api_url)
    if response.status_code == 200:
        return response.json()
    return {}


def fetch_parent_id(repo):
    if repo["fork"]:
        repo_url = repo["url"]
        return fetch_repo_info(repo_url)["parent"]["id"]
    return None


def fetch_repos(owner, is_org, page_per=100):
    """
    Fetches repositories for a given GitHub user or organization.
    """
    # TODO: check if per_page of 100 is indeed the maximum
    if is_org:
        api_url = f"https://api.github.com/orgs/{owner}/repos?per_page={page_per}"
    else:
        api_url = f"https://api.github.com/users/{owner}/repos?per_page={page_per}"

    response = query_github(api_url)
    if response.status_code != 200:
        print(
            f"Failed to fetch repositories for {owner}: {response.status_code} - {response.text}"
        )
        return []

    # pagination
    repos = response.json()
    while response.links and "next" in response.links:
        response = query_github(response.links["next"]["url"])
        repos += response.json()

    return repos


def get_owners(org="ScopeFoundry", repo="ScopeFoundry") -> Owners:
    api_url = f"https://api.github.com/repos/{org}/{repo}/forks?per_page=100"
    # TODO: add pagination
    response = query_github(api_url)

    fork_users = [
        r["owner"]["login"] for r in response.json() if r["owner"]["type"] == "User"
    ]
    fork_orgs = [
        r["owner"]["login"] for r in response.json() if r["owner"]["type"] != "User"
    ]
    return Owners(fork_users, fork_orgs, org)


def read_cached_repos():
    if not Path(CACHE_FILE).exists():
        return []
    with open(CACHE_FILE, "r", encoding="utf8") as file:
        return json.load(file)["repositories"]


def replace_cached_data(cache_data):
    with open(CACHE_FILE, "w", encoding="utf8") as f:
        json.dump(cache_data, f, indent=4)


def timestamped_id(repo):
    timestamp = repo["updated_at"]
    return f'{repo["html_url"]}:{timestamp}'


def fetch_and_cache_repos():
    """
    Fetches repositories from both ScopeFoundry and collaborator forks, then caches the results.
    """
    # can reduce the number of requests if only updating the new repos
    existing_ids = {timestamped_id(repo): repo for repo in read_cached_repos()}

    owners = get_owners()

    # fetch hw repos
    hw_repos = []
    for owner, is_org in owners:
        repos = fetch_repos(owner, is_org)
        for repo in repos:
            if not repo["name"].startswith(HW_PREFIX):
                continue

            if timestamped_id(repo) in existing_ids:
                to_cache = existing_ids[timestamped_id(repo)]
                # to_cache["default_branch"] = repo["default_branch"]
            else:
                to_cache = {
                    "name": repo["name"],
                    "id": repo["id"],
                    "owner": owner,
                    "html_url": repo["html_url"],
                    "description": repo["description"],
                    "updated_at": repo["updated_at"],
                    "readme": fetch_readme(repo["html_url"]),
                    "default_branch": repo["default_branch"],
                    "parent_id": fetch_parent_id(repo),
                }
            hw_repos.append(to_cache)

    if not hw_repos:
        msg = "Failed to update HW Component Cache: No hardware component repositories found"
        print(msg)
        return

    cache_data = {
        "fetched_at": datetime.datetime.now(datetime.UTC).isoformat(),
        "repositories": hw_repos,
    }
    replace_cached_data(cache_data)

    msg = f"HW Component Cache updated successfully at {cache_data['fetched_at']}"
    print(msg)


if __name__ == "__main__":
    fetch_and_cache_repos()
