#!/usr/bin/python3

"""
File contains A COOL function
"""


import json


def load_from_json_file(filename):
    """
    function that loads stuff from json file
    """
    with open(filename, mode="r", encoding='utf-8') as file:
        data = json.loads(file.read())
        return data
