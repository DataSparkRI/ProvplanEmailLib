import os
import smtplib
from email.mime.text import MIMEText
import ConfigParser


class Emailer(object):

    def __init__(self):
        self.config = ConfigParser.ConfigParser()
        self.config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))
        self.smtp_server = self.config.get('settings', 'smtp_server')
        self.smtp_port = self.config.get('settings', 'smtp_port')
        self.smtp_user = self.config.get('settings', 'smtp_user')
        self.smtp_password = self.config.get('settings', 'smtp_password')
        self.from_address = self.config.get('settings', 'from_address')
        self.to_addresses = self.config.get('settings', 'to_addresses')
        self.subject = self.config.get('settings', 'subject')
        self.body = self.config.get('settings', 'body')
        self.connection = self.smtp_connect()

    def smtp_connect(self):
        try:
            smtp_connection = smtplib.SMTP(self.smtp_server, self.smtp_port)
        except smtplib.SMTPException, exception:
            print exception
        try:
            smtp_connection.login(self.smtp_user, self.smtp_password)
        except smtplib.SMTPException, exception:
            print exception
        return smtp_connection

    def construct_msg(self, from_address=None, to_addresses=None, subject=None, body=None):
        """ Constuct Message, any of these fields override whats in config.ini """
        if body:
            message = MIMEText(body)
        else:
            message = MIMEText(self.body)
        if from_address:
            message['From'] = from_address
        else:
            message['From'] = self.from_address
        if to_addresses:
            message['To'] = to_addresses
        else:
            message['To'] = self.to_addresses
        if subject:
            message['Subject'] = subject
        else:
            message['Subject'] = self.subject

        self.message = message.as_string()

        return message.as_string()

    def send_email(self, from_address=None, to_addresses=None, subject=None, body=None):
        message = self.construct_msg(from_address, to_addresses, subject, body)
        try:
            self.connection.sendmail(self.from_address, self.to_addresses, message)
        except smtplib.SMTPException, exception:
            print exception

    def disconnect(self):
        self.connection.quit()
