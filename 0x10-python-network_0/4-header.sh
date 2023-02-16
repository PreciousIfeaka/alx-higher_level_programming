#!/bin/bash
# Takes in a URL as an argument and send a GET request to a url
curl -sH "X-School-User-Id: 98" "${1}"
