#!/bin/bash
# fucked up all my uploads yesterday
curl -s -H "Content-Type: application/json" "$1" -d @"$2"
