#!/usr/bin/python3
"""
This module fetches a url given a set of requirements.
"""

import urllib.request

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        content = response.read()
        try:
            print('Body response:')
            print('\t- type: {}'.format(type(content)))
            print('\t- content: {}'.format(content))
            print('\t- utf8 content: {}'.format(content.decode('utf-8')))
        except Exception as e:
            pass
