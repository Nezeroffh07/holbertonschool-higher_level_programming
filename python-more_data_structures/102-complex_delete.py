#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """Deletes keys with a specific value in a dictionary."""
    # Lüğət üzərində gəzərkən onu dəyişdirmək xəta verir.
    # Ona görə də əvvəlcə açarların surətini (list kimi) götürürük.
    for key in list(a_dictionary.keys()):
        if a_dictionary[key] == value:
            del a_dictionary[key]
    return a_dictionary
