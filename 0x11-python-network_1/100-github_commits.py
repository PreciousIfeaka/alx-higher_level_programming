#!/usr/bin/python3
"""
This script takes the repository and the owner of a github account as
argument and displays the last ten commits of the repository
"""


if __name__ == "__main__":
    from sys import argv
    import requests

    url = f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits"

    res = requests.get(url)
    commits = res.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get('sha'),
                commits[i].get('commit').get('author').get('name')))
    except IndexError:
        pass
