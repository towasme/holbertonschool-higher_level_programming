#!/usr/bin/python3
"""
python script
"""
import requests
import sys


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) == 2:
        data = {'q': sys.argv[1]}
    else:
        data = {'q': ""}
    r = requests.post(url, data)
    try:
        r_json = r.json()
        if len(r_json) == 0:
            print("No result")
        else:
            print("[{}] {}".format(r_json.get('id'), r_json.get('name')))
    except:
        print("Not a valid JSON")
