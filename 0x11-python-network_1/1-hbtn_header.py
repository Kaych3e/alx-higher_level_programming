#!/usr/bin/python3
# sends request to the URL displays the value of X-Request-Id variable

import urllib.request
import sys


if __name__ == "__main__":

    with urllib.request.urlopen("https://alx-intranet.hbtn.io") as response:
        headers = response.info()
        print(headers['X-Request-Id'])
