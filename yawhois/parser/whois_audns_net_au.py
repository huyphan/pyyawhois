from .base_scannable import ScannableParserBase
from ..scanner.whois_audns_net_au import WhoisAudnsNetAuScanner
from ..utils import array_wrapper
from ..record import Nameserver
from ..record import Contact
from ..record import Registrar
from dateutil import parser as time_parser

class WhoisAudnsNetAuParser(ScannableParserBase):

    _scanner = WhoisAudnsNetAuScanner

    @property
    def domain(self):
          return self.node("Domain Name")

    # == Values for Status
    #
    # @see http://www.auda.org.au/policies/auda-2002-28/
    # @see http://www.auda.org.au/policies/auda-2006-07/
    #
    @property
    def status(self):
        return array_wrapper(self.node("Status"))

    @property
    def available(self):
        return bool(self.node("status:available"))

    @property
    def registered(self):
        return not self.available

    @property
    def updated_on(self):
        if self.node("Last Modified"):
            return time_parser.parse(self.node("Last Modified"))

    @property
    def registrar(self):
        if self.node("Registrar ID"):
            return Registrar(id = self.node("Registrar ID"), name = self.node("Registrar Name"))

    @property
    def registrant_contacts(self):
        contact = self._build_contact("Registrant Contact", Contact.TYPE_REGISTRANT)
        if contact:
          contact.organization = self.node("Registrant") 
          return contact

    @property
    def technical_contacts(self):
        return self._build_contact("Tech Contact", Contact.TYPE_TECHNICAL)

    @property
    def nameservers(self):
        return [Nameserver(name = name) for name in array_wrapper(self.node("Name Server"))]

    def _build_contact(self, element, type_):
        if self.node("%s ID" % element):
            return Contact(**{
              'type' : type_,
              'id'   : self.node("%s ID" % element),
              'name' : self.node("%s Name" % element),
              'email': self.node("%s Email" % element)
            })