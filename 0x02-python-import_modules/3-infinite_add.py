#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    count = 1
    tsum = 0
    arglen =  len(argv) - 1

    if (arglen > 0):
        while (count <= arglen):
            tsum += int(argv[count])
            count += 1
    print(tsum)