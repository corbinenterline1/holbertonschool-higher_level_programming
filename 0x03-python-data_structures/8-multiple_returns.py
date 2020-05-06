#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        a = sentence[0]
    else:
        a = None
    l = len(sentence)
    return ((l, a))
