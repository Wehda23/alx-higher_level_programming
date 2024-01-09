#!/usr/bin/python3

"""
File contains function that reads files
"""


def write_file(filename: str = "", text: str = "") -> int:
    """Writes to a file and returns length of string"""
    with open(filename, encoding="utf-8", mode="w") as file:
        return file.write(text)
