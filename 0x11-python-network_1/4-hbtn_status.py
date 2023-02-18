#!/usr/bin/python3
"""
This script fetches a given url using the requests package
"""


if __name__ == "__main__":
    import requests

    r = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
