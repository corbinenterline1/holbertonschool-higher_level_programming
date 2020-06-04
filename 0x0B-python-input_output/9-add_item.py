#!/usr/bin/python3
"""0x0B - 9 - Load, add, save"""
import sys


savejson = __import__('7-save_to_json_file').save_to_json_file
loadjson = __import__('8-load_from_json_file').load_from_json_file
try:
    nl = loadjson('add_item.json')
except:
    nl = []
for i in range(1, len(sys.argv)):
    nl.append(sys.argv[i])
savejson(nl, 'add_item.json')
