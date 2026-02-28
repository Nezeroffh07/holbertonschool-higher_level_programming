#!/usr/bin/env python3
"""
This module defines an abstract class Animal and its subclasses.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class representing an animal."""

    @abstractmethod
    def sound(self):
        """Abstract method to return the animal's sound."""
        pass


class Dog(Animal):
    """Class representing a dog, inherited from Animal."""

    def sound(self):
        """Returns the sound of the dog."""
        return "Bark"


class Cat(Animal):
    """Class representing a cat, inherited from Animal."""

    def sound(self):
        """Returns the sound of the cat."""
        return "Meow"
