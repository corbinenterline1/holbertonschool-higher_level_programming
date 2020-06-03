#!/usr/bin/python3
import json
"""0x0B - 7 - Save Object to a file"""


def save_to_json_file(my_obj, filename):
    """save_to_json_file writes an Object to a text file,
    using a JSOn representation.

    Args:
        my_obj: object to be written to file using JSON repr
        filename: name of text file
        """

    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
