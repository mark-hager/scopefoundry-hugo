# Generates markdown doc pages from cached_repos.json
import json
from pathlib import Path
import shutil

ROOT = Path("content/en/docs/300_reference/hw-components")
HW_BASELINK = Path("/docs/300_reference/hw-components")

def laod_cached_repos():
    with open("cached_repos.json", "r", encoding="utf8") as file:
        return json.load(file)  # Load JSON as a dictionary

def mk_unique_title(repo):
    return f"{repo['name']} ({repo["owner"]})"


def mk_unique_folder_name(repo):
    return f"{repo['name']}-{repo["owner"]}".replace(" ", "-")


def path_to(repo):
    return str(ROOT / mk_unique_folder_name(repo))


def link_to(repo):
    folder = mk_unique_folder_name(repo)
    return str(HW_BASELINK / folder).lower()


def sort_key(repo):
    return f'{repo["name"].lower()}:{repo["updated_at"]}'


def import_with_gh_cmd(name, html_url, owner, default_branch="master"):
    path = f"ScopeFoundryHW/{name.strip("HW_")}"
    remote_name = f"upstream_{owner}"
    return f"mkdir {path} && cd {path} && git init --initial-branch={default_branch} && git remote add {remote_name} {html_url} && git pull {remote_name} {default_branch} && cd ../.."


def import_with_git_subtree(name, html_url, default_branch="master"):
    return f"git subtree add --prefix ScopeFoundryHW/{name.strip("HW_")}/ {html_url} {default_branch} && git checkout"


def fork_from(repo, id_lu):
    if repo["parent_id"] is None:
        return ""
    parent = id_lu[find_root_id(repo, id_lu)]
    return f"- Forked from [{mk_unique_title(parent)}]({link_to(parent)})"


def markdown_content(
    title,
    weight,
    name: str,
    html_url: str,
    description=None,
    updated_at=None,
    readme=None,
    owner="ScopeFoundry",
    default_branch="master",
    forked_from: str = "",
    **kwargs,
):
    # dedented bc otherwise python writes indentation:
    # https://stackoverflow.com/questions/53142613/error-in-converting-from-markdown-to-editor-in-flask
    return f"""
---
title: {title}
description: {description or "No description available."}
weight: {weight}
---
- [GitHub Repository]({html_url})
- Last Updated: {updated_at}
{forked_from}

#### To add to your app:

`cd to/your_project_folder` and use the following cmd (requires [git](/docs/100_development/20_git/))

```bash
{import_with_gh_cmd(name, html_url, owner, default_branch)}
```

## Readme
{readme}
"""


def find_root_id(repo, id_lu):
    if repo["parent_id"] is None:
        return repo["id"]
    else:
        return find_root_id(id_lu[repo["parent_id"]], id_lu)


def generate_markdown_files(repos_list):
    # depth = 2 hierachry:
    # 1. roots are repos without parents
    # 2. children repos have ancestors, will get linked to the root parent
    roots = [r for r in repos_list if r["parent_id"] is None]
    children = [r for r in repos_list if r["parent_id"] is not None]

    id_lu = {r["id"]: r for r in repos_list}
    path_lu = {r["id"]: path_to(r) for r in roots}

    weight = 1
    for repo in sorted(roots, key=sort_key):
        title = mk_unique_title(repo)
        path = Path(path_lu[repo["id"]])
        path.mkdir(exist_ok=True)

        filename = path / "_index.md"
        with open(filename, "w", encoding="utf8") as md_file:
            md_file.write(markdown_content(title, weight, **repo))

        print(f"Generated {filename} {weight=}")
        weight += 1

    for repo in sorted(children, key=sort_key):
        title = mk_unique_title(repo)
        path = Path(path_lu[find_root_id(repo, id_lu)])

        filename = path / f"{mk_unique_folder_name(repo)}.md"
        with open(filename, "w", encoding="utf8") as md_file:
            md_file.write(
                markdown_content(
                    title, weight, forked_from=fork_from(repo, id_lu), **repo
                )
            )

        print(f"Generated {filename} {weight=}")
        weight += 1


# def delete_folder_content(path: Path):
#     if path.exists() and path.is_dir():
#         for item in path.iterdir():
#             if item.is_dir():
#                 delete_folder_content(item)
#                 item.rmdir()
#                 print(f"Deleted folder: {item}")
#             else:
#                 item.unlink()
#                 print(f"Deleted file: {item}")
#         print(f"Emptied folder: {path}")
#     else:
#         print(f"Folder does not exist: {path}")


def delete_folder_content(path: Path):
    for item in path.iterdir():
        if item.is_dir():
            print(item)
            # shutil.rmtree(path)


def gen_hw_doc():
    repos = laod_cached_repos()
    # Access the list of repositories
    # **TODO** check against when this was last done,
    # no point if recent.
    repos_list = repos.get("repositories", [])
    # Generate Markdown files
    if repos_list:
        print(f"Generating {len(repos_list)} markdown files in {ROOT}")
        delete_folder_content(ROOT)
        generate_markdown_files(repos_list)

if __name__ ==  "__main__":    
    gen_hw_doc()
