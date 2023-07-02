#!/bin/bash
# This script takes in a url as an argument, sends a GET request to the url and displays the body of thr response.
curl -sX GET -H "X-School-User-Id : 98" "$1" 
