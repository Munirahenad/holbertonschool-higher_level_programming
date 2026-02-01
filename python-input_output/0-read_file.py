#!/usr/bin/python3
"""Module 0-read_file
Contains function read_file that reads a UTF-8 text file and prints to stdout.
"""


def read_file(filename=""):
    """Reads a text file (UTF-8) and prints it to stdout."""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
