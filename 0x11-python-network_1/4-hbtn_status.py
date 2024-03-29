#!/usr/bin/python3
"""
script that fetches https://alx-intranet.hbtn.io/status
"""
import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    text = requests.get(url).text
    page = 'Body response:\n\t- type: {}\n\t- content: {}'
    print(page.format(type(text), text))
