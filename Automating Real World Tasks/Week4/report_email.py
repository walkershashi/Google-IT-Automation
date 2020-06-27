#!/usr/bin/env python3

import os 
import reports
import emails

def generate_paragraph():
    description_files = os.listdir('supplier-data/description')

    descriptions = []
    for file in description_files:
        with open("supplier-data/description/" + file, 'r') as description_file:
            description = description_file.readlines()
            descriptions.append(["name: {}".format(description[0]), "weight: {}".format(description[1])])

    paragraph = ""
    for detail in descriptions:
        paragraph += detail[0] + "<br/>" + detail[1] + "<br/><br/>"
    print(paragraph)
    return paragraph

if __name__ == "__main__":
    attachment = "processed.pdf"
    title = "Processed Update on 26-06-2020"
    paragraph = generate_paragraph()
    
    reports.generate_report(attachment, title, paragraph)

    sender = 'automation@example.com'
    receiver = 'username@example.com'
    subject = 'Upload Completed - Online Fruit Store'
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    attachment_path = 'processed.pdf'

    message = emails.generate_email(sender, receiver, subject, body, attachment_path)
    emails.send_email(message)