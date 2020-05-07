#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary:
        doubled = a_dictionary.copy()
        for a in doubled:
            abs(doubled[a])
            doubled[a] *= 2
        return (doubled)

