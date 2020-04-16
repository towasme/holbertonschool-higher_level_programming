#!/usr/bin/python3
""" python script
"""
import requests
from sys import argv


if __name__ == "__main__":
    username = argv[1]
    token = argv[2]
    url = 'https://api.github.com/user'
    r = requests.get(url, auth=(username, token))
    try:
        r_json = r.json()
        print(r_json['id'])
    except:
        print("None")
