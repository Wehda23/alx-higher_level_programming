#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        a, b = args
        result = fct(a, b)
        return result
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
