#!/bin/bash
# req to url passed as arg and displays only status code of respons
curl -s -o /dev/null -w "%{http_code}" "$1"
