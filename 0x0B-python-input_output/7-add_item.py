#!/usr/bin/python3
"""
Student module
"""
from sys import argv
from os import path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_items():
    """
    function to add items
    """
    name = "add_item.json"
    if path.isfile(name):
        f_list = load_from_json_file(name)
    else:
        f_list = []
    for i in range(1, len(argv)):
        f_list.append(argv[i])
    save_to_json_file(f_list, name)


add_items()
