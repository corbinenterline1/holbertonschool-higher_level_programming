#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary:
        doubled = a_dictionary.copy()
        for a in doubled:
            doubled[a] *= 2
        return (doubled)
