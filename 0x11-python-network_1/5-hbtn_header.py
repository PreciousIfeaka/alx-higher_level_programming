#!/usr/bin/python3

"""This script takes in a url, sends a request to it
and display the value of the variable X-Request-Id in the response header
"""

if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]

    try:
        response = requests.get(url)
        head = response.headers.get('X-Request-Id')
        print(head)
    except Exception as e:
        pass
