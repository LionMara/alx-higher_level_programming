#!/usr/bin/python3
"""3-error_code.py"""

import sys
import urllib
import urllib.error
import urllib.request
if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
