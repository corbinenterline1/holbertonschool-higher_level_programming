#!/usr/bin/python3
"""0x11 - 4"""
import requests


if __name__ == "__main__":
        getit = requests.get('https://intranet.hbtn.io/status').text
        print('Body response:')
        print('\t- type: {}'.format(type(getit)))
        print('\t- content: {}'.format(getit))
