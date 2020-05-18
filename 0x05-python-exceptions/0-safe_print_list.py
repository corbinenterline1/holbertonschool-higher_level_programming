#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    d = 0
    try:
        for a in range(0, x):
            print(my_list[a], end='')
            d += 1
        print()
    except:
        print()
        return(d)
    return(d)
