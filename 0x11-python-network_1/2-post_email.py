#!/usr/bin/python3

"""
This module takes in a url and an email, sends a POST request to the url
with the email as a parameter, and displays the body of the response in utf-8
"""

import sys
import urllib.request

if __name__ == '__main__':
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    email = urllib.parse.urlencode(value).encode('ascii')

    with urllib.request.urlopen(url, email) as response:
        mail_value = reponse.read()
        mail_value = mail_value.decode('utf-8')
        print('Your email is: {}'.format(mail_value))
