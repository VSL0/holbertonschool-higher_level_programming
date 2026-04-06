#!/usr/bin/python3
"""Module for Roman to Integer conversion"""


def roman_to_int(roman_string):
    """Converts a Roman numeral to an integer"""
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    total = 0
    for i in range(len(roman_string)):
        val = roman_dict.get(roman_string[i], 0)
        # Check if the next value is larger (subtraction rule)
        if i + 1 < len(roman_string) and \
           val < roman_dict.get(roman_string[i + 1], 0):
            total -= val
        else:
            total += val
    return total
