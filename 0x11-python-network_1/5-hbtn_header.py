#!/usr/bin/python3
"""5-hbtn_header.py"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    req = requests.get(url)
    print(req.headers.get("X-Request-Id"))
