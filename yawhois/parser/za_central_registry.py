from .base_icann_compliant import BaseIcannCompliantParser
from ..record import Contact
from ..record import Registrar
from dateutil import parser as time_parser

class ZaCentralRegistryParser(BaseIcannCompliantParser):

    @property
    def domain_id(self):
        return self.node('Domain ID')

    @property
    def expires_on(self):
        if self.node('Registry Expiry Date'):
            return time_parser.parse(self.node('Registry Expiry Date'))

    @property
    def registrar(self):
        if self.node("Sponsoring Registrar"):
            return Registrar(
                id = self.node('Sponsoring Registrar IANA ID'),
                name = self.node('Sponsoring Registrar'),
                organization = self.node('Sponsoring Registrar'),
            )

    @property
    def available(self):
        return not bool(self.node("Creation Date"))

    def _build_contact(self, element, type_):
        if self.node("%s Name" % element):
            return Contact(**{
                'type':         type_,
                'id':           self.node("%s ID" % element),
                'name':         self._value_for_property(element, 'Name'),
                'organization': self._value_for_property(element, 'Organization'),
                'address':      self._value_for_property(element, 'Street'),
                'city':         self._value_for_property(element, 'City'),
                'zip':          self._value_for_property(element, 'Postal Code'),
                'state':        self._value_for_property(element, 'State/Province'),
                'country_code': self._value_for_property(element, 'Country'),
                'phone':        self._value_for_phone_property(element, 'Phone'),
                'fax':          self._value_for_property(element, 'Fax'),
                'email':        self._value_for_property(element, 'Email')
            })
