#!/usr/bin/python3
"""Module for add_integer method."""


def add_integer(a, b=98):
    """
    Adds 2 integers.
    a and b must be integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # NaN və ya Infinity (Overflow) yoxlaması
    # Python-da NaN öz-özünə bərabər olmayan tək dəyərdir (a != a)
    if a != a or a == float('inf') or a == float('-inf'):
        raise TypeError("a must be an integer")
    if b != b or b == float('inf') or b == float('-inf'):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
