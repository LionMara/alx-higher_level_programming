#!/usr/bin/python3
"""script takes in URL displays value of the X-Request-Id variable"""

import urllib.request
import sys

url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    headers = response.headers

print(headers['X-Request-Id'])
