#!/usr/bin/python3
def safe_print_division(a, b):
    result: int = 0
    try:
        result = a/b
    except Exception as e:
        result = None
    finally:
        print("inside result: {}".format(result))

    return result
