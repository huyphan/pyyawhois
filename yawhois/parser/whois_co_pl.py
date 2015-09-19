from .base import ParserBase
from ..record import Nameserver
from dateutil import parser as time_parser
import re

class WhoisCoPlParser(ParserBase):

    @property
    def domain(self):
        match = re.search("domain:\s+(.+?)\n", self.content_for_scanner)
        if match:
            return match.group(1)

    @property
    def status(self):
        if self.available:
            return 'available'
        else:
            return 'registered'

    @property
    def available(self):
        return bool(re.search("% Unfortunately, No Results Were Found", self.content_for_scanner))

    @property
    def registered(self):
        return not self.available

    @property
    def updated_on(self):
        match = re.search("changed:\s+(.+?)\n", self.content_for_scanner)
        if match:
            return time_parser.parse(match.group(1))

    @property
    def nameservers(self):
        return [Nameserver(name=name) for name in re.findall("nserver:\s+(.+)\n", self.content_for_scanner)]
