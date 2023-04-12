#!/usr/bin/python3
""" Function that appends a string at the end of a text file """


def append_write(filename="", text=""):
    """ Appends text file and returns num of chars added """
    with open(filename, "a", encoding="utf-8") as f:
        return(f.write(text))
