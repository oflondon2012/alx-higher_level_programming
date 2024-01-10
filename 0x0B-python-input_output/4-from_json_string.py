#!/usr/bin/python3
"""
Module that return an object
"""
import json


def from_json_string(my_str):
    """
    function that return an object
    """
    return json.loads(my_str)
