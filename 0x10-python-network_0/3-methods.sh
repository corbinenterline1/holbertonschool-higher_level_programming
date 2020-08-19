#!/bin/bash
# Display all HTTP methods server will accept. Line manipulation BASH FUN
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
