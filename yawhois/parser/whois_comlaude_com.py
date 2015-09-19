from .base import ParserBase
from ..record import Nameserver
from ..record import Contact
from ..record import Registrar
from dateutil import parser as time_parser
import re

class WhoisComlaudeComParser(ParserBase):

    def __init__(self, *args):
        super(WhoisComlaudeComParser, self).__init__(*args)
        
    # The server is contacted only in case of a registered(self):main.
    @property
    def available(self):
        return False
    
    @property
    def registered(self):
        return not self.available
    
    @property
    def created_on(self):
        match = re.search("Registered: (.+)\n", self.content_for_scanner)
        if match:
            return time_parser.parse(match.group(1))

    @property
    def expires_on(self):
        match = re.search("Expires: (.+)\n", self.content_for_scanner)
        if match:
            return time_parser.parse(match.group(1))

    @property
    def registrar(self):
        return Registrar(name="NOM IQ LTD (DBA COM LAUDE)", url="http://www.comlaude.com")
          
    @property
    def registrant_contacts(self):
        return self._build_contact("Registrant Contact:", Contact.TYPE_REGISTRANT)
    
    @property
    def admin_contacts(self):
        return self._build_contact("Admin Contact:", Contact.TYPE_ADMINISTRATIVE)

    @property
    def technical_contacts(self):
        return self._build_contact("Technical Contact:", Contact.TYPE_TECHNICAL)

    @property
    def nameservers(self):
        match = re.search("Nameservers:\n((?:\s*[^\s\n]+\n)+)\n", self.content_for_scanner)
        print self.content_for_scanner
        if match:
            print match.group(1).split("\n")
            return [Nameserver(name=line.strip()) for line in match.group(1).split("\n") if line]

    def _build_contact(self, element, type_):
        match = re.search(element + "\n((.+\n)*)\n\n", self.content_for_scanner)
        if match:
            lines = map(lambda x: x.strip(), match.group(1).split("\n"))

            # 0 Domain Manager
            # 1 Nom-IQ Ltd dba Com Laude
            #   2nd Floor, 28-30 Little Russell Street
            #   London WC1A 2HN
            #   United Kingdom
            #   Phone: +44.2078360070
            #   Fax: +44.2078360070
            #   Email: admin@comlaude.com

            contact = Contact(**{
                'type': type_,
                'name': lines[0],
                'organization': lines[1],
                'address': None,
                'city': None,
                'state': None,
                'zip': None,
                'country': None
            })

            m = re.search("Phone: (.*)", match.group(1))
            if m:
                contact.phone = m.group(1)

            m = re.search("Email: (.*)", match.group(1))
            if m:
                contact.email = m.group(1)

            m = re.search("Fax: (.*)", match.group(1))
            if m:
                contact.fax = m.group(1)

            return contact
