#!/usr/bin/python3
def islower(c):
    for i in range(ord('a'), ord('z') + 1):
        if ord(c) == i:
            return True
    return False
