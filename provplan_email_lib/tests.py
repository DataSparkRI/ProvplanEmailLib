"""
Run tests like so:
    python -m unittest discover
Make sure its from the main module directory!
SEE: http://docs.python.org/library/unittest.html#test-discovery
"""
from unittest import TestCase, main
from provplan_email_lib import *

class TestSend(TestCase):
    """ makes assumption that you have a config.ini in the proper directory with proper credentials"""
    e = Emailer()
    e.send_email() # this will just send whatever is in config
    e.disconnect()


if __name__ == '__main__':
    main()
