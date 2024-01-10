#!/usr/bin/python3
"""
Module that create an object form JSON
"""
import json


def load_from_json_file(filename):
    """
    function that create objec from JSON
    """
    with open(filename, "r") as f:
        return json.loads(f.readline())
