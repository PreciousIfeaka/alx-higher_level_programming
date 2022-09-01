#!/usr/bin/python3
def roman_to_int(roman_string):
    rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if not roman_string or roman_string is None:
        return 0
    else:
        i = 0
        for m in range(len(roman_string)):
            if rom[roman_string[m]] > rom[roman_string[m - 1]] and m > 0:
                i += rom[roman_string[m]] - 2 * rom[roman_string[m - 1]]
            else:
                i = i + rom[roman_string[m]]
        return i
