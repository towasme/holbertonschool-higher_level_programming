#!/usr/bin/python3
import json
"""
function that returns and object represented by json string
"""


def from_json_string(my_str):
    return (json.loads(my_str))
