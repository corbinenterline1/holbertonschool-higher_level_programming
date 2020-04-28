#!/usr/bin/python3
def fizzbuzz():
    a = 1
    while a < 101:
        if a % 3 == 0 and a % 5 == 0:
            b = "FizzBuzz"
        elif a % 3 == 0:
            b = "Fizz"
        elif a % 5 == 0:
            b = "Buzz"
        else:
            b = a
        print("{}".format(b), end=' ')
        a += 1
