#!/usr/bin/python3

"""
An abstract base class
"""
import json
import csv
import turtle


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializer"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def id(cls):
        """Used in tests to retrieve the last id value"""
        return cls.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Dumps a list of dicts to a json string
        :param list_dictionaries: a list of python dictionaries
        :return: A JSON string
        """
        return json.dumps(list_dictionaries or [])

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves objects to a json file
        :param list_objs: The objects to save
        """
        if not list_objs:
            list_objs = []
        dicts = [obj.to_dictionary() for obj in list_objs]
        data = cls.to_json_string(dicts)
        with open(f"{cls.__name__}.json",
                  mode='w+', encoding='utf-8') as f:
            f.write(data)

    @staticmethod
    def from_json_string(json_string):
        """
        Retrieves data from a json string
        :param json_string: a json string
        :return: a python object derived from the json string
        """
        return json.loads(json_string) if json_string else []

    @classmethod
    def create(cls, **dictionary):
        """
        Creates an instance of rectangle or square from a dictionary
        :param dictionary: the kwargs for updating the instance attributes
        :return: the newly created instance
        """
        if 'size' in dictionary:
            obj = cls(size=10)
        else:
            obj = cls(height=5, width=10)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """
        Loads a json file and creates square or
        rectangle instances from the loaded data
        :return: The created rectangles or squares
        """
        file_name = f"{cls.__name__}.json"

        try:
            with open(file_name, mode="r", encoding="utf-8") as f:
                data = f.read()
                list_dicts = cls.from_json_string(data)
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    def get_csv_values(self):
        """
        Computes the csv representation of a Rectangle or Square
        :return: The column values to save to csv
        """
        if self.__class__.__name__ == "Rectangle":
            return [self.id, self.width, self.height, self.x, self.y]
        else:
            return [self.id, self.size, self.x, self.y]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Saves objects to a csv file
        :param list_objs: The objects to save
        """
        file_name = f"{cls.__name__}.csv"
        if 'Rectangle' in file_name:
            header = ["id", "width", "height", "x", "y"]
        else:
            header = ["id", "size", "x", "y"]

        with open(file_name, mode="w+", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(header)
            data = [obj.get_csv_values() for obj in list_objs]
            if data:
                writer.writerows(data)

    @classmethod
    def load_from_file_csv(cls):
        """
        Loads a csv file and creates square or
        rectangle instances from the loaded data
        :return: The created rectangles or squares
        """
        file_name = f"{cls.__name__}.csv"

        try:
            with open(file_name, mode="r", encoding="utf-8") as f:
                data = list(csv.reader(f))
                if not data:
                    return []
                keys = data[0]
                vals_list = data[1:]
                list_dicts = [dict(zip(keys, map(int, vals))) for
                              vals in vals_list]
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draws all rectangles and squares
        :param list_rectangles: rectangles to draw
        :param list_squares: squares to draw
        """
        t = turtle.Turtle()
        t.screen.bgcolor("#7CFC00")
        t.pensize(3)
        t.shape("turtle")
        t.color("#FF5733")
        for r in list_rectangles:
            t.showturtle()
            t.up()
            t.goto(r.x, r.y)
            t.down()
            t.forward(r.width)
            t.right(90)
            t.forward(r.height)
            t.right(90)
            t.forward(r.width)
            t.right(90)
            t.forward(r.height)
            t.hideturtle()
        t.color("#000000")
        for s in list_squares:
            t.showturtle()
            t.up()
            t.goto(s.x, s.y)
            t.down()
            t.forward(s.size)
            t.right(90)
            t.forward(s.size)
            t.right(90)
            t.forward(s.size)
            t.right(90)
            t.forward(s.size)
            t.hideturtle()
        turtle.exitonclick()
