#!/usr/bin/python3
"""
This script takes in a letter and sends a POST request
to a url with a letter as a parameter.
"""


if __name__ == "__main__":
    import sys
    import requests

    url = 'http://0.0.0.0:5000/search_user'

    value = sys.argv[1] if len(sys.argv) == 2 else ""

    data = {'q': value}

    response = requests.post(url, data)
    try:
        res = response.json()
        if res:
            print("[{}] {}".format(res['id'], res['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
