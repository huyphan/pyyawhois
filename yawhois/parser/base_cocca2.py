from .base_scannable import ScannableParserBase
from ..scanner.base_cocca2 import BaseCocca2Scanner
from ..utils import array_wrapper
from ..record import *
from dateutil import parser as timeparser

class BaseCocca2Parser(ScannableParserBase):

    _scanner = BaseCocca2Scanner

    @property
    def domain(self):
        return self.node("Domain Name").lower()

    @property
    def domain_id(self):
        return self.node("Domain ID")

    @property
    def status(self):
        statuses = map(lambda x: x.lower(), array_wrapper(self.node("Domain Status")))

        if "no object found" in statuses:
            return "available"

        if "ok" in statuses:
            return "registered"

        raise ParserError("Unknown status '%s'." % ", ".join(statuses))

    @property
    def available(self):
        return self.status == "available"

    @property
    def registered(self):
        return not self.available

    @property
    def created_on(self):
        value = self.node('Creation Date')
        if value:
            return timeparser.parse(value)
    
    @property
    def updated_on(self):
        value = self.node('Updated Date')
        print value
        if value:
            return timeparser.parse(value)

    @property
    def expires_on(self):
        value = self.node('Registry Expiry Date')
        if value:
            return timeparser.parse(value)

    @property
    def registrar(self):
        if self.node("Sponsoring Registrar"):
            return Registrar(
                id   = self.node("Sponsoring Registrar IANA ID") or None,
                name = self.node("Sponsoring Registrar"),
                url  = self.node("Sponsoring Registrar URL") or None,
            )

    @property
    def nameservers(self):
        return [Nameserver(name = name) for name in filter(None, array_wrapper(self.node("Name Server")))]
