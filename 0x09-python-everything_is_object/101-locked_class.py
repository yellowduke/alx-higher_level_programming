#!/usr/bin/python3
"""
Defines a class with no class or object attributes
"""

class LockedClass:
    """
    Prevents the user from dynamically creating new instance attributes except new intamce attribute is called first_name
    """

    __slots__ = ["first_name"]

    def __init__(self, first_name):
        pass
