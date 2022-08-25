#!/usr/bin/python3
for ltr in range(ord('z'), ord('a') - 1, -1):
    if ltr % 2 != 0:
        ltr = ltr - 32
    print("{}".format(chr(ltr)), end="")
