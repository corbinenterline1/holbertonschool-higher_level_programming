#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    divlist = []
    a = 0
    for value in range(list_length):
        try:
            a = my_list_1[value] / my_list_2[value]
        except (TypeError):
            a = 0
            print("wrong type")
        except (ZeroDivisionError):
            a = 0
            print("division by 0")
        except (IndexError):
            a = 0
            print("out of range")
        finally:
            divlist.append(a)
    return(divlist)
