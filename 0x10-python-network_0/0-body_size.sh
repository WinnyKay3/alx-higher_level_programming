#!/bin/bash
# takes in url and sends a request
curl -sI "$1" | grep 'content-length' | awk '{print $2}'
