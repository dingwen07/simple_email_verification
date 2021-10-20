
import json
import os, sys
from smtplib import SMTP


class HomeConfig:
    with open("./email_verification/app/app_config.json", 'r') as config_file:
        config = json.load(config_file)['home_config']
        CONTEXT = config['context']

class EmailConfig:
    with open("./email_verification/app/app_config.json", 'r') as config_file:
        config = json.load(config_file)['email_config']
        SENDER_ADDRESS = config['sender_address']
        SENDER_NAME = config['sender_name']
        SMTP_SERVER = config['smtp_server']
        SMTP_PORT = config['smtp_port']
        PASSWORD = config['password']
