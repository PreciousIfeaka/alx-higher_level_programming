#!/usr/bin/python3
"""
This script takes in a letter and sends a POST request to a url
with the letter as a parameter
"""

if __name__ == '__main__':
    from sys import argv
    import requests

    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) == 2:
        payload = {'q': argv[1]}
    else:
        payload = {'q': ""}

    try:
        response = requests.post(url, data=payload)
        r = response.json()
        jsoned = 'application/json'
        if r = {}:
            print("No result")
        elif response.headers.get('content-type') == jsoned:
            name = r.get('name')
            identity = r.get('id')
            print('[{}] {}'.format(identity, name))
        else:
            print("Not a valid JSON")
    except Exception as e:
        pass
