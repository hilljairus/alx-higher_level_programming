#!/usr/bin/python3
from operator import ne


def no_c(my_string):

    new_string = ''

    for letter in my_string:
        if letter == 'c' or letter == 'C':
            pass
        else:
            new_string += letter

    return new_string
