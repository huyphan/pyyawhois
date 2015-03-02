from .base_scannable import ScannableParserBase
from ..scanner.whois_centralnic_com import WhoisCentralnicComScanner
from ..utils import array_wrapper
from ..record import Nameserver
from ..record import Contact
from ..record import Registrar
from dateutil import parser as time_parser

class WhoisCentralnicComParser(ScannableParserBase):

    _scanner = WhoisCentralnicComScanner

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
            return time_parser.parse(self.node("Created On"))

    @property
    def updated_on(self):
        if self.node("Last Updated On"):
            return time_parser.parse(self.node("Last Updated On"))

    @property
    def expires_on(self):
        if self.node("Expiration Date"):
            return time_parser.parse(self.node("Expiration Date"))

    @property
    def registrar(self):
        if self.node("Sponsoring Registrar ID"):
            return Registrar(**{
                'id'           : self.node("Sponsoring Registrar ID"),
                'name'         : None,
                'organization' : self.node("Sponsoring Registrar Organization"),
                'url'          : self.node("Sponsoring Registrar Website")
            })

    @property
    def registrant_contacts(self):
        return self._build_contact("Registrant", Contact.TYPE_REGISTRANT)

    @property
    def admin_contacts(self):
        return self._build_contact("Admin", Contact.TYPE_ADMINISTRATIVE)

    @property
    def technical_contacts(self):
        return self._build_contact("Tech", Contact.TYPE_TECHNICAL)

    @property
    def nameservers(self):
        return [Nameserver(name=name.lower().strip(". ")) for name in array_wrapper(self.node("Name Server"))]


    def _build_contact(self, element, type_):
        if self.node("%s ID" % element):

            address = "\n".join(filter(None, [self.node("%s Street%d" % (element, i)) for i in range(1, 4)]))
            if len(address) == 0:
                address = None 

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
                'fax'          : self.node("%s FAX" % element),
                'email'        : self.node("%s Email" % element)
            })