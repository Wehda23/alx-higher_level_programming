#!/usr/bin/python3

"""
File contains function that reads files
"""


def read_file(filename: str = ""):
    """Reads a file and returns its content as string."""
    with open(filename, encoding="utf-8", mode="r") as file:
        print(file.read(), end="")
