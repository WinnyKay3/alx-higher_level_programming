#!/bin/bash
# takes in url and sends a request to it.
curl -s "$1" | wc -c
