#!/bin/bash
# This script sends a JSON POST request to a url and displays the response
curl -sX POST -H "Content-Type: application/json" -d "@$2" "$1"
