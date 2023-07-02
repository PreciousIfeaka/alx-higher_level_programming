#!/bin/bash
# This script sends a request to a url passed as argument and displays onlt the status code of the response.
curl -sL -w "%{http_code}" "$1" -o /dev/null
