#!/bin/bash
# takes url sends a POST req to passed url and displays the body of respns
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
