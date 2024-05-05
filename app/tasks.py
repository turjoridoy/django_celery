import smtplib

from celery import shared_task
from time import sleep
from django.conf import settings
from email.mime.text import MIMEText


@shared_task
def send_email(email_address):
    print("send email called")
    sleep(5)
    print(f"hi there I am sending email {email_address}")
    me = settings.EMAIL_USERNAME
    password = settings.EMAIL_PASSWORD
    you = email_address

    email_body = """
        <html>
            <body>
                <p>Hello World!</p>
            </body>
        </html>
    """

    message = MIMEText(email_body, 'html')
    message['Subject'] = 'New mail!'
    message['From'] = me
    message['To'] = you

    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(me, password)
        server.sendmail(me, you, message.as_string())
        server.quit()

    except Exception as e:
        print(f'Error in sending email: {e}')
