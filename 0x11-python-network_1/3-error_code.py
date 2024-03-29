#!/usr/bin/python3
"""
script that takes in a URL, sends a request and displays
the value of the X-Request-Id variable found in the header
(handling HTTP errors)
"""
from urllib import request, error
import sys


if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as response:
            html = response.read()
            print(html.decode('utf-8'))
            except error.HTTPError as exce:
                print('Error code: {}'.format(exce.code))
