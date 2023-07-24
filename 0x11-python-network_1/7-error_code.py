#!/usr/bin/python3
"""This script takes in a url, sends a request to it and displays the body
of the response. Returns the status code if it is greater than 400
"""

if __name__ == '__main__':
    from sys import argv
    import requests

    try:
        response = requests.get(argv[1])
        if response.status_code < 400:
            print(response.text)
        else:
            print('Error code: {}'.format(response.text))
    except Exception as e:
        pass
