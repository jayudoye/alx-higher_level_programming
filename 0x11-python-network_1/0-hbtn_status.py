#!/usr/bin/python3
"""A script that fetches https://alx-intranet.hbtn.io/status using urllib """
import urllib.request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

try:
    with urllib.request.urlopen(url) as response:
        # Reading the response body
        content = response.read()
        utf8_content = content.decode('utf-8')

        # Displaying information about the response
        print("Body response:")
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")
        print(f"\t- utf8 content: {utf8_content}")

except urllib.error.URLError as e:
    print(f"Error accessing the URL: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
