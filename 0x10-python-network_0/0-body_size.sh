#!/usr/bin/env bash
# This script takes in a url, sends a request to it and displays the size of the body of the response.
curl -s "$1" | wc -c
