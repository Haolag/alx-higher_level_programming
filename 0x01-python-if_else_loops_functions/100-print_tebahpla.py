#!/usr/bin/python3
for x in range(122, 96, -1):
    if (x % 2) == 0:
        letter = x
    else:
        letter = x - 32
    print("{}".format(chr(letter)), end='')
