#!/bin/bash
#sends a request to a URL, displays only the status code of the response
curl -sI "$1" -o /dev/null -w "%{http_code}"
