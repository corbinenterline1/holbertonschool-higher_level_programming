#!/usr/bin/python3
if __name__ == '__main__':
        import sys
        l = len(sys.argv) - 1
        c = 1
        if l >= 1:
            if l == 1:
                print("{:d} argument:".format(l))
            else:
                print("{:d} arguments:".format(l))
            while l > 0:
                print("{:d}: {}".format(c, sys.argv[c]))
                l -= 1
                c += 1
        else:
            print("{:d} arguments.".format(l))
