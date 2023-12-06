#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    top = 0
    bottom = 0
    for element in my_list:
        top = top + (element[0] * element[1])
        bottom += element[1]
    return top/bottom
