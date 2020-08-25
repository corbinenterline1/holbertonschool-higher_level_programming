#!/usr/bin/python3
"""0x11 - 7"""
import requests
import sys


if __name__ == "__main__":
    try:
        response = requests.get(sys.argv[1])
        response.raise_for_status()
        response.encoding = 'utf-8'
        print(response.text)
    except:
        print("Error code: {}".format(response.status_code))
