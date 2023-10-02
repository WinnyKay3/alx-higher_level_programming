#!/usr/bin/python3
''' use of requests module to fetch'''

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)

    #checking http status code error
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
