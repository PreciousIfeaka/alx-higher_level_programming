#!/bin/bash
# Responds to a message
curl -s -X PUT -L -H "Origin: HolbertonSchool" -d "user_id=98" "0.0.0.0:5000/catch_me"
