#!/bin/bash
# takes in url and sends a request
curl -s "$1" | wc -c
