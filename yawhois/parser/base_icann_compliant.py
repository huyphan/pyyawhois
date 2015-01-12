from .base_scannable import ScannableParserBase
from ..scanner.base_icann_compliant import BaseIcannCompliantScanner
from ..utils import array_wrapper
from ..record import *
from dateutil import parser as timeparser

class BaseIcannCompliantParser(ScannableParserBase):

    _scanner = BaseIcannCompliantScanner

    @property
    def domain(self):
        if self.node('Domain Name'):
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
        return bool(self.node('status:available'))

    @property
    def registered(self):
        return not self.available

    @property
    def created_on(self):
        value = self.node('Creation Date')
        if value:
            return timeparser.parse(value)
    
    @property
    def updated_on(self):
        value = self.node('Updated Date')
        if value:
            return timeparser.parse(value)

    @property
    def expires_on(self):
        value = self.node('Registrar Registration Expiration Date')
        if value:
            return timeparser.parse(value)

    @property
    def registrar(self):
        value = self.node('Registrar')
        if value:
            return Registrar(self.node('Registrar IANA ID'), self.node('Registrar'), self.node('Registrar'), self.node('Registrar URL'))

    @property
    def registrant_contacts(self):
        return array_wrapper(self._build_contact('Registrant', Contact.TYPE_REGISTRANT))

    @property
    def admin_contacts(self):
        return array_wrapper(self._build_contact('Admin', Contact.TYPE_ADMINISTRATIVE))

    @property
    def technical_contacts(self):
        return array_wrapper(self._build_contact('Tech', Contact.TYPE_TECHNICAL))

    @property
    def nameservers(self):
        return [Nameserver(name = name) for name in filter(None, array_wrapper(self.node("Name Server") or self.node('Name Servers')))]

    def _build_contact(self, element, type_):
        if self.node("%s Name" % element):
            return Contact(**{
                'id'           : self.node("Registry %s ID" % element),
                'type'         : type_,
                'name'         : self._value_for_property(element, 'Name'),
                'organization' : self._value_for_property(element, 'Organization'),
                'address'      : self._value_for_property(element, 'Street'),
                'city'         : self._value_for_property(element, 'City'),
                'zip'          : self._value_for_property(element, 'Postal Code'),
                'state'        : self._value_for_property(element, 'State/Province'),
                'country_code' : self._value_for_property(element, 'Country'),
                'phone'        : self._value_for_property(element, 'Phone'),
                'fax'          : self._value_for_property(element, 'Fax'),
                'email'        : self._value_for_property(element, 'Email')
            })

    def _value_for_phone_property(self, element, prop):
        return " ext: ".join(filter(None,[value_for_property(element, prop), value_for_property(element, prop + " Ext")] ))

    def _value_for_property(self, element, prop):
        return ", ".join(filter(None, array_wrapper(self.node("%s %s" % (element, prop))))) or None
