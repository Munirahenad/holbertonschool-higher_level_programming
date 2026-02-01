#!/usr/bin/python3
"""Module 2-append_write
Contains function append_write that appends a string to a UTF-8 text file.
"""


def append_write(filename="", text=""):
    """Append a string to a UTF-8 text file and return chars count."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
