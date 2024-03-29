#!/usr/bin/python3
"""
script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of the
response (decoded in utf-8)
"""
from sys import argv
from urllib import request, parse


if __name__ == '__main__':
    if len(argv) > 2:
        emaildata = parse.urlencode({'email': argv[2]}).encode('ascii')
        requs = request.Request(argv[1], emaildata)
        with request.urlopen(requs) as response:
            html = response.read()
            print(html.decode('utf-8'))
