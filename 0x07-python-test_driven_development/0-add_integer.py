#!/usr/bin/python3
def add_integer(a, b=98) -> int:
    """
    Function that adds 2 integers

    Args:
        - a: integer value
        - b: integer value (default: 98)

    Returns:
        - Sum of both integers
    """
    # Check type of a
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    # Check type of b
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    # Cast them into int and then add.
    return int(a) + int(b)
