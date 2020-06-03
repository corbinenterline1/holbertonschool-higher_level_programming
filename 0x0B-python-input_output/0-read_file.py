#!/usr/bin/python3
"""0x0B - 0 - Read file"""


def read_file(filename=""):
    with open(filename) as f:
        for line in f:
            print(line, end='')
