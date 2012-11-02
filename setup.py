try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

    config = {
        'description': '',
        'author': 'Jesse Ellis',
        'url': 'https://github.com/ProvidencePlan/provplan-email-lib',
        'download_url': 'https://github.com/ProvidencePlan/provplan-email-lib/zipball/master',
        'author_email': 'jellis@provplan.org',
        'version': '0.1.0',
        'name': 'provplan_email)_lib'
        }

    setup(**config)
