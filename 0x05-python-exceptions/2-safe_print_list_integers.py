#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
        count = 0
        try:
            for j in range(x):
                value = my_list[j]
                if isinstance(value, int):
                    print("{:d}".format(my_list[value]), end="")
                    count += 1
        except (ValueError, TypeError, IndexError):
            pass
        print()
        return count
