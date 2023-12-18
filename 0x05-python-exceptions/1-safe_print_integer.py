#!/usr/bin/python3
def safe_print_integer(value) -> bool:
    if isinstance(value, int):
        print("{:d}".format(value))
        return True
    return False
