#!/usr/bin/python3
"""0x0B - 8 - Create object from a JSON file"""
import json


def load_from_json_file(filename):
    """load_from_json_file creates an Object from a "JSON file".

    Args:
        filename: name of file
        """
    with open(filename) as f:
        jobj = json.loads(f.read())
    return jobj
