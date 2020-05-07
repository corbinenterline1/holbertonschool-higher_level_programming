#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or not roman_string:
        return (0)
    b = 0
    for i in range(len(roman_string)):
        if roman_string[i] == 'I':
            b += 1
        elif roman_string[i] == 'V':
            if roman_string[i - 1] == 'I':
                b -= 1
                b += 4
            else:
                b += 5
        elif roman_string[i] == 'X':
            if roman_string[i - 1] == 'I':
                b -= 1
                b += 9
            else:
                b += 10
        elif roman_string[i] == 'L':
            if roman_string[i - 1] == 'X':
                b -= 10
                b += 40
            else:
                b += 50
        elif roman_string[i] == 'C':
            if roman_string[i - 1] == 'X':
                b -= 10
                b += 90
            else:
                b += 100
        elif roman_string[i] == 'D':
            if roman_string[i - 1] == 'C':
                b -= 100
                b += 400
            else:
                b += 500
        elif roman_string[i] == 'M':
            if roman_string[i - 1] == 'C':
                b -= 100
                b += 900
            else:
                b += 1000
    return (int(b))
