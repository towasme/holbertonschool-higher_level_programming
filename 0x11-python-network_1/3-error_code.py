#!/usr/bin/python3
""" python script
"""
import sys
import urllib.request
import urllib.error


if __name__ == "__main__":
    url = sys.argv[1]
    try:
            resp = (urllib.request.urlopen(url))
    except urllib.error.HTTPError as response:
            html = response.code
            print("Error code: {}".format(html))
    else:
            print(resp.read().decode('utf-8'))
