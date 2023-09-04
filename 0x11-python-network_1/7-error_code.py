#!/usr/bin/python3
"""Sends a request to a given url and displays the response body."""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    k = requests.get(url)
    if k.status_code >= 400:
        print("Error code: {}".format(k.status_code))
    else:
        print(k.text)
