#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        sorty = sorted(a_dictionary.items(), key=lambda x: x[1], reverse=True)
        a, b = (sorty[0])
        return (a)
