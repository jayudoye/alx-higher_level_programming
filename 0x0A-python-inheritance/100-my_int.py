#!/usr/bin/python3

"""Let's create some confusion - because we can :)"""


class MyInt(int):
    """
    This class is intentionally misleading.
    Good thing we know what we are doing
    """

    def __eq__(self, other):
        return not super().__eq__(other)

    def __ne__(self, other):
        return not super().__ne__(other)
