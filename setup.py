try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Yet another Python Whois module',
    'author': 'Huy Phan',
    'url': 'http://github.com/huyphan/pyyawhois',
    'author_email': 'dachuy@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['pyyawhois'],
    'scripts': [],
    'name': 'pyyawhois'
}

setup(**config)
