#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0:
        copystr = str[:n] + str[n + 1:]
    else:
        copystr = str[:]
    return (copystr)
