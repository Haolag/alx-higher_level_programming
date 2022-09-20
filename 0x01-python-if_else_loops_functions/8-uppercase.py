#!/usr/bin/python3
def uppercase(str):
    strup = ""
    for i in range(len(str)):
        if ord(str[i]) >= ord('a') and ord(str[i]) <= ord('z'):
            strup = ord(str[i]) - 32
        else:
            strup = ord(str[i])
        print("{:c}".format(strup), end="")
    print()
