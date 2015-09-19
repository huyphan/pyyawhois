from .base import ParserBase
from ..record import Nameserver
from ..exceptions import ParserError
from dateutil import parser as time_parser
from datetime import datetime
import re

class WhoisCoUgParser(ParserBase):

    def __init__(self, *args):
        super(WhoisCoUgParser, self).__init__(*args)

    @property
    def status(self):
        match = re.search("^Status:\s+(.+?)\n", self.content_for_scanner, re.MULTILINE)
        if match:
            status = match.group(1).lower()
            if status == 'active':
                return 'registered'
            elif status == 'unconfirmed':
                return 'registered'
            else:
                raise ParserError("Unknown status `%s`" % status)
        else:
            return 'available'

    @property
    def available(self):
        return bool(re.search("% No entries found for the selected source", self.content_for_scanner))

    @property
    def registered(self):
        return not self.available

    @property
    def created_on(self):
        match = re.search("Registered:\s+(.+)$", self.content_for_scanner, re.MULTILINE)
        if match:
            return time_parser.parse(match.group(1))

    @property
    def updated_on(self):
        match = re.search("Updated:\s+(.+)$", self.content_for_scanner, re.MULTILINE)
        if match:
            return time_parser.parse(match.group(1).replace("EAT", "+0300"), dayfirst=True)

    @property
    def expires_on(self):
        match = re.search("Expiry:\s+(.+)$", self.content_for_scanner, re.MULTILINE)
        if match:
            return time_parser.parse(match.group(1))      

    @property
    def nameservers(self):
        return [Nameserver(name=name.lower()) for name in re.findall("Nameserver:\s+(.+)\n", self.content_for_scanner)]

