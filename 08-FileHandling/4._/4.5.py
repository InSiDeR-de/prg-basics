#The file email.txt contains a raw email. Write a program that uses regular expressions to fetch and print:
#sender email address
#recipient email address
#email subject
#email body
with open('email.txt') as file:
    content = file.read()  
import re
senderemail = re.search(r'From: (.+)', content)
recipient = re.search(r'To: (.+)', content) 
subject = re.search(r'Subject: (.+)', content)
body = re.search(r'\n\n(.+)', content, re.DOTALL)
if senderemail:
    print(f'Sender: {senderemail.group(1)}')
if recipient:
    print(f'Recipient: {recipient.group(1)}')
if subject:
    print(f'Subject: {subject.group(1)}')
if body:
    print(f'Body: {body.group(1).strip()}')

