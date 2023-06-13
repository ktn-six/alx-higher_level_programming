#!/usr/bin/python3
# 5-no_c.py


def no_c(my_string):
    """characters c and C from a stringa are removed."""
    copy = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(copy))


