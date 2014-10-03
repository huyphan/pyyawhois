import re
from dateutil import parser as timeparser
from .base_scannable import ScannableParserBase
from ..scanner.base_afilias import BaseAfiliasScanner
from ..utils import array_wrapper
from ..record import *
from ..exceptions import ParserError

class BaseAfiliasParser(ScannableParserBase):

    _scanner = BaseAfiliasScanner

    @property
    def disclaimer(self):
        return self.node("field:disclaimer")

    @property
    def domain(self):
        if self.node("Domain Name"):
            return self.node("Domain Name").lower()

    @property
    def domain_id(self):
        return self.node("Domain ID")

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
    def created_on(self):
        if self.node("Created On"):
            return timeparser.parse(self.node("Created On"))

    @property
    def updated_on(self):
        if self.node("Last Updated On"):
            return timeparser.parse(self.node("Last Updated On"))

    @property
    def expires_on(self):
        if self.node("Expiration Date"):
            return timeparser.parse(self.node("Expiration Date"))

    @property
    def registrar(self):
        value = self.node("Sponsoring Registrar")
        if value:
            try:
                id_, name = self._decompose_registrar(value)
                return Registrar(id = id_, name = name)
            except Exception, e:
                raise ParserError("Unknown registrar format '%s'" % value)

    @property
    def nameservers(self):
        return [Nameserver(name = name.lower()) for name in filter(None, array_wrapper(self.node("Name Server")))]

    @property
    def registrant_contacts(self):
        return array_wrapper(self._build_contact("Registrant", Contact.TYPE_REGISTRANT))

    @property
    def admin_contacts(self):
        return array_wrapper(self._build_contact('Admin', Contact.TYPE_ADMINISTRATIVE))

    @property
    def technical_contacts(self):
        return array_wrapper(self._build_contact('Tech', Contact.TYPE_TECHNICAL))

    def _build_contact(self, element, type_):
        value = self.node("%s ID" % element)
        if value:
            addresses = []

            for c in ["", "1", "2", "3"]:
                add = self.node("%s Street%s" % (element, c))
                addresses.append(add)

            address = "\n".join(filter(None, addresses))

            return Contact(**{
                'type'         : type_,
                'id'           : self.node("%s ID" % element),
                'name'         : self.node("%s Name" % element),
                'organization' : self.node("%s Organization" % element),
                'address'      : address,
                'city'         : self.node("%s City" % element),
                'zip'          : self.node("%s Postal Code" % element),
                'state'        : self.node("%s State/Province" % element),
                'country_code' : self.node("%s Country" % element),
                'phone'        : self.node("%s Phone" % element),
                'fax'          : self.node("%s FAX" % element) or self.node("%s Fax" % element),
                'email'        : self.node("%s Email" % element)
            })

    def _decompose_registrar(self, value):
        pattern = re.compile("(.+?) \((.+?)\)")
        match = pattern.search(value)
        if match:
            return (match.group(2), match.group(1))
