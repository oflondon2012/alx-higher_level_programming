#!/usr/bin/python3
"""
Module function that writes an Object to a text file, using a JSON
"""
import json


def save_to_json_file(my_obj, filename):
    """
    function that writes an object using JSON
    """
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
