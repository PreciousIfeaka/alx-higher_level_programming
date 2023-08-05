#!/usr/bin/python3
"""
This script takes in a letter and sends a POST request to a url
with the letter as a parameter
"""

if __name__ == '__main__':
    import sys
    import requests

    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) == 2:
        payload = {'q': sys.argv[1]}
    else:
        payload = {'q': ""}

    response = requests.post(url, data=payload)
    try:
        r = response.json()
        if r = {}:
            print("No result")
        else:
            name = r.get('name')
            identity = r.get('id')
            print('[{}] {}'.format(identity, name))
    except ValueError:
        print("Not a valid JSON")
