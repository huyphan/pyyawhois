from dateutil import parser as time_parser
from .base_scannable import ScannableParserBase
from ..scanner.verisign import VerisignScanner
from ..utils import array_wrapper
from ..record import Nameserver, Registrar

class VerisignParserBase(ScannableParserBase):

    _scanner = VerisignScanner

    @property
    def disclaimer(self):
        return self.node("Disclaimer")

    @property
    def domain(self):
        return self.node("Domain Name").lower()

    @property
    def domain_id(self):
        return self.node("Domain ID")

    @property
    def status(self):
        if self.available:
            return "available"
        else:
            return "registered"

    @property
    def available(self):
        return "No match for" in self.content_for_scanner

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
        if self.node("Registry Expiry Date"):
            return time_parser.parse(self.node("Registry Expiry Date"))

    @property
    def registrar(self):
        value = self.node("Sponsoring Registrar")
        if value:
            return Registrar(id   = self.last_useful_item(self.node("Sponsoring Registrar IANA ID")), 
                             name = self.last_useful_item(self.node("Sponsoring Registrar")), 
                             url  = self.referral_url)

    @property
    def nameservers(self):
        return [Nameserver(name = name.lower()) for name in filter(lambda x: "no nameserver" not in x.lower(), array_wrapper(self.node("Name Server")))]

    @property
    def referral_whois(self):
        return self.last_useful_item(self.node("Whois Server"))

    @property
    def referral_url(self):
        return self.last_useful_item(self.node("Referral URL"))

    # In case of "SPAM Response", the response contains more than one item
    # for the same value and the value becomes an Array.
    def last_useful_item(self, values):
        if isinstance(values, list):
            return values[-1]
        return values
