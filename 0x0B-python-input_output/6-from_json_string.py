#!/usr/bin/python3
import json
"""0x0B - 6 - From JSON to Object"""


def from_json_string(my_str):
    """from_json_string returns an object (Python data structure)
    represented by a JSON string.

    Args:
        my_str: string JSON to convert to a python object
        """
    robj = json.loads(my_str)
    return robj
