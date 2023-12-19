#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    try:
        for k in range(list_length):
            try:
                lst1 = float(my_list_1[k])
                lst2 = float(my_list_2[k])
                if lst2 == 0:
                    result.append(0)
                    print("division by 0")
                else:
                    result.append(lst1 / lst2)
            except ValueError:
                result.append(0)
                print("wrong type")
            except IndexError:
                result.append(0)
                print("out of range")
    except ZeroDivisionError:
        result.append(0)
        print("division by 0")
    finally:
        return result
