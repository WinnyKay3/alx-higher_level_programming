#!/bin/bash
# deletes req passed as first arg and displays body of respns
curl -sX DELETE "$1"
