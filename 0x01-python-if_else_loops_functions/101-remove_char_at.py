#!/usr/bin/python3
def remove_char_at(str, n):
    newnode = ""
    j = 0
    for ch in str:
        if j != n:
            newnode = newnode + ch
        j = j + 1
    return newnode
