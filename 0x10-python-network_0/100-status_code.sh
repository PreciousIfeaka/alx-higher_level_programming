#!/bin/bash
# This script displays only the status code of the url response
curl -s -o /dev/null -w "%{http_code}" "$1"
