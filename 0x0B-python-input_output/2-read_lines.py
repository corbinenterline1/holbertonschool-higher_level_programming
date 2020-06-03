#!/usr/bin/python3
"""0x0B - 2 - Read n lines"""


def read_lines(filename="", nb_lines=0):
    """Read lines reads n lines of a text file and prints it to stdout.

    Args:
        filename: name of file
        nb_lines: number of lines to read. Read the entire file if
        lower or equal to 0, OR greater or equal to
        the total number of lines of the file.
        """
    lc = 0
    with open(filename) as f:
        for line in f:
            if lc != nb_lines or nb_lines <= 0:
                print(line, end='')
                lc += 1
            else:
                break
