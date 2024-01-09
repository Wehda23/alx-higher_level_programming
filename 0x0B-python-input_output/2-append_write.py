#!/usr/bin/python3

"""
File contains function that reads files
"""


def append_write(filename: str = "", text: str = "") -> int:
    """Writes to a file and returns length of string"""
    with open(filename, encoding="utf-8", mode="a") as file:
        return file.write(text)
