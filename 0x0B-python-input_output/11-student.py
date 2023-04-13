#!/usr/bin/python3
""" Defines a class Student """


class Student():
    """ Define student by Public Instance Attributes """
    def __init__(self, first_name, last_name, age):
        """ By Instantiation """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves a dictionary representation of a Student instance """
        if attrs is None:
            return self.__dict__
        else:
            list_dic = {}
            for att in attrs:
                if att in self.__dict__.keys():
                    list_dic[att] = self.__dict__[att]
            return list_dic

	def reload_from_json(self, json):
        """ Replaces all attributes of the Student instance """
        for k, v in json.items():
            setattr(self, k, v)
