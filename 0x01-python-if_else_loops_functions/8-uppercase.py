#!/usr/bin/python3
def uppercase(str):
    b = 0
    for a in str:
        b = ord(a)
        if b > 96 and b < 123:
            b -= 32
        print("{:c}".format(b), end='')
    print("")
