#!/usr/bin/python3
"""0x111 - 5"""
import requests
import sys


if __name__ == "__main__":
    try:
        getit = requests.get(sys.argv[1])
        print(getit.headers['X-Request-Id'])
    except:
        pass
