#!/usr/bin/python3
""" python script
"""
import sys
import urllib.request
import urllib.error


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as resp:
        html = resp.code
        print("Error code: {}".format(html))
