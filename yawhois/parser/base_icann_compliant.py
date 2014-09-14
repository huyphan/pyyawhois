from .base_scannable import ScannableParserBase
from ..scanner.base_icann_compliant import BaseIcannCompliantScanner
from dateutil import parser

class BaseIcannCompliantParser(ScannableParserBase):

    _scanner = BaseIcannCompliantScanner

    @property
    def domain(self):
        return self.node('Domain Name').lower()

    @property
    def domain_id(self):
        return self.node('Registry Domain ID')

    @property
    def status(self):
        if self.available:
            return 'available'
        else:
            return 'registered'

    @property
    def available(self):
        return bool(self.get('status:available'))

    @property
    def registered(self):
        return not self.available

    @property
    def created_on(self):
        value = self.node('Creation Date')
        if value:
            return parser.parse(value)
    
    @property
    def created_on(self):
        value = self.node('Updated Date')
        if value:
            return parser.parse(value)

    @property
    def expires_on(self):
        value = self.node('Registrar Registration Expiration Date')
        if value:
            return parser.parse(value)

    @property
    def registrar(self):
        value = self.node('Registrar')
        return Registrar(node('Registrar IANA ID'), node('Registrar'), node('Registrar'), node('Registrar URL'))