#!/usr/bin/python3
"""
This script takes in a letter and sends a POST request to a url
with the letter as a parameter
"""

if __name__ == '__main__':
    from sys import argv
    import requests

    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) == 1:
        data = {'q': ""}
    else:
        data = {'q': argv[1]}

    try:
        resp = requests.post(url, data=data)
        jsoned = 'application/json'
        if resp.headers.get('content-type') == jsoned and len(resp.text) == 0:
            print("No result")
        elif resp.headers.get('content-type') == jsoned:
            name = resp.text.get('name')
            identity = resp.text.get('id')
            print('[{}] {}'.format(identity, name))
        else:
            print("Not a valid JSON")
    except Exception as e:
        pass
