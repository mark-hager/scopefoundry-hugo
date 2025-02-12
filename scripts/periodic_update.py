from fetch_sf_hw import fetch_and_cache_repos
from gen_hw_doc import gen_hw_doc


def main():
    fetch_and_cache_repos()
    gen_hw_doc()


if __name__ == "__main__":
    main()
