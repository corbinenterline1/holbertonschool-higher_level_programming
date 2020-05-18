#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    d = 0
    a = 0
    for a in range(0, x):
        try:
            print("{:d}".format(my_list[a]), end='')
            d += 1
        except (TypeError, ValueError):
            continue
        a += 1
    print()
    return(d)
