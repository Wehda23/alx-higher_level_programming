#!/usr/bin/python3


"""
COOL SCRIPT YOU GOTA TRY IT OUT
"""


import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

# First check if file is existing
try:
    items = load_from_json_file("add_item.json")
except Exception as e:
    items = []


if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        items.append(arg)

save_to_json_file(items, "add_item.json")
