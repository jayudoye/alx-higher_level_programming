#!/usr/bin/python3
"""
A Python script that takes in a URL and an email, 
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""

from urllib.request import urlopen, Request
from sys import argv
from urllib.parse import urlencode

if __name__ == "__main__":
    url = argv[1]
    # Prepare the data to be sent in the POST request
    data = {"email": argv[2]}
    email = urlencode(data).encode("ascii")
    req = Request(url, email)

    # Send a POST request with the email parameter
    with urlopen(req) as response:
        # Read and display the body of the response (decoded in utf-8)
        body = response.read().decode('utf-8')
        print(body)
