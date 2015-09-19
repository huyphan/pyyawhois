from .base_scannable import ScannableParserBase
from ..scanner.whois_denic_de import WhoisDenicDeScanner
from ..exceptions import ParserError
from ..record import Nameserver
from ..record import Contact
from ..record import Registrar
from dateutil import parser as time_parser
import re

class WhoisDenicDeParser(ScannableParserBase):

    _scanner = WhoisDenicDeScanner

    @property
    def disclaimer(self):
        return self.node('Disclaimer')

    @property
    def domain(self):
        return self.node('Domain')

    @property
    def status(self):
        status = self.node('Status')
        if status == 'connect':
            return 'registered'
        elif status == 'free':
            return 'available'
        elif status == 'invalid':
            return 'invalid'
        elif status == 'failed':
            return 'registered'
        elif self.response_error:
            return 'invalid'
        else:
            raise ParserError("Unknown status `%s`" % status)

    @property
    def available(self):
        return not self.invalid and (self.node('Status') == 'free')

    @property
    def registered(self):
        return not self.invalid and not self.available

    @property
    def updated_on(self):
        if self.node('Changed'):
            return time_parser.parse(self.node('Changed'))

    @property
    def registrar(self):
        raw = self.node('Zone-C')
        if raw:
            return Registrar(id=None, name=raw['name'], organization=raw['organization'], url=None)

    @property
    def registrant_contacts(self):
        return self._build_contact('Holder', Contact.TYPE_REGISTRANT)

    @property
    def admin_contacts(self):
        return self._build_contact('Admin-C', Contact.TYPE_ADMINISTRATIVE)

    @property
    def technical_contacts(self):
        return self._build_contact('Tech-C', Contact.TYPE_TECHNICAL)

    # Nameservers are listed in the following formats:
    #
    #   Nserver:     ns1.prodns.de. 213.160.64.75
    #   Nserver:     ns1.prodns.de.
    #
    @property
    def nameservers(self):
        nameservers = []
        if self.node('Nserver'):
            for line in self.node('Nserver'):
                _tmp = re.split("\s+", line)
                if len(_tmp) == 1:
                    name = _tmp[0]
                    ipv4 = None
                else:
                    name, ipv4 = _tmp    
                nameservers.append(Nameserver(name=name, ipv4=ipv4))

        return nameservers

    # Checks whether the response has been throttled.
    #
    # @return [Boolean]
    #
    # @example
    #   % Error: 55000000002 Connection refused; access control limit reached.
    #
    @property
    def response_throttled(self):
        return bool(self.node("response:throttled"))

    @property
    def response_error(self):
        return bool(self.node("response:error"))

    @property
    def invalid(self):
        return self.node('Status') == 'invalid' or self.response_error

    def _build_contact(self, element, type_):
        raw = self.node(element)
        if raw:
            raw['type'] = type_
            return Contact(**raw)
