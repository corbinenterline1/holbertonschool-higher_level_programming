#!/usr/bin/python3
"""0x11 - 2"""
import urllib.request
import sys


if __name__ == "__main__":
    datas = bytes(urllib.parse.urlencode(
        {"email": sys.argv[2]}).encode('utf-8'))
    with urllib.request.urlopen(sys.argv[1], data=datas) as response:
        stf = response.read().decode('utf-8')
        print(stf)
