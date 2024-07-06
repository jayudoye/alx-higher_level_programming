#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""

import requests

url = "https://alx-intranet.hbtn.io/status"

if __name__ == "__main__":
    reponse = requests.get(url)
    
    # Displaying the body of the response with tabulation before each line
    print("Body response:")
    print("\t- type: {}".format(type(rep.text)))
    print("\t- content: {}".format(rep.text))
