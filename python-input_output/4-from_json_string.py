#!/usr/bin/python3
"""Module 4-from_json_string
Contains function from_json_string that returns a Python object from a JSON string.
"""

import json


def from_json_string(my_str):
    """Return the Python object represented by a JSON string."""
    return json.loads(my_str)
