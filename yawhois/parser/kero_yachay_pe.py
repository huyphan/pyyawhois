from .base import ParserBase
from ..exceptions import ResponseError, ParserError
import re

class KeroYachayPeParser(ParserBase):

    '''
    Parser for the kero.yachay.pe server.

    This parser is just a stub and provides only a few basic methods
    to check for domain availability and get domain status.
    '''

    @property
    def status(self):
        match = re.compile("Status:\s+(.+?)\n", re.M).search(self.content_for_scanner)
        if match:
            status = match.group(1).lower()
            if status == "active":
                return "registered"
            elif status == "suspended":
                return "registered"
            elif status == "not registered":
                return "available"
            elif status == "inactive":
                return "inactive"
            else:
                raise ResponseError("Unknown status: '%s'" % status)
        else:
            raise ParserError("Unable to parse status")

    @property
    def available(self):
        return self.status == "available"

    @property
    def registered(self):
        return self.status == "registered"

    @property
    def nameservers(self):
        match = re.compile("Name Servers:\n((.+\n)+)\n", re.M).search(self.content_for_scanner)
        if match:
            content = match.group(1)
            return [{'name': name.strip()} for name in content.split("\n")]

    @property
    def response_throttled(self):
        return "Looup quota exceeded." in self.content_for_scanner