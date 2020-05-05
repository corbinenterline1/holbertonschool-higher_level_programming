#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)
    a = my_list.index(idx + 1)
    new_list = list.copy(my_list)
    new_list[a] = element
    return (new_list)
