#!/usr/bin/env python3
"""
This module demonstrates the use of Mixins to add modular
functionalities to classes without complex inheritance.
"""


class SwimMixin:
    """A mixin class that provides swimming behavior."""

    def swim(self):
        """Prints the swimming action."""
        print("The creature swims!")


class FlyMixin:
    """A mixin class that provides flying behavior."""

    def fly(self):
        """Prints the flying action."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A class representing a Dragon that inherits behaviors from
    both SwimMixin and FlyMixin.
    """

    def roar(self):
        """Prints the roaring action of the dragon."""
        print("The dragon roars!")
