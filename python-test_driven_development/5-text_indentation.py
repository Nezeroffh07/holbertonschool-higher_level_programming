#!/usr/bin/python3
"""Module for text_indentation method."""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?' and ':'.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    skip_space = True
    for char in text:
        # Əgər əvvəlki simvol durğu işarəsi olubsa, boşluqları keçirik
        if skip_space and char == ' ':
            continue
        
        skip_space = False
        print(char, end="")
        
        # Durğu işarəsini tapdıqda yeni sətirləri əlavə edirik və bayrağı qaldırırıq
        if char in ".?:":
            print("\n\n", end="")
            skip_space = True
