#!/usr/bin/python3
def multiple_returns(sentence):
    size = len(sentence)
    f_car = sentence[0] if size > 0 else None
    return size, f_car
