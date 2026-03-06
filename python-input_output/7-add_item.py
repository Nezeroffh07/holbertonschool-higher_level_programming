#!/usr/bin/python3
"""
This script adds all command-line arguments to a Python list,
and then saves them to a file named add_item.json.
"""
import sys


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    filename = "add_item.json"

    # Faylın mövcud olub-olmadığını yoxlayırıq
    try:
        my_list = load_from_json_file(filename)
    except FileNotFoundError:
        # Fayl yoxdursa, boş bir siyahı yaradırıq
        my_list = []

    # Terminaldan gələn yeni arqumentləri siyahıya əlavə edirik
    # sys.argv[1:] skriptin öz adını (sys.argv[0]) nəzərə almamaq üçündür
    my_list.extend(sys.argv[1:])

    # Yenilənmiş siyahını təkrar fayla JSON formatında yazırıq
    save_to_json_file(my_list, filename)
