#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        val = int(value)
        print("{:d}".format(val))
        return True
    except (ValueError, TypeError) as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
