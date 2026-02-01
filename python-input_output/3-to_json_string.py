#!/usr/bin/python3
"""Module 3-to_json_string
Contains function to_json_string that returns the JSON string of an object.
"""

import json


def to_json_string(my_obj):
    """Return the JSON representation (string) of an object."""
    return json.dumps(my_obj)
