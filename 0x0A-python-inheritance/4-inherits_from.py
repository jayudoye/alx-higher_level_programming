
#!/usr/bin/python3

""" returns True if the object is an instance of a class that inherited
(directly or indirectly) from the specified class ; otherwise False."""


def inherits_from(obj, a_class):
    """Check if obj inherits from a_class"""
    if obj.__class__ == a_class:
        return False
    return isinstance(obj, a_class) or issubclass(obj.__class__, a_class)
