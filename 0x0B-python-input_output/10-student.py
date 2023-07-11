#!/usr/bin/python3
"""10. Student to JSON with filter"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if not attrs:
            return self.__dict__
        dic = {}
        for i in attrs:
            if i in self.__dict__.keys() and type(i) == str:
                dic[i] = self.__dict__[i]
        return dic
