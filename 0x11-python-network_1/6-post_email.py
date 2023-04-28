#!/usr/bin/python3
"""
Python script that takes in a URL and an email address, sends a POST request
to the passed URL with email as a parameter & displays body of the response
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    myreq = {'email': sys.argv[2]}
    response = requests.post(url, data=myreq)
    print(response.text)
