#!/bin/bash
# sends JSON POST req to given url with given json file
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
