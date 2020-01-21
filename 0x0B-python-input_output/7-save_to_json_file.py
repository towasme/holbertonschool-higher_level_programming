#!/usr/bin/python3
import json
"""
function that reads a text file
"""


def save_to_json_file(my_obj, filename):
    with open(filename, 'w',  encoding='utf-8') as file:
        return file.write(json.dumps(my_obj))
