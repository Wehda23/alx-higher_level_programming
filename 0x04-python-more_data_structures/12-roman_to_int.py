#!/usr/bin/python3
def roman_to_int(roman_string):
    total = 0
    if isinstance(roman_string, str):
        roman = {
            "I": 1, "V": 5, "X": 10,
            "L": 50, "C": 100, "D": 500,
            "M": 1000,
        }
        for roman_character in roman_string:
            total += roman[roman_character]

    return total
