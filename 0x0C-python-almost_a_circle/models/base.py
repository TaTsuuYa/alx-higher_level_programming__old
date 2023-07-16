#!/usr/bin/python3
"""
1. Base class,
15. Dictionary to JSON string,
16. JSON string to file,
17. JSON string to dictionary,
18. Dictionary to Instance
"""
from json import dumps, loads


class Base:
    """
    The base class for the upcoming tasks
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        constructor
        """
        if id is None:
            self.inc__nb_objects()
            self.id = self.__nb_objects
        else:
            self.id = id

    @classmethod
    def inc__nb_objects(cls):
        cls.__nb_objects += 1

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        stringify a dict as json
        """
        if list_dictionaries is None:
            return "[]"
        return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves the stringified version of the instance to a file
        """
        with open(f"{cls.__name__}.json", 'w', encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                lst = []
                for obj in list_objs:
                    lst.append(obj.to_dictionary())
                f.write(cls.to_json_string(lst))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return []
        return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        try:
            with open(f"{cls.__name__}.json", 'r', encoding="utf-8") as f:
                insts = cls.from_json_string(f.read())
                lst = []
                for inst in insts:
                    lst.append(cls.create(**inst))
                return lst
        except FileExistsError:
            return []
