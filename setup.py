try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'description': '',
        'author': 'Jesse Ellis',
        'url': 'https://github.com/ProvidencePlan/ProvplanEmailLib',
        'download_url': 'https://github.com/ProvidencePlan/ProvplanEmailLib/zipball/master',
        'install_requires': [],
        'packages': ['provplan_email_lib'],
        'author_email': 'jellis@provplan.org',
        'version': '0.1.0',
        'name': 'provplan_email_lib'
}

setup(**config)
