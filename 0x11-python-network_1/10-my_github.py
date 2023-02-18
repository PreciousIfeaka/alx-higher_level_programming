#!/usr/bin/python3
"""
This script takes a github credentials (username and password)
and uses the GitHub API to display the id
"""


if __name__ == "__main__":
    import sys
    import requests
    from requests.auth import HTTPBasicAuth

    url = "https://api.github.com/user"
    basic = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    res = requests.get(url, auth=basic)
    print(res.json().get('id'))
