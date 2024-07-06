#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)
"""

from urllib.request import urlopen, Request
from urllib.parse import urlencode
from urllib.error import HTTPError
from sys import argv

if __name__ == "__main__":
    # Check if a URL is provided as a command-line argument
    url = argv[1]
    try:
        with urlopen(url) as response:
            # Read and display the body of the response (decoded in utf-8)
            body = response.read().decode("utf-8")
            print(body)
    except HTTPError as e:
        # Handle HTTPError exceptions and print the HTTP status code
        print("Error code: {}".format(e.code))
