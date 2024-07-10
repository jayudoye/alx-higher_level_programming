#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request to the URL
and displays the body of the response
"""

import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    # Send a request to the URL
    response = requests.get(url)
    # Check if the HTTP status code is greater than or equal to 400
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        # Display the body of the response
        print(response.content.decode("utf-8"))
