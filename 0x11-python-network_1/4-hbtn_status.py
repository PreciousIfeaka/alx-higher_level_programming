#!/usr/bin/python3

"""
This script fetches a url using the requests package
"""

if __name__ == '__main__':
    import requests

    url = 'https://alx-intranet.hbtn.io/status'
    try:
        response = requests.get(url)
        print('Body response:')
        print('\t- type: {}'.format(type(response.text)))
        print('\t- content: {}'.format(response.text))
    except Exception as e:
        pass
