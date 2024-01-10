#!/usr/bin/python3

"""
File that contains a cool function
"""


import json


def save_to_json_file(my_obj, filename):
    """Function that saves to json file"""
    with open(filename, mode="w", encoding="utf-8") as file:
        json_data = json.dumps(my_obj)
        file.write(json_data)
