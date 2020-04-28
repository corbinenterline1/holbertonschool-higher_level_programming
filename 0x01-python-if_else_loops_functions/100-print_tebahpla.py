#!/usr/bin/python3
flag = 0
for i in range(122, 96, -1):
    a = i
    if flag == 1:
        a = i - 32
    print("{:c}".format(a), end='')
    if flag == 1:
        flag = 0
    else:
        flag = 1
