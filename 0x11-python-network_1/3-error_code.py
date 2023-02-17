#!/usr/bin/python3
"""
This script  takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8)
"""


if __name__ == "__main__":
    import sys
    import urllib.request
    from urllib.error import HTTPError

    url = sys.argv[1]
    request_0 = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request_0) as response:
            content = response.read()
            print("{}".format(content.decode('utf-8')))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
