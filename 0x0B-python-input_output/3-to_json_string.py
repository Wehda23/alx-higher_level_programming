#!/usr/bin/python3

"""
File that contains a function that jsonify object
"""

import json


def to_json_string(my_obj):
    """
    Function that jsonify an object.
    """
    return json.dumps(my_obj)
