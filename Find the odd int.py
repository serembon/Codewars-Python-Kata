"""
Given an array, find the integer that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
"""


# My solution

def find_it1(seq):
    res = 0
    for element in seq:
        res = res ^ element
    return res


# Best way


def find_it2(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i
