#!/usr/bin/python3
""" Script that adds all arguments to a python list """

from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    existing_item = load_from_json_file("add_item.json")
except FileNotFoundError:
    existing_item = []

save_to_json_file(existing_item, "add_item.json")
