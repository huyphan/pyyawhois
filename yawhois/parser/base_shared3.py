from dateutil import parser as time_parser
from .base_scannable import ScannableParserBase
from ..record import Registrar, Contact, Nameserver
from ..scanner.base_shared3 import BaseShared3Scanner
from ..utils import array_wrapper

class BaseShared3Parser(ScannableParserBase):

    _scanner = BaseShared3Scanner

    @property
    def disclaimer(self):
        return self.node("field:disclaimer")

    @property
    def domain(self):
        if self.node("domain name"):
            return self.node("domain name").lower()

    @property
    def status(self):
        if self.available:
            return "available"
        else:
            return "registered"

    @property
    def available(self):
        return bool(self.node('status:available'))

    @property
    def registered(self):
        return not bool(self.node('status:available'))

    @property
    def created_on(self):
        if self.node("created date"):
            return time_parser.parse(self.node("created date"))

    @property
    def updated_on(self):
        if self.node("updated date"):
            return time_parser.parse(self.node("updated date"))

    @property
    def expires_on(self):
        if self.node("expiration date"):
            return time_parser.parse(self.node("expiration date"))

    @property
    def registrar(self):
        value = self.node('registrar')
        if value:
            return Registrar(None, value, None, self.node('url'))

    @property
    def registrant_contacts(self):
        return array_wrapper(self._build_contact("owner", Contact.TYPE_REGISTRANT))

    @property
    def admin_contacts(self):
        return array_wrapper(self._build_contact('admin', Contact.TYPE_ADMINISTRATIVE))

    @property
    def technical_contacts(self):
        return array_wrapper(self._build_contact('tech', Contact.TYPE_TECHNICAL))

    @property
    def nameservers(self):
        return [Nameserver(name = name) for name in filter(None, array_wrapper(self.node("nameserver")))]

    def _build_contact(self, element, type_):
        if self.node("%s-contact" % element):
            return Contact(**{
                'type'         : type_,
                'id'           : self.node("%s-contact"      % element),
                'name'         : self.node("%s-name"         % element),
                'organization' : self.node("%s-organization" % element),
                'address'      : self.node("%s-street"       % element),
                'city'         : self.node("%s-city"         % element),
                'zip'          : self.node("%s-zip"          % element),
                'state'        : None,
                'country_code' : self.node("%s-country"      % element),
                'phone'        : self.node("%s-phone"        % element),
                'fax'          : self.node("%s-fax"          % element),
                'email'        : self.node("%s-email"        % element)
            })
