
#!/usr/bin/env python3

import os
import requests

txt_file = os.listdir("/data/feedback")

feedback = {}

for file in txt_file:
    with open("/data/feedback/" + file) as f:
        lines = f.readlines()
        feedback['title'] = lines[0]
        feedback['name'] = lines[1]
        feedback['date'] = lines[2]
        feedback['feedback'] = lines[3]

        response = requests.post("http://<corpweb-external-IP>/feedback", data = feedback)
