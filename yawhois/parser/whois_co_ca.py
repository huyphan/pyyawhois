from .base import ParserBase
from ..record import Nameserver
from dateutil import parser as time_parser
import re

class WhoisCoCaParser(ParserBase):

    @property
    def status(self):
        if self.available:
            return 'available'
        elif self.reserved:
            return 'reserved'
        else:
            return 'registered'

    @property
    def available(self):
        return bool(re.search("^(.+) is available", self.content_for_scanner))

    @property
    def registered(self):
        return not self.available

    @property
    def created_on(self):
        match = re.search("date_approved:\s+(.+)\n", self.content_for_scanner)
        if match:
            return time_parser.parse(match.group(1))

    @property
    def expires_on(self):
        match = re.search("date_renewal:\s+(.+)\n", self.content_for_scanner)
        if match:
            return time_parser.parse(match.group(1))

    @property
    def nameservers(self):
        nameservers = re.findall("ns[\d]_hostname:\s+(.+)\n", self.content_for_scanner)
        return [Nameserver(name=name) for name in nameservers]

    @property
    def reserved(self):
        return bool(re.search("^Domain is not available or is reserved by the registry", self.content_for_scanner))
