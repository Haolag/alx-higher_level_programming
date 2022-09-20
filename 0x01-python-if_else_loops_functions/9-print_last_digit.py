#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        lastdig = (number * -1) % 10
    else:
        lastdig = number % 10
    print("{}".format(lastdig), end="")
    return lastdig
