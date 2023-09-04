#!/usr/bin/python3
'''Script that takes url and sends req to the url and displays value 
of variable X-request-id in response header'''

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    k = requests.get(url)
    print(k.headers.get("X-Request-Id"))
