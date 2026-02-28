#!/usr/bin/env python3
"""
This module defines a CountedIterator class that keeps track
of the number of items iterated over.
"""


class CountedIterator:
    """Custom iterator that counts the number of fetched items."""

    def __init__(self, some_iterable):
        """Initialize the iterator object and the counter."""
        self.iterator = iter(some_iterable)
        self.counter = 0

    def get_count(self):
        """Return the current count of iterated items."""
        return self.counter

    def __next__(self):
        """
        Return the next item from the iterator and increment the count.
        Raises StopIteration when no more items are available.
        """
        # Original iteratordan növbəti elementi alırıq.
        # Əgər element bitibsə, bu sətir avtomatik StopIteration verəcək.
        item = next(self.iterator)
        
        # Element uğurla alındısa, sayğacı 1 artırırıq.
        self.counter += 1
        
        return item
