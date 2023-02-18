#!/usr/bin/python3
"""
This script sends a request to a url and displays the value of the variable
X-Request-Id in the response header
"""


if __name__ == "__main__":
    import sys
    import requests

    response = requests.get(sys.argv[1])
    x_request_id = response.headers.get('X-Request-Id')
    print(x_request_id)
