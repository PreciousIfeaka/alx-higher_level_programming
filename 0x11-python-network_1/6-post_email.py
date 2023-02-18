#!/usr/bin/python3
"""
This script takes a URL and an email address, sends a POST request
to the passed URL with the email as a parameter, and
finally diaplays the body of the response.
"""


if __name__ == "__main__":
    import sys
    import requests

    url = sys.argv[1]
    data = {'email': sys.argv[2]}

    response = requests.post(url, data)
    print(response.text)
