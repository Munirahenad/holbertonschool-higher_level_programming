#!/usr/bin/python3
"""Module 5-text_indentation
Contains function text_indentation.
"""


def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters: ., ? and :.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    n = len(text)

    while i < n and text[i] == ' ':
        i += 1

    while i < n:
        ch = text[i]
        print(ch, end="")

        if ch in ".?:":
            print("\n")
            i += 1
            while i < n and text[i] == ' ':
                i += 1
            continue

        i += 1

