#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    counter = 1
    arglen = len(argv) - 1
    print(f"{arglen} {'argument' if arglen == 1 else 'arguments'}", end="")
    print(f"{'.' if arglen == 0 else ':'}")
    while (counter <= arglen):
        print(f"{counter}: {argv[counter]}")
        counter = counter + 1
