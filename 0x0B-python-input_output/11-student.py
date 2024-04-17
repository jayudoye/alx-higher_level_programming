
#!/usr/bin/python3
"""
Write a class Student that defines a student by: (based on 10-student.py)

Public instance attributes:
first_name
last_name
age
Instantiation with first_name, last_name and age:
def __init__(self, first_name, last_name, age):
Public method def to_json(self, attrs=None): that retrieves a dictionary
representation of a Student instance (same as 8-class_to_json.py):
If attrs is a list of strings, only attributes name contain in this
list must be retrieved.
Otherwise, all attributes must be retrieved
Public method def reload_from_json(self, json): that replaces all
attributes of the Student instance:
You can assume json will always be a dictionary
A dictionary key will be the public attribute name
A dictionary value will be the value of the public attribute
You are not allowed to import any module
"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Initialization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the specified student attributes"""
        if type(attrs) != list:
            return self.__dict__
        return {k: v for k, v in self.__dict__.items() if k in attrs}

    def reload_from_json(self, json):
        """Replace attribute values of an instance with new ones"""
        for k, v in json.items():
            if k in self.__dict__:
                setattr(self, k, v)
