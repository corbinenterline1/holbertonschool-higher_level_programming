#!/usr/bin/python3
"""0x0B - 3 - Write to a file"""


def write_file(filename="", text=""):
    """write_file writes a string to a text file (UTF8) & returns the number
    of characters written.

    Args:
        filename: name of file
        text: string to be written
        """
    with open(filename, 'w') as f:
        f.write(text)
    return len(text)
