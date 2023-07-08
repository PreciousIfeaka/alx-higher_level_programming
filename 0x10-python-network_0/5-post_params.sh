#!/bin/bash
# This script takes in a url, sends a POST request to the passed url
#... and displays the body of the response
curl -sX POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
