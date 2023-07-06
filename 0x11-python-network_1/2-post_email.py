#!/usr/bin/python3
""" 2-post_email.py"""

from urllib import request, parse
import sys

url = sys.argv[1]
email = sys.argv[2]

if __name__ == "__main__":
    params = urllib.parse.urlencode({'email': email}).encode('utf-8')
    with urllib.request.urlopen(url, data=params) as response:
        body = response.read().decode('utf-8')
        print(body)
