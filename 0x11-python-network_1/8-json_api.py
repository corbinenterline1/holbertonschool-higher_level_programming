#!/usr/bin/python3
"""0x11 - 8"""
import requests
import sys

if __name__ == "__main__":
    try:
        q = sys.argv[1]
    except:
        q = ""
    response = requests.post("http://0.0.0.0:5000/search_user", data={'q': q})
    jasponse = {}
    try:
        jaspons = response.json()
        if len(jaspons) > 0:
            print("[{:d}] {}".format(jaspons.get("id"), jaspons.get("name")))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
