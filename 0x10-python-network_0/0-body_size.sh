#!/bin/bash
# curl body size

response=$(curl -sI "$1")
size=$(echo "$response" | grep -i Content-Length | awk '{print $2}' | tr -d '\r')
echo "$size"
