#!/usr/bin/python3
def safe_print_integer(value) -> bool:
    try:
        if not isinstance(value, int):
            raise TypeError("User other type")

        print("{:d}".format(value))
        return True
    except Exception as e:
        return False
