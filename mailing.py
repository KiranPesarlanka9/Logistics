# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

SENDGRID_API_KEY = "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"

def send_mail(content, subject):
    message = Mail(
        from_email='dont-reply@mailing.com',
        to_emails='kiranpesarlanka9@gmail.com',
        subject=subject,
        html_content=content)
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)
