#!/bin/bash
# Send GET request with header variable X-HolbertonSchool-User-ID, val. 98
CURL -sX GET -H 'X-HolbertonSchool-User-Id: 98' "$1"
