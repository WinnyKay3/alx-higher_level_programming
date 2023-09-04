#!/usr/bin/python3
'''Fetches https:intranet.hbtn.io/status'''
import requests

if __name__ == "__main__":
    k = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(k.text)))
    print("\t- content: {}".format(k.text))

