from .base_scannable import ScannableParserBase
from ..scanner.whois_cctld_by import WhoisCctldByScanner
from ..utils import array_wrapper
from ..record import Nameserver
from ..record import Registrar
from dateutil import parser as time_parser

class WhoisCctldByParser(ScannableParserBase):

    _scanner = WhoisCctldByScanner

    @property
    def domain(self):
        if self.node("Domain Name"):
            return self.node("Domain Name").lower()

    @property
    def status(self):
        if self.available:
            return 'available'
        else:
            return 'registered'

    @property
    def available(self):
        return bool(self.node("status:available"))

    @property
    def registered(self):
        return not self.available

    @property
    def created_on(self):
        if self.node("Creation Date"):
            return time_parser.parse(self.node("Creation Date"))

    @property
    def updated_on(self):
        if self.node("Updated Date"):
            return time_parser.parse(self.node("Updated Date"))

    @property
    def expires_on(self):
        if self.node("Expiration Date"):
            return time_parser.parse(self.node("Expiration Date"))

    @property
    def registrar(self):
        registrar = self.node("Registrar")
        if registrar:
            return Registrar(id=registrar, name=registrar, organization=registrar)

    @property
    def nameservers(self):
        return [Nameserver(name=name.lower()) for name in array_wrapper(self.node("Name Server"))]
