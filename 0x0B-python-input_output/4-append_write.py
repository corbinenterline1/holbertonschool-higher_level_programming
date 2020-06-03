#!/usr/bin/python3
"""0x0B - 4 - Append to a file"""


def append_write(filename="", text=""):
    """append_write appends a string at the end of a UTF8 text file.
    Returns number of characters added.

    Args:
        filename: name of file
        text: text to be appended
        """
    with open(filename, 'a') as f:
        f.write(text)
    return len(text)
