#!/usr/bin/python3
def uppercase(str):
    for index, character in enumerate(str):
        if ord(character) >= 97 and ord(character) <= 122:
            character = chr(ord(character) - 32)
        print("{}".format(character), end= "")
        if index == len(str) - 1:
            print("")
