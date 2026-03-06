#!/usr/bin/python3
"""
This module defines a Student class with serialization and deserialization.
"""


class Student:
    """A class that defines a student."""

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        If attrs is a list of strings, only those attributes are retrieved.
        Otherwise, all attributes are retrieved.
        """
        if type(attrs) is list and all(type(x) is str for x in attrs):
            return {k: self.__dict__[k] for k in attrs if k in self.__dict__}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.

        Args:
            json (dict): A dictionary containing the new attributes.
        """
        for key, value in json.items():
            setattr(self, key, value)
