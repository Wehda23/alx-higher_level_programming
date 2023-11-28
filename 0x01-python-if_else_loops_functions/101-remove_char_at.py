#!/usr/bin/python3
def remove_char_at(str, n):
    return "".join([char for index, char in enumerate(str) if index != n])
