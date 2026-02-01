#!/usr/bin/python3
"""Module 1-write_file
Contains function write_file that writes a string to a UTF-8 text file.
"""


def write_file(filename="", text=""):
    """Write a string to a UTF-8 text file and return chars count."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
