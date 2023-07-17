#!/usr/bin/python3
"""
10-my_github.py
takes your GitHub credential
nd uses the GitHub API to display your id
"""

import requests
import sys

username = sys.argv[1]
access_token = sys.argv[2]

headers = {
    "Authorization": f"Basic {username}:{access_tojen}"
}

response = requests.get("https://api.github.com/user", headers=headers)
if response.status_code == 200:
    data = response.json()
    user_id = data.get("id")
    print(user_id)
else:
    print("None")
