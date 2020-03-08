# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

SENDGRID_API_KEY = "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"

def send_mail(content, subject, to):
    message = Mail(
        from_email='dont-reply@mailing.com',
        to_emails=to,
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

