#!/usr/bin/python3
def fizzbuzz():
    for j in range(1, 101):
        if j % 3 == 0 and j % 5 == 0:
            print("FizzBuzz ", end="")
        elif j % 5 == 0:
            print("Buzz ", end="")
        elif j % 3 == 0:
            print("Fizz ", end="")
        else:
            print(f"{j} ", end="")
