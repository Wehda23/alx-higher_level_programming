#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    names = []
    if value in a_dictionary.values():
        for key, val in a_dictionary.items():
            if val == value:
                names.append(key)

        if names:
            for name in names:
                a_dictionary.pop(name)
    return a_dictionary
