#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    """Prints an integer and returns True, or False and prints to stderr."""
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        sys.stderr.write("Exception: {}\n".format(e))
        return False
