#!/usr/bin/python3
"""
This module defines a MyInt class that inherits from int.
"""


class MyInt(int):
    """A rebel integer class where == and != are inverted."""

    def __eq__(self, other):
        """
        Inverts the == operator.
        Returns the real != result from the parent class.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the != operator.
        Returns the real == result from the parent class.
        """
        return super().__eq__(other)
