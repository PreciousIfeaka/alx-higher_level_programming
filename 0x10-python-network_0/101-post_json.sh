#!/bin/bash
# This script displays the body of the response of the url argument
curl -s -X POST -H "Content-Type: application/json" -d "$2" "$1"
