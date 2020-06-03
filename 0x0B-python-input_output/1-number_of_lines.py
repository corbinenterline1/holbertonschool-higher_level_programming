#!/usr/bin/python3
"""0x0B - 1 - Number of lines"""


def number_of_lines(filename=""):
    """Number of lines returns the number of lines of a text file.

    Args:
        filename: name of file to count lines
        """
    lc = 0
    with open(filename) as f:
        for line in f:
            lc += 1
    return lc
