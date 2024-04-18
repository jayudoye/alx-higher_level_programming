#!/usr/bin/python3

"""Add custom attribute to an object"""


def add_attribute(obj, att, value):
    """Add attribute to an object"""
    if hasattr(obj, "__dict__"):
        setattr(obj, att, value)
    else:
        raise TypeError("can't add new attribute")
