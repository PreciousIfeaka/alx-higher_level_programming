#!/usr/bin/python3
"""
This module takes in a url, sends a request to the url and displays the
value of the X-Request-Id variable found in the header of the response.
"""

import urllib.request
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        header = dict(response.headers)
        header_val = header.get('X-Request-Id')
        print(header_val)
