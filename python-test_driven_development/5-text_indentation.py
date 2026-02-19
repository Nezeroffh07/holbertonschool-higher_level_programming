#!/usr/bin/python3
"""Module for text_indentation method."""


def text_indentation(text):
    """Prints a text with 2 new lines after each '.', '?' and ':'."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    skip = True
    for c in text:
        if skip and c == ' ':
            continue
        skip = False
        print(c, end="")
        if c in ".?:":
            print("\n\n", end="")
            skip = True
