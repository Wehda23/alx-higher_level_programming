#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [number if number != search else replace for number in my_list]
