#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for index, number in enumerate(my_list):
        if index + 1 == search:
            new_list.append(replace)
        else:
            new_list.append(number)
    return new_list
