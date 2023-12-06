#!/usr/bin/python3
def roman_to_int(roman_string):
    total = 0
    if isinstance(roman_string, str):
        roman = {
            "I": 1, "V": 5, "X": 10,
            "L": 50, "C": 100, "D": 500,
            "M": 1000,
        }
        prev_value = 0
        for roman_character in reversed(roman_string):
            current_value = roman[roman_character]
            if current_value >= prev_value:
                total += roman[roman_character]
            else:
                total -= current_value

            prev_value = current_value
    return total
