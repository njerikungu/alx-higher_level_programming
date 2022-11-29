#!/usr/bin/python3
for letters in range(97, 123):
    if chr(letters) != 101 and chr(letters) != 123:
        print("{}".format(chr(letters)), end="")
