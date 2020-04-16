#!/usr/bin/python3
""" python script
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        r = requests.get(url)
        if r.raise_for_status() is None:
            print(r.text)
    except:
        print("Error code: {}".format(r.status_code))
