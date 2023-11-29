#!/usr/bin/python3
def uppercase(str):
    for char in range(len(str)):
        if ord(str[char]) >= 97 and ord(str[char]) <= 122:
            number = 32
        else:
            number = 0
        print("{:c}".format(ord(str[char]) - number), end="")
    print()
