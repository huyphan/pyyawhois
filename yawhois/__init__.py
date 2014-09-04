# -*- coding: utf-8 -*-

"""
Yet Another Python Whois Library
~~~~~~~~~~~~~~~~~~~~~

pyyawhois is a python port of Ruby's whois module.

:copyright: (c) 2014 by Huy Phan.
:license: MIT, see LICENSE for more details.

"""

__title__     = 'pyyawhois'
__version__   = '1.0'
__build__     = 1
__author__    = 'Huy Phan <dachuy@gmail.com>'
__license__   = 'MIT'
__copyright__ = 'Copyright 2014 Huy Phan'

from .client import Client
from .api import lookup