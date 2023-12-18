#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        for number in range(x):
            print(my_list[number], end="")
        print()
    except:
        pass
