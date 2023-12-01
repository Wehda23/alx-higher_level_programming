#!/usr/bin/python3
import sys

if __name__ != "__main__":
    exit()

if len(sys.argv) == 1:
    print("0 arguments.")
else:
    note = "argument" if len(sys.argv) == 2 else "arguments"
    print("{} {}:".format(len(sys.argv) - 1, note))
    for number, argument in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(number, argument))
