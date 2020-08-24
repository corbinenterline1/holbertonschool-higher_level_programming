#!/usr/bin/python3
"""0x11 - 0"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print('Body response:')
        tp = type(response.read())
        print('\t- type {}'.format(tp))
        print('\t- content: {}'.format(html))
        dc = html.decode(encoding='UTF-8')
        print('\t- utf8 content: {}'.format(dc))
