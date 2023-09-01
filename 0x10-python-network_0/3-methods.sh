#!/bin/bash
# displays all HTTP methods the server accepts
culr -Is "$1" | grep Allow | cut -c 8-
