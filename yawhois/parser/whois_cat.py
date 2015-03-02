from .base import ParserBase
from ..utils import array_wrapper
from ..record import Nameserver
from dateutil import parser as time_parser
import re

class WhoisCatParser(ParserBase):

    @property
    def status(self):
        match = re.search("Status:\s+(.+?)\n", self.content_for_scanner)
        if match:
            return array_wrapper(match.group(1).split(", "))

    @property
    def available(self):
        return bool(re.search("Object (.*?) NOT FOUND", self.content_for_scanner))

    @property
    def registered(self):
        return not self.available

    @property
    def created_on(self):
        match = re.search("Created On:\s+(.*)\n", self.content_for_scanner)
        if match:
            return time_parser.parse(match.group(1))

    @property
    def updated_on(self):
        match = re.search("Last Updated On:\s+(.*)\n", self.content_for_scanner)
        if match:
            return time_parser.parse(match.group(1))      

    @property
    def expires_on(self):
        match = re.search("Expiration Date:\s+(.*)\n", self.content_for_scanner)
        if match:
            return time_parser.parse(match.group(1))      

    # Nameservers are listed in the following formats:
    #
    #   Name Server: dns2.gencat.cat 83.247.132.4
    #   Name Server: dns.gencat.net
    #
    @property
    def nameservers(self):
        nameservers = []
        for nameserver in re.findall("Name Server:\s+(.+)\n", self.content_for_scanner):
            if ' ' in nameserver:
                name, ipv4 = nameserver.split(" ")
                nameservers.append(Nameserver(name = name, ipv4 = ipv4))
            else:
                nameservers.append(Nameserver(name = nameserver))
        return nameservers