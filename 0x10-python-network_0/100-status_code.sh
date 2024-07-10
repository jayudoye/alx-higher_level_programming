#!/bin/bash
# Send request to the URL and display only the status code
curl -s -o /dev/null -w "%{http_code}" "$1"
