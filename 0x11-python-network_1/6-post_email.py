#!/usr/bin/python3
""" python script
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    data = {'email': sys.argv[2]}
    r = requests.post(url, data)
    print(r.text)
