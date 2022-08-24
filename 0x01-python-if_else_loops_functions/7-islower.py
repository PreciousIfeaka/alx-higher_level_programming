#!/usr/bin/python3
def islower(c):
    for alph in range(chr(97), chr(123)):
        if c == alph:
            return True
    if ord(c) < 97 or ord(c) > 122:
        return False
