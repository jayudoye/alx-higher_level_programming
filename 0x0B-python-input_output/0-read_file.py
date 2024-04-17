#!/usr/bin/python3

"""Reads and prints the content of a file"""


def read_file(filename=""):
    """Read file"""
    with open(filename, encoding="utf-8", mode="r") as f:
        data = f.read()
        print(data, end="")
