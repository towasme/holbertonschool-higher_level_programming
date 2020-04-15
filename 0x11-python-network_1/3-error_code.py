#!/usr/bin/python3
""" python script
"""
import sys
import urllib.request
import urllib.parse


url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    html = response.read()
    print(html)
