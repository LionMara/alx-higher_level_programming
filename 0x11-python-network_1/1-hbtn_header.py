#!/usr/bin/python3
"""
     - script that takes in a URL
     - sends a request to the URL
     - displays the value of the X-Request-Id variable
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        headers = response.headers

print(headers['X-Request-Id'])
