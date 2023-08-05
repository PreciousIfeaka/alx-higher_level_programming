#!/usr/bin/python3
"""The module lists the last ten commits of the repository rails
by a user rails
"""


if __name__ == "__main__":
    from sys import argv
    import requests

    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[1], argv[2])
    response = requests.get(url)
    json = response.json()
    try:
        for i in range(10):
            commit = json[i]
            sha = commit.get('sha')
            author = commit.get('commit').get('author').get('name')
            print("{}: {}".format(sha, author))
    except Exception as e:
        pass
