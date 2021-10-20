import smtplib

from .app_config import EmailConfig

def send_email(email, subject, body):

    server = smtplib.SMTP(EmailConfig.SMTP_SERVER, EmailConfig.SMTP_PORT)
    server.starttls()
    server.login(EmailConfig.SENDER_ADDRESS, EmailConfig.PASSWORD)
    message = f'From: {EmailConfig.SENDER_NAME} <{EmailConfig.SENDER_ADDRESS}>\nTo: {email}\nSubject: {subject}\n\n{body}'
    server.sendmail(EmailConfig.SENDER_ADDRESS, [email], message)
    server.quit()
