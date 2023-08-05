#!/usr/bin/python3
"""
This script takes a GitHub credentials (username and password) and uses
github api to display the account id
"""

if __name__ == "__main__":
    from sys import argv
    import requests
    from requests.auth import HTTPBasicAuth

    url = 'https://api.github.com/users/{}'.format(argv[1])
    response = requests.get(url, auth=HTTPBasicAuth(argv[1], argv[2]))
    json = response.json()
    print(json.get('id'))
