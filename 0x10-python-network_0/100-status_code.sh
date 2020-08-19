#!/bin/bash
# the problems were my fault, damn it
curl -o /dev/null -s -w "%{http_code}" "$1"
