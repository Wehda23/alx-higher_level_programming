#!/usr/bin/python3
import sys

arguments: list = sys.argv

# Check the length of arguements should be exactly 2
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

# Grab the arguement
N = sys.argv[1]

# Check if N is an integer
if not isinstance(N, int):
    print("N must be a number")
    sys.exit(1)

# N must be greater or equal to 4
if N < 4:
    print("N must be at least 4")
    sys.exit(1)
