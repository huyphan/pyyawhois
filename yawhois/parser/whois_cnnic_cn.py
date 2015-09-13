from .base_scannable import ScannableParserBase
from ..scanner.whois_cnnic_cn import WhoisCnnicCnScanner
from ..utils import array_wrapper
from ..record import Nameserver
from ..record import Contact
from ..record import Registrar
from dateutil import parser as time_parser

class WhoisCnnicCnParser(ScannableParserBase):

    _scanner = WhoisCnnicCnScanner

    @property
    def domain(self):
        if self.node("Domain Name"):
            return self.node("Domain Name").lower()

    @property
    def domain_id(self):
        if self.node("ROID"):
            return self.node("ROID")

    @property
    def status(self):
        return array_wrapper(self.node("Domain Status"))

    @property
    def available(self):
        return bool(self.node("status:available"))

    @property
    def registered(self):
        return not self.reserved and not self.available

    @property
    def created_on(self):
        value = self.node("Registration Time")
        if value:
            return time_parser.parse(value)

    @property
    def expires_on(self):
        value = self.node("Expiration Time")
        if value:
            return time_parser.parse(value)      

    @property
    def registrar(self):
        value = self.node("Sponsoring Registrar")
        if value:
            return Registrar(id=value, name=value)

    @property
    def registrant_contacts(self):
        return self._build_contact("Registrant", Contact.TYPE_REGISTRANT)

    @property
    def admin_contacts(self):
        return self._build_contact("Administrative", Contact.TYPE_ADMINISTRATIVE)

    @property
    def nameservers(self):
        nameservers = []
        for nameserver in array_wrapper(self.node("Name Server")):
            nameservers.append(Nameserver(name = nameserver.lower()))
        return nameservers

    @property
    def reserved(self):
        return bool(self.node("status:reserved"))

    def _build_contact(self, element, type_):
        if self.node(element):
            return Contact(**{
                'type'         : type_,
                'id'           : self.node("%s ID" % element),
                'name'         : self.node(element),
                'email'        : self.node("%s Contact Email" % element)
            })