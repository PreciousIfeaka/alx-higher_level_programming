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
        q = sys.argv[1]
        payload = {'q': q}
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
    except Exception as e:
        print("Not a valid JSON")
