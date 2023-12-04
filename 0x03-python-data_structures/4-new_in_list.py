#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copied_list = [element for element in my_list]
    if idx < 0 or idx >= len(my_list):
        return copied_list
    else:
        copied_list[idx] = element
        return copied_list
