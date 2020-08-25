#!/usr/bin/python3
"""0x111 - 6"""
import requests
import sys


if __name__ == '__main__':
    dats = {'email': str(sys.argv[2])}
    getit = requests.get(sys.argv[1], data=dats)
    print(getit.text)
