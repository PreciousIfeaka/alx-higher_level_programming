#!/usr/bin/python3
"""
This script takes in a url, sends a request to the url and displays the value
of the X-request-Id variable found in the header of the response
"""


if __name__ == "__main__":
    import sys
    import urllib.request

    with urllib.request.urlopen(sys.argv[1]) as response:
        print(dict(response.headers).get('X-Request-Id'))
