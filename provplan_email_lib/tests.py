"""
Run tests like so:
    python -m unittest discover
Make sure its from the main module directory!
SEE: http://docs.python.org/library/unittest.html#test-discovery
"""
from unittest import TestCase, main
from provplan_email_lib import *
import ConfigParser
class TestSend(TestCase):

    def test_sends_email(self):
        e = Emailer(config_file='/tmp/config.ini')
        e.send_email(to_addresses='amedrano@provplan.org',subject='Tesing out the code.', body='Unit test!',from_address='thatdude@testcase.org') # this will just send whatever is in config
        e.disconnect()

    def test_sends_email_no_config(self):
        # read config so that we can pass it the settings.
        config = ConfigParser.ConfigParser()
        config.read('/tmp/config.ini')
        smtp_server = config.get('settings', 'smtp_server')
        smtp_port = config.get('settings', 'smtp_port')
        smtp_user = config.get('settings', 'smtp_user')
        smtp_password = config.get('settings', 'smtp_password')

        e = Emailer(None, smtp_server, smtp_port, smtp_user, smtp_password)
        e.send_email(to_addresses='amedrano@provplan.org',subject='Tesing out the code. No config', body='Unit test!',from_address='thatdude@testcase.org') # this will just send whatever is in config
        e.disconnect()

if __name__ == '__main__':
    main()
