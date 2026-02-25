#!/usr/bin/python3
"""
This module provides a function to lookup attributes and methods.
"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list object containing the names of attributes and methods.
    """
    return dir(obj)
