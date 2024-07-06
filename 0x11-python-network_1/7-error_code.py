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
    reponse = requests.get(url)
    # Check if the HTTP status code is greater than or equal to 400
    if reponse.status_code >= 400:
        print("Error code: {}".format(reponse.status_code))
    else:
        # Display the body of the response
        print(rep.content.decode("utf-8"))
