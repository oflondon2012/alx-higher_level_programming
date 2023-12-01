#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if (__name__ == "__main__"):
    arglen = len(argv)
    ret = 0
    operators = ["+", "-", "*", "/"]

    if (arglen != 4):
        print(f"Usage: {argv[0]} <a> <operator> <b>")
        exit(1)

    if (argv[2] not in operators):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    oprand = argv[2]
    b = int(argv[3])

    if (oprand == "+"):
        ret = add(a, b)
    elif (oprand == "-"):
        ret = sub(a, b)
    elif (oprand == "*"):
        ret = mul(a, b)
    else:
        ret = div(a, b)
    print(f"{a} {oprand} {b} = {ret}")
