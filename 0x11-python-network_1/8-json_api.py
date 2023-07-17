#!/usr/bin/python3
"""
  8-json_api.py
  script that takes in a letter
  sends a POST request to http://0.0.0.0:5000/search_user
"""

import sys
import requests

letter = sys.argv[1] if len(sys.argv) > 1 else ""


params = {"q": letter}

response = request.post("http://0.0.0.0:5000/search_user", data=params)

try:
    data = response.json()
    if data:
        user_id = data.get("id")
        user_name = data.get("name")
        print(f"[{user_id}] {user_name}")
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")
