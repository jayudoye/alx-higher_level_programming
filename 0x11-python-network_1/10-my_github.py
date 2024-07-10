#!/usr/bin/python3
"""This script takes your GitHub credentials
(username and password) and uses the GitHub API
to display your id"""
from requests.auth import HTTPBasicAuth
import requests
import sys

if __name__ == "__main__":
    url = "https://api.github.com/user"
    response = requests.get(url, auth=HTTPBasicAuth(sys.argv[1], sys.argv[2]))
    print(response.json().get('id'))
