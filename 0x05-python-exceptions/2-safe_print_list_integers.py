#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed: int = 0
    for number in range(x):
        try:
            print("{:d}".format(my_list[number]), end="")
            printed += 1
        except Exception as e:
            continue
    print()
    return printed
