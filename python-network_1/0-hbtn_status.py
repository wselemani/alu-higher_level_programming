#!/usr/bin/python3
"""
This module fetches the status from the Holberton/ALX intranet URL
using the urllib package and prints the formatted body response.
"""
import urllib.request


if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))
