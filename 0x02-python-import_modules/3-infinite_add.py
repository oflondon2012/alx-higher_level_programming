#!/usr/bin/python3


def addarg(argv):
    arglen = len(argv) - 1
    if arglen == 0:
        print("{:d}".format(arglen))
        return
    else:
        count = 1
        sum = 0
        while count <= arglen:
            sum += int(argv[count])
            count += 1
        print("{:d}".format(sum))


if __name__ == "__main__":
    import sys
    addarg(sys.argv)
