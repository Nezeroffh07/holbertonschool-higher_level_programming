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

    # NaN və ya Sonsuzluq (Overflow) yoxlaması
    if a != a or abs(a) > 1.7976931348623157e+308:
        raise TypeError("a must be an integer")
    if b != b or abs(b) > 1.7976931348623157e+308:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
