# from celery import shared_task
# from PaperSafeBank.celery import Celery
# from django.core import mail
# from django.template.loader import render_to_string
# import smtplib
# import sendgrid
# import os
# from sendgrid.helpers.mail import Mail, Email, To, Content



# @shared_task
# def send_email():
#     sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('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'))
#     from_email = Email("chparmar@bestpeers.com")  # Change to your verified sender
#     to_email = To("tsonare@bestpeers.com")  # Change to your recipient
#     subject = "Transaction successfully."
#     content = Content("text/plain", "and easy to do anywhere, even with Python")
#     mail = Mail(from_email, to_email, subject, content)

#     # Get a JSON-ready representation of the Mail object
#     mail_json = mail.get()

#     # Send an HTTP POST request to /mail/send
#     response = sg.client.mail.send.post(request_body=mail_json)
#     # to_email = 'me@example.com'
#     # subject = 'Testing Celery/redis'
#     # from_email = 'me2@example.com'
#     # message = 'This is a test of my Celery/function.'
#     # recipient_list = []
#     # recipient_list.append(to_email)
#     # html_message = render_to_string('send_mail.html', {'message': message})
#     # try:
#     #     mail.send_mail(subject, message, from_email, recipient_list, html_message)
#     # except smtplib.SMTPException:
#     #     return 0
#     # return mail

