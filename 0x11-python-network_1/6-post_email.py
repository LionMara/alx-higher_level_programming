#!/usr/bin/python3
"""6-post_email.py"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    req = requests.post(url, data=value)
    print(r.text)
