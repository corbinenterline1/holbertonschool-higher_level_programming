#!/usr/bin/python3
"""0x11 - 3"""
import urllib.request
import sys


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            pg = response.read().decode('utf-8')
            print(pg)
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.code))
