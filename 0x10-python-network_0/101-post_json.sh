#!/bin/bash
# zimegwantana
curl -sH "Content-Type: application/json" -d @"$2" -X POST "$1"
