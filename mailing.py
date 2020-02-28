# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

SENDGRID_API_KEY = ""

content = "Is it inconvenient when your emails of password reset or email address confirmations cannot go to your users because it went to their Spam folder? How to ensure that your users can see it without opening Spam folder? Have you ever heard about transactional email services? It is the excellent solution for these cases. Let’s dig in and find out which service is the best."
message = Mail(
    from_email='dont-reply@mailing.com',
    to_emails='kiranpesarlanka9@gmail.com',
    subject='Test Mailing Service',
    html_content=content)
try:
    sg = SendGridAPIClient(SENDGRID_API_KEY)
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)
