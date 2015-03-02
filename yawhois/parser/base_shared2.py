from .base_scannable import ScannableParserBase
from ..scanner.base_shared2 import BaseShared2Scanner
from ..utils import array_wrapper
from ..record import Nameserver
from ..record import Contact
from ..record import Registrar
from dateutil import parser as time_parser

class BaseShared2Parser(ScannableParserBase):
    _scanner = BaseShared2Scanner

    @property
    def domain(self):
        if self.node("Domain Name"):
            return self.node("Domain Name").lower()

    @property
    def domain_id(self):
        return self.node("Domain ID")

    @property
    def status(self):
        if self.node("Domain Status"):
            return array_wrapper(self.node("Domain Status"))

    @property
    def available(self):
        return bool(self.node("status:available"))

    @property
    def registered(self):
        return not self.available

    @property
    def created_on(self):
        if self.node("Domain Registration Date"):
            return time_parser.parse(self.node("Domain Registration Date"))

    @property
    def updated_on(self):
        if self.node("Domain Last Updated Date"):
            return time_parser.parse(self.node("Domain Last Updated Date"))

    @property
    def expires_on(self):
        if self.node("Domain Expiration Date"):
            return time_parser.parse(self.node("Domain Expiration Date"))

    @property
    def registrar(self):
        if self.node("Sponsoring Registrar"):
            return Registrar(id = self.node("Sponsoring Registrar IANA ID"), name = self.node("Sponsoring Registrar"))

    @property
    def registrant_contacts(self):
        return self._build_contact("Registrant", Contact.TYPE_REGISTRANT)

    @property
    def admin_contacts(self):
        return self._build_contact("Administrative Contact", Contact.TYPE_ADMINISTRATIVE)

    @property
    def technical_contacts(self):
        return self._build_contact("Technical Contact", Contact.TYPE_TECHNICAL)

    @property
    def nameservers(self):
        return [Nameserver(name = name.lower()) for name in array_wrapper(self.node("Name Server"))]

    def _build_contact(self, element, type_):
        if self.node("%s ID" % element):

            address = "\n".join(filter(None, [self.node("%s Address%d" % (element, i)) for i in range(1, 4)]))
            
            return Contact(**{
                'type'         : type_,
                'id'           : self.node("%s ID" % element),
                'name'         : self.node("%s Name" % element),
                'organization' : self.node("%s Organization" % element),
                'address'      : address,
                'city'         : self.node("%s City" % element),
                'zip'          : self.node("%s Postal Code" % element),
                'state'        : self.node("%s State/Province" % element),
                'country'      : self.node("%s Country" % element),
                'country_code' : self.node("%s Country Code" % element),
                'phone'        : self.node("%s Phone Number" % element),
                'fax'          : self.node("%s Facsimile Number" % element),
                'email'        : self.node("%s Email" % element)
            })
         