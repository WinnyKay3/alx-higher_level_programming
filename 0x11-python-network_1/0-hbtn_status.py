#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status."""
from urllib import request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(response_body)))
        print("\t- content: {}".format(response_body))
        print("\t- utf8 content: {}".format(response_body.decode("utf-8")))
