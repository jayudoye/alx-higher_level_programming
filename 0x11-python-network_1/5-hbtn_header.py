#!/usr/bin/python3
"""This script takes in a URL, sends a request to the
URL and displays the value of the variable
X-Request-Id in the response header"""
import requests
import sys

# Check if a URL is provided as a command-line argument
if len(sys.argv) != 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    response = requests.get(url)

    print(response.headers.get('X-Request-Id'))

except requests.RequestException as e:
    print(f"Error accessing the URL: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
