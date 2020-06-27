#!/usr/bin/env python3

import os
import requests

URL = "http://35.226.232.234/fruits"
description_files = os.listdir("supplier-data/descriptions")
image_names = os.listdir("supplier-data/images/")
image_index = 0

for file in description_files:
    description = {}

    with open("supplier-data/descriptions/" + file, 'r') as des_file:
        lines = des_file.readlines()
        description['name'] = lines[0]
        description['weight'] = int(lines[1][:-4])
        description['description'] = lines[2]
        description['image_name'] = image_names[image_index]
        image_index += 1

    response = requests.post(URL, data = description)
