#!/usr/bin/python3
import json
"""
function that creates an object from a json file
"""


def load_from_json_file(filename):
    with open(filename, 'r', encoding='UTF-8') as file:
        return (json.load(file))
