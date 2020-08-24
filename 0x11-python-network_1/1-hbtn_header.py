#!/usr/bin/python3
"""0x11 - 1"""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        hr = response.getheader('X-Request-Id')
        print(hr)
