#!/usr/bin/python3
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'
req = urllib.request.Request(url)

with urllib.request.urlopen(req) as response:
    data = response.read()
    print("Body response:")
    print("\t- type:", type(data))
    print("\t- content:", data)
    print("\t- utf8 content:", data.decode('utf-8'))

