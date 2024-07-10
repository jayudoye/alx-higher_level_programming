#!/usr/bin/python3
"""This script calls the GitHub API and lists 10 commits
(from the most recent to oldest) of the
repository “rails” by the user “rails”"""
import requests
import sys

if __name__ == "__main__":
    try:
        url = "https://api.github.com/repos/{}/{}/commits".\
              format(sys.argv[2], sys.argv[1])
        response = requests.get(url)
        response = response.json()
        for repo in response[:10]:
            print("{}: ".format(repo.get('sha')), end="")
            name = repo.get('commit').get('author').get('name')
            print("{}".format(name))
    except ValueError:
        print("Not a valid JSON")
