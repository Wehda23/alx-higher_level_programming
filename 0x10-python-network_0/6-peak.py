#!/usr/bin/python3
# Program that finds a peak 


def find_peak(list_of_integers) -> int:
    """
    Function used to find the highest number in a list

    Args:
        - list_of_integers (list[int): List contains integer values

    Return:
        - Integer value
    """
    # Check situations
    if not list_of_integers:
        return None
    
    if len(list_of_integers) == 1:
        return list_of_integers[0]

    new_set: set = set(list_of_integers)
    return list(new_set).pop()
