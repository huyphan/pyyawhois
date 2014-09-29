# -*- coding: utf-8 -*-

"""
This module provides a Client object to handle whois queries.

"""

from .server import Server

DEFAULT_TIMEOUT = 10

class Client(object):

    def __init__(self, settings = {}):

        if settings.has_key('timeout'):
            self.timeout = settings.pop('timeout')
        else:
            self.timeout = DEFAULT_TIMEOUT

        self.settings = settings

    def lookup(self, domain):
        server = Server.guess(domain)
        server.configure(self.settings)
        return server.lookup(domain)