import smtplib
import imaplib
import email


# 1. Sending Email with SMTP

smtp_obj = smtplib.SMTP('smtp.example.com', 587)
smtp_obj.ehlo()
smtp_obj.starttls()  # secure connection

smtp_obj.login('your_email@example.com', 'your_password')

smtp_obj.sendmail(
    'your_email@example.com',
    'recipient@example.com',
    'Subject: Hello\n\nThis is the email body.'
)

smtp_obj.quit()


# 2. Common SMTP Providers

"""
Gmail: smtp.gmail.com, port 587
Outlook: smtp.office365.com, port 587
Yahoo: smtp.mail.yahoo.com, port 587

Note: Many providers require app passwords or OAuth instead of plain passwords.
"""


# 3. Retrieving Email with IMAP

imap_obj = imaplib.IMAP4_SSL('imap.example.com')

imap_obj.login('your_email@example.com', 'your_password')

imap_obj.select('INBOX')

status, messages = imap_obj.search(None, 'ALL')

mail_ids = messages[0].split()


# 4. Fetching and Reading Emails

latest_email_id = mail_ids[-1]

status, data = imap_obj.fetch(latest_email_id, '(RFC822)')

raw_email = data[0][1]

parsed_email = email.message_from_bytes(raw_email)

subject = parsed_email['subject']
from_ = parsed_email['from']

body = parsed_email.get_payload()


# 5. Working with Email Content

for part in parsed_email.walk():
    content_type = part.get_content_type()

    if content_type == 'text/plain':
        body = part.get_payload(decode=True)


# 6. Deleting Emails

imap_obj.store(latest_email_id, '+FLAGS', '\\Deleted')
imap_obj.expunge()


# 7. Logging Out

imap_obj.logout()


# 8. Sending Attachments

from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = 'Report'
msg['From'] = 'your_email@example.com'
msg['To'] = 'recipient@example.com'

msg.set_content('Please find the attached file.')

with open('file.txt', 'rb') as f:
    file_data = f.read()
    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename='file.txt')

smtp_obj = smtplib.SMTP('smtp.example.com', 587)
smtp_obj.starttls()
smtp_obj.login('your_email@example.com', 'your_password')

smtp_obj.send_message(msg)
smtp_obj.quit()


# 9. Sending SMS Messages

"""
You can send SMS using email-to-SMS gateways provided by carriers.

Example:
number@carrier_gateway.com

Or use APIs like:
- Twilio
- Nexmo (Vonage)

These require account setup and API keys.
"""


# 10. Practical Example

def send_email(subject, body, to_email):
    smtp_obj = smtplib.SMTP('smtp.example.com', 587)
    smtp_obj.starttls()
    smtp_obj.login('your_email@example.com', 'your_password')

    message = f"Subject: {subject}\n\n{body}"

    smtp_obj.sendmail('your_email@example.com', to_email, message)
    smtp_obj.quit()
