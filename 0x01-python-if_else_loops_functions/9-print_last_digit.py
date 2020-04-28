#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        lastnum = number % 10
    else:
        lastnum = (abs(number) % 10)
    print("{:d}".format(lastnum), end='')
    return(lastnum)
