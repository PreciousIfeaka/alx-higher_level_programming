#!/usr/bin/python3

"""This script takes in a url and an email address, sends a POST request
to the passed url with the email as a parameter and finally displays the
body of the response
"""

if __name__ == '__main__':
    import sys
    import requests

    url = sys.argv[1]
    data = {'email': sys.argv[2]}

    try:
        response = requests.post(url, data=data)
        print(response.text)
    except Exception as e:
        pass
