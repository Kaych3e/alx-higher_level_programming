#!/bin/bash
#send a POST request with contents of a file,passed with filename as 2nd arg
curl -s "$1" -H "Content-Type: application/json" -d "$(cat "$2")"
