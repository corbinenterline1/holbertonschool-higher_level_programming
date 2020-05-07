#!/usr/bin/python3
def uniq_add(my_list=[]):
    addset = set(my_list)
    a = 0
    while addset:
        a += addset.pop()
    return (a)
