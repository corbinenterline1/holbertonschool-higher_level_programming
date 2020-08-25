#!/usr/bin/python3
"""0x11 - 10"""
from requests.models import HTTPBasicAuth
import requests
import sys


if __name__ == "__main__":
    respy = requests.get("https://api.github.com/user", auth=HTTPBasicAuth(
        sys.argv[1], sys.argv[2]))
    iddy = respy.json().get("id")
    print(iddy)
