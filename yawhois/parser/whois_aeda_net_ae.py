import re
from .base import ParserBase
from ..exceptions import ParserError
from ..record import Nameserver

class WhoisAedaNetAeParser(ParserBase):

    @property
    def status(self):
        pattern = re.compile("Status:\s+(.+?)\n")
        match   = pattern.search(self.content_for_scanner)
        if match:
            status = match.group(1)
            if status == "ok":
                return "registered"
            raise ParserError("Unknown status '%s'." % status)

        return "available"

    @property
    def available(self):
        return self.content_for_scanner.strip() == "No Data Found"

    @property
    def registered(self):
        return not self.available

    @property
    def nameservers(self):
        pattern = re.compile("Name Server:\s+(.+)\n")
        return [Nameserver(name = name) for name in  pattern.findall(self.content_for_scanner)]
