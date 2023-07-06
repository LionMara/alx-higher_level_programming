#!/usr/bin/python3
"""
- script that takes in a URL and an email,
- sends a POST request to the passed URL with the email as a parameter
- displays the body of the response (decoded in utf-8)
"""

from urllib import request, parse
import sys

url = sys.argv[1]
email = sys.argv[2]

if __name__ == "__main":
    params = urllib.parse.urlencode({'email':email}).encode('utf-8')
    with urllib.request.urlopen(url, data=params) as response:
        body = response.read().decode('utf-8')
        print(body)
