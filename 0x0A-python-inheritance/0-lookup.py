#!/usr/bin/python3

"""Print a list of attributes of an object"""


def lookup(obj):
    """Returns the attributes of the passed object"""
    return dir(obj)
