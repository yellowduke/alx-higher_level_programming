#!/usr/bin/python3
""" Defines the class Student """


class Student:
    """ Defines a student by public instance attributes """

    def __init__(self, first_name, last_name, age):
        """ Define by Instantiation method """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Retrieves a dictionary representation """
        return self.__dict__.copy()
