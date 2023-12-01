#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for function in sorted(dir(hidden_4)):
        if function[:2] != "__":
            print("{}".format(function))
