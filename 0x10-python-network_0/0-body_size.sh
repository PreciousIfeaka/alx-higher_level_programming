#!/bin/bash
#This displays the size of the body of a URL response by its bytes
curl -s "$1" | wc -c
