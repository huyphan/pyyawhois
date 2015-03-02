from .base_scannable import ScannableParserBase
from ..scanner.whois_cira_ca import WhoisCiraCaScanner
from ..utils import array_wrapper
from ..record import Nameserver
from ..record import Contact
from ..record import Registrar
from ..exceptions import ParserError
from dateutil import parser as time_parser
import re

class WhoisCiraCaParser(ScannableParserBase):

    _scanner = WhoisCiraCaScanner

    @property
    def disclaimer(self):
        return self.node("field:disclaimer")


    @property
    def domain(self):
        return self.node("Domain name")

    @property
    def status(self):
      match = re.search("Domain status:\s+(.+?)\n", self.content_for_scanner)
      if match:
          status = match.group(1)
          if status in ['registered', 'redemption', 'auto-renew grace', 'to be released', 'pending delete']:
              return 'registered'
          elif status == 'available':
              return 'available'
          elif status == 'unavailable':
              return 'invalid'
          else:
              raise ParserError("Unknown status '%s'" % status)
      else:
          raise ParserError("Unable to parse status")

    @property
    def available(self):
        return self.status == 'available'

    @property
    def registered(self):
        return not self.available

    @property
    def created_on(self):
        if self.node("Creation date"):
            return time_parser.parse(self.node("Creation date"))

    @property
    def updated_on(self):
        if self.node("Updated date"):
            return time_parser.parse(self.node("Updated date"))

    @property
    def expires_on(self):
        if self.node("Expiry date"):
            return time_parser.parse(self.node("Expiry date"))

    @property
    def registrar(self):
        if self.node("Registrar"):
            return Registrar(**{
                'id': self.node("Registrar")["Number"],
                'name': self.node("Registrar")["Name"],
                'organization': self.node("Registrar")["Name"],
            })

    @property
    def registrant_contacts(self):
        return self._build_contact("Registrant", Contact.TYPE_REGISTRANT)

    @property
    def admin_contacts(self):
        return self._build_contact("Administrative contact", Contact.TYPE_ADMINISTRATIVE)

    @property
    def technical_contacts(self):
        return self._build_contact("Technical contact", Contact.TYPE_TECHNICAL)

    # Nameservers are listed in the following formats:
    #
    #   ns1.google.com
    #   ns2.google.com
    #
    #   ns1.google.com  216.239.32.10
    #   ns2.google.com  216.239.34.10
    #
    @property
    def nameservers(self):
        nameservers = []
        for nameserver in array_wrapper(self.node("field:nameservers")):
            name, ipv4 = re.split("/\s+", nameserver)
            nameservers.append(Nameserver(name = name, ipv4 = ipv4))
        return nameservers

    # Attempts to detect and returns the version.
    #
    # TODO: This is very empiric.
    #       Use the available status in combination with the creation date label.
    #
    # NEWPROPERTY
    @property
    def version(self):
        match = re.search("^% \(c\) (.+?) Canadian Internet Registration Authority", self.content_for_scanner)
        if match:
            if match.group(1) == '2007':
                return '1'
            elif match.group(1) == '2010':
                return '2'
            else:
                raise ParserError("Unable to detect version.")
        else:
            raise ParserError("Unable to detect version.")

    @property
    def invalid(self):
        return self.status == 'invalid'

    @property
    def valid(self):
        return not self.invalid

    def _build_contact(self, element, type_):
        if self.node(element):
            return Record(**{
                'type'         : type_,
                'id'           : None,
                'name'         : self.node(element)["Name"],
                'organization' : None,
                'address'      : self.node(element)["Postal address"],
                'city'         : None,
                'zip'          : None,
                'state'        : None,
                'country'      : None,
                'phone'        : self.node(element)["Phone"],
                'fax'          : self.node(element)["Fax"],
                'email'        : self.node(element)["Email"]
            })
