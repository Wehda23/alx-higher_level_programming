#!/usr/bin/python3
import sys
if len(sys.argv) == 1:
    print("0 arguments.")
else:
    print("{} arguments:".format(len(sys.argv) - 1))
    for number, argument in enumerate(sys.argv[1:], start = 1):
        print("{}: {}".format(number, argument))

