#!/usr/bin/python3

"""
File that contains a class called MyList
"""


class MyList(list):
    """
    Class that inherits from list class
    """
    def print_sorted(self):
        """
        Prints the list, but sorteded (ascending)
        Also does not affect original list.

        Args:
            - self: python data structure list
        """
        new_list: list = sorted(self)
        print(new_list)
