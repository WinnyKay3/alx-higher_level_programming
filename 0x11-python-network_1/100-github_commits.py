#!/usr/bin/python3
''' using github api to list commits.'''

import sys
import requests


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        owner_name, repo_name)

    params = {'per_page': 10}

    response = requests.get(url, params=params)

    commits = response.json()
    for commit in commits:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")
