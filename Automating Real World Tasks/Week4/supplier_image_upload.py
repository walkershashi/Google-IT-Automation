#!/usr/bin/env python3

import requests
import glob
import os

URL = "http://localhost/upload/"

for file in glob.glob("supplier-data/images/0*"):
    print(file)
    with open(file, 'rb') as upload_file:
        print(upload_file)
        post = requests.post(URL, files = {'file': upload_file})