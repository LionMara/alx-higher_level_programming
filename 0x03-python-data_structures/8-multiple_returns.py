#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == None:
        tuple1 = len(sentence), None,
        return tuple1
    tuple1 = len(sentence), sentence[0]
    return tuple1
