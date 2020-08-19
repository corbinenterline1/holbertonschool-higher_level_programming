#!/bin/bash
# curl request, then display size of body in bytes
curl -s "$1" | wc -c
