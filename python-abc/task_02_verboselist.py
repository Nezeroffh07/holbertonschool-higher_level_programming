#!/usr/bin/env python3
"""
This module defines a VerboseList class that extends the built-in list
class to print notifications upon modifications.
"""


class VerboseList(list):
    """A custom list class that prints notifications when modified."""

    def append(self, item):
        """Add an item to the end of the list and print a notification."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, item_list):
        """Extend the list with multiple items and print a notification."""
        super().extend(item_list)
        print("Extended the list with [{}] items.".format(len(item_list)))

    def remove(self, item):
        """Remove an item from the list and print a notification."""
        if item in self:
            print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Pop an item from the list and print a notification."""
        # Əgər indeks səhvdirsə, self[index] avtomatik IndexError verəcək
        # və yalandan print çap olunmayacaq.
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
