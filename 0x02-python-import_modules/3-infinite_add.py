#!/usr/bin/python3
if __name__ == '__main__':
    import sys
b = 0
c = 0
a = 1
l = len(sys.argv) - 1
if l <= 0:
    print("{:d}".format(b))
elif l == 1:
    c = int(sys.argv[a])
    b += c
    print("{:d}".format(b))
else:
    while l > 0:
        c = int(sys.argv[a])
        b += c
        a += 1
        l -= 1
    print("{:d}".format(b))
