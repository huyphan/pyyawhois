# -*- coding: utf-8 -*-

"""
This module provides a Client object to handle whois queries.

"""

from .server import Server

class Client(object):

    DEFAULT_TIMEOUT = 10

    def __init__(self, settings = {}):
        self.settings = settings

    def lookup(self, domain):
        server = Server.guess(domain)
        server.configure(self.settings)
        return server.lookup(domain)