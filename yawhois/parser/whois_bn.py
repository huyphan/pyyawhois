from .base import ParserBase
from ..record import Nameserver
from dateutil import parser as time_parser
import re

class WhoisBnParser(ParserBase):

    @property
    def status(self):
        if self.available:
            return 'available'
        else:
            return 'registered'

    @property
    def available(self):
        return bool(re.search("^No records matching .+ found", self.content_for_scanner, re.MULTILINE))

    @property
    def registered(self):
        return not self.available

    @property
    def created_on(self):
        match = re.search("Created:\s+(.+)\n", self.content_for_scanner)
        if match:
            return time_parser.parse(match.group(1))

    @property
    def updated_on(self):
        match = re.search("Last Updated:\s+(.+)\n", self.content_for_scanner)
        if match:
            return time_parser.parse(match.group(1))

    @property
    def nameservers(self):
        return [Nameserver(name = name.lower()) for name in re.findall("Name Server \d:\s+(.+)\n", self.content_for_scanner)]
