#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URl"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    k = requests.get(url)
    print(k.headers.get("X-Request-Id"))
