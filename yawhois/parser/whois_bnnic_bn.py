from .base import ParserBase
from ..record import Nameserver
from dateutil import parser as time_parser
import re

class WhoisBnnicBnParser(ParserBase):

    @property
    def status(self):
        if self.available:
            return 'available'

        return 'registered'

    @property
    def available(self):
        return bool(re.search("^Domain Not Found", self.content_for_scanner))

    @property
    def registered(self):
        return not self.available

    @property
    def created_on(self):
        match = re.search("Creation Date:\s+(.+)\n", self.content_for_scanner)
        if match:
            return time_parser.parse(match.group(1)) 

    @property
    def updated_on(self):
        match = re.search("Modified Date:\s+(.+)\n", self.content_for_scanner)
        if match:
            return time_parser.parse(match.group(1))       

    @property
    def expires_on(self):
        match = re.search("Expiration Date:\s+(.+)\n", self.content_for_scanner)
        if match:
            return time_parser.parse(match.group(1))             

    @property
    def nameservers(self):
        match = re.search("Name Servers:\n((.+\n)+)\n", self.content_for_scanner)
        nameservers = []        
        if match:
            for line in match.group(1).split("\n"):
                if not line: continue
                name, ipv4 = re.findall("(.+) \((.+)\)", line)[0]
                nameservers.append(Nameserver(name=name.strip().lower(), ipv4=ipv4.strip().split(",")[0]))
        return nameservers
