#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary:
        for x, y in a_dictionary.items():
            print("{}: {}".format(x, y))
