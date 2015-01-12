from .base_scannable import ScannableParserBase
from ..record import *
import re

class WhoisAiParser(ScannableParserBase):

    @property
    def status(self):
        if self.available:
            return 'available'
        else:
            return 'registered'

    @property
    def available(self):
        pattern = re.compile("Domain (.+?) not registred")
        return bool(pattern.search(self.content_for_scanner))
    @property
    def registered(self):
        return not self.available

    @property
    def nameservers(self):
        pattern = re.compile("Nameservers\n((.+\n)+)\n")
        servers = []
        for match in pattern.findall(self.content_for_scanner):
            for line in match[0].split("\n"):
                if "Server Hostname" in line:
                    servers.append(Nameserver(name = line.split(":")[-1].strip()))
        return servers