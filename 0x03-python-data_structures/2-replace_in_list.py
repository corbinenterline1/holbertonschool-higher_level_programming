#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list):
        return (my_list)
    a = my_list.index(idx + 1)
    my_list[a] = element
    return (my_list)
