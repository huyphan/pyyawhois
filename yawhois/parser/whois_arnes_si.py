from .base_scannable import ScannableParserBase
from ..exceptions import ParserError
from ..record import *
from dateutil import parser as timeparser
import re

class WhoisArnesSiParser(ScannableParserBase):

    @property
    def status(self):
        pattern = re.compile("status:\s+(.+)\n")
        match = pattern.search(self.content_for_scanner)

        if match:
            statuses = match.group(1).strip().lower().split(",")
            if 'ok' in statuses or 'serverupdateprohibited' in statuses:
                return 'registered'
            else:
                raise ParserError("Unknown status '%s'." % statuses)
        else:
            return 'available'

    @property
    def available(self):
        return "% No entries found" in self.content_for_scanner

    @property
    def registered(self):
        return not self.available

    @property
    def created_on(self):
        match = re.compile("created:\s+(.*)\n").search(self.content_for_scanner)
        if match:
            return timeparser.parse(match.group(1))

    @property
    def expires_on(self):
        match = re.compile("expire:\s+(.*)\n").search(self.content_for_scanner)
        if match:
            return timeparser.parse(match.group(1))

    @property
    def nameservers(self):
        pattern = re.compile("nameserver:\s+(.+)\n")
        return [Nameserver(name.strip().lower()) for name in pattern.findall(self.content_for_scanner)] 
