"""
Automate the Boring Stuff with Python
Chapter 20 Notes
"""

# SMTP

"""
SMTP sends emails.
Python module:
smtplib
"""

import smtplib

smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)

smtp_obj.starttls()

# smtp_obj.login('youremail@gmail.com', 'password')

smtp_obj.quit()


# SMTP Servers

"""
Gmail:
smtp.gmail.com

Outlook:
smtp.office365.com

Yahoo:
smtp.mail.yahoo.com
"""


# Sending Emails

"""
sendmail(from, to, message)
"""

message = """Subject: Hello

This is the email body.
"""

# smtp_obj.sendmail(
#     'from@gmail.com',
#     'to@gmail.com',
#     message
# )


# IMAP

"""
IMAP reads emails.

Libraries:
imapclient
pyzmail
"""

# pip install imapclient
# pip install pyzmail36


# Connecting to IMAP

# import imapclient

# imap_obj = imapclient.IMAPClient(
#     'imap.gmail.com',
#     ssl=True
# )

# imap_obj.login(
#     'email@gmail.com',
#     'password'
# )


# Inbox

# imap_obj.select_folder(
#     'INBOX',
#     readonly=True
# )


# Searching Emails

# imap_obj.search(['ALL'])

# imap_obj.search(['UNSEEN'])

# imap_obj.search([
#     'FROM',
#     'example@gmail.com'
# ])

# imap_obj.search([
#     'SUBJECT',
#     'Python'
# ])


# Fetching Emails

# raw_messages = imap_obj.fetch(
#     UIDs,
#     ['BODY[]']
# )


# Reading Emails

# import pyzmail

# message = pyzmail.PyzMessage.factory(
#     raw_email
# )

# print(message.get_subject())

# print(message.get_addresses('from'))

# print(
#     message.text_part.get_payload().decode(
#         message.text_part.charset
#     )
# )


# Deleting Emails

# imap_obj.delete_messages(UIDs)

# imap_obj.expunge()


# Twilio SMS

"""
Twilio sends text messages.
"""

# pip install twilio

# from twilio.rest import Client

# client = Client(
#     account_sid,
#     auth_token
# )

# client.messages.create(
#     body='Hello',
#     from_='+123456789',
#     to='+987654321'
# )


# Pushbullet

"""
Pushbullet sends notifications.
"""

# pip install pushbullet.py

# from pushbullet import Pushbullet

# pb = Pushbullet("API_KEY")

# pb.push_note(
#     "Title",
#     "Message"
# )


# Security

"""
Use app passwords or .env files.
Do not hardcode passwords.
"""


# Common Errors

"""
AuthenticationError
= Wrong login

SSL Error
= Wrong port/settings
"""


# Key Terms

"""
SMTP = Send emails
IMAP = Read emails
TLS = Encryption
UID = Email ID
"""


# Mini Email Example

import smtplib

email = "your_email@gmail.com"

subject = "Python Email"

body = "Sent with Python."

message = f"Subject: {subject}\n\n{body}"

server = smtplib.SMTP(
    'smtp.gmail.com',
    587
)

server.starttls()

# server.login(email, password)

# server.sendmail(
#     email,
#     "friend@gmail.com",
#     message
# )

server.quit()

print("Done")
