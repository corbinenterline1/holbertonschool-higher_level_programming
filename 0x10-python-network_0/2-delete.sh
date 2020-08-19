#!/bin/bash
# DELETE request to URL passed as first arg, display body of response
curl -sX DELETE "$1"
