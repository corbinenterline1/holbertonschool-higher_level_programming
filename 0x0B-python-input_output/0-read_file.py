#!/usr/bin/python3
"""0x0B - 0 - Read file"""


def read_file(filename=""):
    """read file function. Prints file one line at a time."""
    with open(filename) as f:
        for line in f:
            print(line, end='')
