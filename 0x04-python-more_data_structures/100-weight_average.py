#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0);
    scorelist = [(x * y) for x, y in my_list]
    score = sum(scorelist)
    weightlist = [i[1] for i in my_list]
    weight = sum(weightlist)
    return (score / weight)
