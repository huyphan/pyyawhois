# -*- coding: utf-8 -*-

"""
The Server class has two important roles:
1. it acts as a database for the WHOIS server definitions
2. it is responsible for selecting the right adapter used to handle the query to the WHOIS server(s).
"""

import re
import glob
import os
import json
from .utils import *
from .exceptions import *
import adapters

class Server(object):

    # The WHOIS server definitions.
    _definitions = {}

    def __init__(self):
        pass

    @staticmethod
    def guess(string):
        # Top Level Domain match
        if matches_tld(string):
            return Server.factory('tld', ".", "whois.iana.org")

        # IP address (secure match)
        if matches_ip(string):
            return Server.find_for_ip(string)

        # Email Address (secure match)
        if matches_email(string):
            return Server.find_for_email(string)

        # Domain Name match
        server = Server.find_for_domain(string)
        if server:
            return server

        # ASN match
        if matches_asn(string):
            return Server.find_for_asn(string)

        # Game Over
        raise ServerNotFound("Unable to find a WHOIS server for '%s'" % string)

    @staticmethod
    def find_for_domain(domain):
        for definition in Server._definitions['tld']:
            if re.compile(re.escape(definition[0])+"$").search(domain):
                return Server.factory('tld', *definition)
        return None        

    @staticmethod
    def load_definitions():
        data_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../data")
        for f in glob.glob(data_path+"/*.json"):
            Server.load_json(f)

    @staticmethod
    def load_json(file_path):
        def_type = os.path.splitext(os.path.basename(file_path))[0]
        for allocation, settings in json.loads(open(file_path, "r").read()).items():
            Server.define(def_type, allocation, settings.get("host"), settings)

    @staticmethod    
    def define(def_type, allocation, host, options = {}):
        if not Server._definitions.has_key(def_type):
            Server._definitions[def_type] = []
        Server._definitions[def_type].append((allocation, host, options))

    @staticmethod
    def factory(def_type, allocation, host, options = {}):
        adapter = options.get('adapter') or adapters.Standard
        if not callable(adapter):
            adapter = adapters.const_get(camelize(adapter))
        return adapter(def_type, allocation, host, options)

Server.load_definitions()