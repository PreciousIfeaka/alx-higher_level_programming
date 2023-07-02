#!/bin/bash
# This script takes a url and displayes all http methods the server will accept
curl -s --head "$1" | grep "Allow:" | cut -d " " -f 2-
