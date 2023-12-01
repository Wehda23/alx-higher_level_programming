#!/usr/bin/python3
import sys

if __name__ != "__main__":
    exit()

if len(sys.argv) == 1:
    print("0")
else:
    numbers= sys.argv[1:]
    total= 0
    for number in numbers:
        total += int(number)
    print(total)
