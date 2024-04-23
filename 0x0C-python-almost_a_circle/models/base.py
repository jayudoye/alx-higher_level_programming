#!/usr/bin/python3
"""This module defines a model blueprint"""
import json
import os
import csv
from turtle import Turtle as t


class Base():
    """This class define a blueprint for creating objects"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization Method"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves json string to a file"""

        filename = "{:s}.json".format(cls.__name__)

        if list_objs is None:
            with open(filename, "w", encoding="utf-8") as file:
                file.write("[]")
        else:
            with open(filename, "w", encoding="utf-8") as file:
                new_list = []
                for instance in list_objs:
                    new_list.append(instance.to_dictionary())
                new_list_str = cls.to_json_string(new_list)
                file.write(new_list_str)

    @staticmethod
    def from_json_string(json_string):
        """From JSON to dictionary"""

        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Reconstruct a python 'list of dictionaries'
        object from a json string representation
        """

        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 2)
        if cls.__name__ == "Square":
            dummy_instance = cls(5)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Reconstruct list of instances from a file"""

        filename = "{:s}.json".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []
        with open(filename, "r", encoding="utf-8") as file:
            json_string = file.read()
            json_to_list_of_dict = cls.from_json_string(json_string)
            instance_list = []
            for dict_ in json_to_list_of_dict:
                instance_list.append(cls.create(**dict_))
        return instance_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes in CSV format"""

        filename = "{:s}.csv".format(cls.__name__)

        with open(filename, 'w', newline='', encoding='utf-8') as csv_file:
            output_writer = csv.writer(csv_file)
            for instance in list_objs:
                if instance.__class__.__name__ == "Rectangle":
                    output_writer.writerow([
                        instance.id,
                        instance.width,
                        instance.height,
                        instance.x,
                        instance.y
                        ])
                    if instance.__class__.__name__ == "Square":
                        output_writer.writerow([
                            instance.id,
                            instance.size,
                            instance.x,
                            instance.y
                            ])

                        @classmethod
    def load_from_file_csv(cls):
        """deserializes in CSV format"""

        filename = "{:s}.csv".format(cls.__name__)

        with open(filename, encoding='utf-8') as csv_file:
            output_reader = csv.reader(csv_file)
            list_objs = []

            for row in output_reader:
                if len(row) == 5:
                    dummy_instance = cls(1, 2)
                    dummy_instance.id = int(row[0])
                    dummy_instance.width = int(row[1])
                    dummy_instance.height = int(row[2])
                    dummy_instance.x = int(row[3])
                    dummy_instance.y = int(row[4])
                    list_objs.append(dummy_instance)
                if len(row) == 4:
                    dummy_instance = cls(5)
                    dummy_instance.id = int(row[0])
                    dummy_instance.size = int(row[1])
                    dummy_instance.x = int(row[2])
                    dummy_instance.y = int(row[3])
                    list_objs.append(dummy_instance)

            return list_objs

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw rectangles and squares"""

        pen = t()
        pen.getscreen()

        # rectangle features
        pen.shape("turtle")
        pen.color("red", "green")

        # turtle speed
        pen.speed(1)

        pen.hideturtle()

        # shape tracing and dimensioning
        for instance in list_rectangles:
            pen.pendown()
            pen.begin_fill()
            pen.fd(instance.width)
            pen.lt(90)
            pen.fd(instance.height)
            pen.lt(90)
            pen.fd(instance.width)
            pen.lt(90)
            pen.fd(instance.height)
            pen.end_fill()
            pen.penup()
            pen.fd(1.5 * instance.width)

        pen.color("red", "violet")

        # square features
        pen.lt(90)
        pen.fd(500)
        for instance in list_squares:
            pen.pendown()
            pen.begin_fill()
            pen.fd(instance.width)
            pen.lt(90)
            pen.fd(instance.height)
            pen.lt(90)
            pen.fd(instance.width)
            pen.lt(90)
            pen.fd(instance.height)
            pen.end_fill()
            pen.penup()
            pen.fd(1.5 * instance.width)

        pen.screen.mainloop()
