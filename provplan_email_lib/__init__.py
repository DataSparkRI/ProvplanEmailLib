import os
import smtplib
from email.mime.text import MIMEText
import ConfigParser


class Emailer(object):

    def __init__(self, config_file=None, smtp_server=None, smtp_port=None, smtp_user=None, smtp_password=None):

        if config_file:
            self.config = ConfigParser.ConfigParser()
            self.config.read(config_file)
            self.smtp_server = self.config.get('settings', 'smtp_server')
            self.smtp_port = self.config.get('settings', 'smtp_port')
            self.smtp_user = self.config.get('settings', 'smtp_user')
            self.smtp_password = self.config.get('settings', 'smtp_password')
        else:
            if smtp_server:
                self.smtp_server = smtp_server
            else:
                raise ValueError('smtp_server is required')
            if smtp_port:
                self.smtp_port = smtp_port
            else:
                raise ValueError('smtp_port is required')
            if smtp_user:
                self.smtp_user = smtp_user
            else:
                raise ValueError('smtp_user is required')
            if smtp_password:
                self.smtp_password= smtp_password
            else:
                raise ValueError('smtp_password is required')

        self.connection = self.smtp_connect()

    def smtp_connect(self):
        try:
            smtp_connection = smtplib.SMTP(self.smtp_server, self.smtp_port)
            smtp_connection.ehlo()
            smtp_connection.starttls()
            smtp_connection.ehlo()
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
            self.connection.sendmail(from_address, to_addresses, message)
        except smtplib.SMTPException, exception:
            print exception

    def disconnect(self):
        self.connection.quit()
