#!/bin/bash
# Send JSON POST request with file contents in the body and display the response body
curl -s -X POST -H "Content-Type: application/json" -d "@$2" "$1"
