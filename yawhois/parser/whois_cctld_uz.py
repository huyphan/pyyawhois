from .base import ParserBase
from ..record import Nameserver
from ..exceptions import ParserError
from dateutil import parser as time_parser
import re

class WhoisCctldUzParser(ParserBase):

    @property
    def status(self):
        match = re.search("^Status: (.+?)\n", self.content_for_scanner, re.MULTILINE)
        if match:
            if match.group(1).lower() == "active":
                return 'registered'
            elif match.group(1).lower() == "reserved":
                return 'reserved'
            else:
                raise ParserError("Unknown status '%s'" % match.group(1))
        else:
            return 'available'

    @property
    def available(self):
        return "not found in database" in self.content_for_scanner

    @property
    def registered(self):
        return not self.available

    @property
    def created_on(self):
        match = re.search("Creation Date:(.+)\n", self.content_for_scanner)
        if match:
            return time_parser.parse(match.group(1))

    @property
    def updated_on(self):
        match = re.search("Updated Date:(.+)\n", self.content_for_scanner)
        if match:
            return time_parser.parse(match.group(1))

    @property
    def expires_on(self):
        match = re.search("Expiration Date:\s+(.+)\n", self.content_for_scanner)
        if match and match.group(1) != '-':
            return time_parser.parse(match.group(1))      

    @property
    def nameservers(self):
        match = re.search("Domain servers in listed order:\n((.+\n)+)\n", self.content_for_scanner)
        if match:
            return [Nameserver(name=name.strip(" .")) for name in filter(None, match.group(1).split("\n"))]
