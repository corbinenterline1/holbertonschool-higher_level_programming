#!/usr/bin/python3
"""0x0B - 5 - To JSON string"""
import json


def to_json_string(my_obj):
    """to_json_string returns the JSON representation of an object (string)
    """
    robj = json.dumps(my_obj)
    return robj
