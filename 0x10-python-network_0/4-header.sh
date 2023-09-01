#!/bin/bash
# takes in url as arg,sends a GET req to the url, en displays body of respons
curl -sH "X-School-User-Id: 98" "$1"
