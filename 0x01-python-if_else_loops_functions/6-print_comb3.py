#!/usr/bin/python3
t = 0
o = 1
while t < 9:
    while o <= 9 and t != 8:
        if o != t:
            print("{:d}{:d}".format(t, o), end=", ")
        o += 1
    t += 1
    o = t
print("{:d}{:d}".format(t - 1, o))
