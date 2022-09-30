#!/usr/bin/python3

"""
This module contains a function that
appends command line arguments to a file
"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


file_name = "add_item.json"

if __name__ == "__main__":
    try:
        args_list = load_from_json_file(file_name)
    except FileNotFoundError:
        args_list = []
    for i, args in enumerate(sys.argv):
        if i > 0:
            args_list.append(args)
    save_to_json_file(args_list, file_name)
