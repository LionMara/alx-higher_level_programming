#!/usr/bin/python3
""" 1-hbtn_header.py """

import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    """ regulates opening of files """
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        print(dict(response.headers).get("X-Request-Id"))
