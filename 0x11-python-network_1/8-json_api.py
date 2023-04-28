#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
The letter must be sent in the variable q,If no argument is given, set q=""
"""
import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) == 1:
        myreq = {'q': ""}
    else:
        myreq = {'q': sys.argv[1]}

    response = requests.post("http://0.0.0.0:5000/search_user", data=myreq)

    try:
        response = response.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get('id'), response.get('name')))
    except ValueError:
        print("Not a valid JSON")
