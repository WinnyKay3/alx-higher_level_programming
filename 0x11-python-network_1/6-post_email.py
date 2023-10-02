#!/usr/bin/python3
''' use of requests module to fetch'''

import sys
import requests

if __name__ == "__main__":
    # get url from command line
    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}

    response = requests.post(url, data=data)
    print(response.text)
