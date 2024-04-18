#!/usr/bin/python3

"""Custom List class that prints sorted items"""


class MyList(list):
    """Custom list"""
    def print_sorted(self):
        """prints items in sorted order"""
        print(sorted(self.__iter__()))
