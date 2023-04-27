#!/bin/bash
#script that takes in a URL & displays the size of the body of the response
curl -sI "$1" | grep -i Content-Length | cut -d " " -f2

