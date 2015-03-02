from dateutil import parser as time_parser
from .base_scannable import ScannableParserBase
from ..scanner.whois_ati_tn import WhoisAtiTnScanner
from ..utils import array_wrapper
from ..record import Nameserver
from ..record import Contact
from ..record import Registrar
import re 

class WhoisAtiTnParser(ScannableParserBase):

    _scanner = WhoisAtiTnScanner

    @property
    def disclaimer(self):
        return self.node('field:disclaimer')

    @property
    def domain(self):
        return self.node('Domain')

    @property
    def status(self):
        if self.available:
            return 'available'
        else:
            return 'registered'

    @property
    def available(self):
          return bool(self.node('status:available'))

    @property
    def registered(self):
           return not self.available


    @property
    def created_on(self):
        if self.node('Acivated'):
            return time_parser.parse(self.node('Acivated'))

    @property
    def registrar(self):
        if self.node('Registrar'):
            return Registrar(id = None, name = self.node('Registrar'))

    @property
    def registrant_contacts(self):
        return self._build_contact('Owner', Contact.TYPE_REGISTRANT)

    @property
    def admin_contacts(self):
        return self._build_contact('Admin.', Contact.TYPE_ADMINISTRATIVE)

    @property
    def technical_contacts(self):
        return self._build_contact('Tech.', Contact.TYPE_TECHNICAL)

    @property
    def nameservers(self):
        pattern = re.compile("(.+)\. \[(.+)\]")
        nameservers = []
        if self.node('NameServers'):
            for nameserver in array_wrapper(self.node('NameServers')):
                match = pattern.match(nameserver)
                if match:
                    name, ipv4 = match.group(1), match.group(2)
                    nameservers.append(Nameserver(name = name, ipv4 = ipv4))

        if len(nameservers):
            return nameservers

    def _build_contact(self, element, type_):

        if self.node("%s Name" % element):
            return Contact(**{
                'type'         : type_,
                'name'         : self.node("%s Name"         % element),
                'address'      : self.node("%s Address"      % element),
                'phone'        : self.node("%s Tel"          % element),
                'fax'          : self.node("%s Fax"          % element),
                'email'        : self.node("%s Email"        % element),
                'created_on'   : time_parser.parse(self.node("%s Created" % element)),
                'updated_on'   : time_parser.parse(self.node("%s Updated" % element)) if self.node("%s Updated" % element) != 'None' else None
            })
