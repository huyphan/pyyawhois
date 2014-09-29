
# This file is autogenerated. Do not edit it manually.
# If you want change the content of this file, edit
#
#   spec/fixtures/responses/whois.registry.om/status_registered
#
# and regenerate the tests with the following script
#
#   $ scripts/generate_tests.py
#

from nose.tools import *
from dateutil.parser import parse as time_parse
import yawhois

class TestWhoisRegistryOmStatusRegistered(object):

    def setUp(self):
        fixture_path = "spec/fixtures/responses/whois.registry.om/status_registered.txt"
        host         = "whois.registry.om"
        part         = yawhois.record.Part(open(fixture_path, "r").read(), host)
        self.record  = yawhois.record.Record(None, [part])

    def test_status(self):
        eq_(self.record.status, ["ok"])

    def test_available(self):
        eq_(self.record.available, False)

    def test_domain(self):
        eq_(self.record.domain, "rop.gov.om")

    def test_nameservers(self):
        eq_(self.record.nameservers.__class__.__name__, 'list')
        eq_(len(self.record.nameservers), 3)
        eq_(self.record.nameservers[0].__class__.__name__, 'Nameserver')
        eq_(self.record.nameservers[0].name, "ns3.omantel.net.om")
        eq_(self.record.nameservers[0].ipv4, "62.231.247.70")
        eq_(self.record.nameservers[0].ipv6, None)
        eq_(self.record.nameservers[1].__class__.__name__, 'Nameserver')
        eq_(self.record.nameservers[1].name, "ns1.omantel.net.om")
        eq_(self.record.nameservers[1].ipv4, "82.178.72.21")
        eq_(self.record.nameservers[1].ipv6, None)
        eq_(self.record.nameservers[2].__class__.__name__, 'Nameserver')
        eq_(self.record.nameservers[2].name, "ns2.omantel.net.om")
        eq_(self.record.nameservers[2].ipv4, "212.72.4.147")
        eq_(self.record.nameservers[2].ipv6, None)

    def test_admin_contacts(self):
        assert_raises(yawhois.exceptions.AttributeNotSupported, self.record.admin_contacts)

    def test_registered(self):
        eq_(self.record.registered, True)

    def test_created_on(self):
        assert_raises(yawhois.exceptions.AttributeNotSupported, self.record.created_on)

    def test_registrar(self):
        eq_(self.record.registrar.__class__.__name__, 'Registrar')
        eq_(self.record.registrar.id, None)
        eq_(self.record.registrar.name, "Oman Telecommunication Company")
        eq_(self.record.registrar.organization, "Oman Telecommunication Company")
        eq_(self.record.registrar.url, None)

    def test_registrant_contacts(self):
        eq_(self.record.registrant_contacts.__class__.__name__, 'list')
        eq_(len(self.record.registrant_contacts), 1)
        eq_(self.record.registrant_contacts[0].__class__.__name__, 'Contact')
        eq_(self.record.registrant_contacts[0].type, yawhois.record.Contact.TYPE_REGISTRANT)
        eq_(self.record.registrant_contacts[0].id, "10084244")
        eq_(self.record.registrant_contacts[0].name, "Nasser Said Al Daree")
        eq_(self.record.registrant_contacts[0].organization, None)
        eq_(self.record.registrant_contacts[0].address, None)
        eq_(self.record.registrant_contacts[0].city, None)
        eq_(self.record.registrant_contacts[0].zip, None)
        eq_(self.record.registrant_contacts[0].state, None)
        eq_(self.record.registrant_contacts[0].country, None)
        eq_(self.record.registrant_contacts[0].country_code, None)
        eq_(self.record.registrant_contacts[0].phone, None)
        eq_(self.record.registrant_contacts[0].fax, None)
        eq_(self.record.registrant_contacts[0].email, "Visit portal.registry.om/whois for Web based WhoIs")

    def test_technical_contacts(self):
        eq_(self.record.technical_contacts.__class__.__name__, 'list')
        eq_(len(self.record.technical_contacts), 1)
        eq_(self.record.technical_contacts[0].__class__.__name__, 'Contact')
        eq_(self.record.technical_contacts[0].type, yawhois.record.Contact.TYPE_TECHNICAL)
        eq_(self.record.technical_contacts[0].id, "10084244")
        eq_(self.record.technical_contacts[0].name, "Nasser Said Al Daree")
        eq_(self.record.technical_contacts[0].organization, None)
        eq_(self.record.technical_contacts[0].address, None)
        eq_(self.record.technical_contacts[0].city, None)
        eq_(self.record.technical_contacts[0].zip, None)
        eq_(self.record.technical_contacts[0].state, None)
        eq_(self.record.technical_contacts[0].country, None)
        eq_(self.record.technical_contacts[0].country_code, None)
        eq_(self.record.technical_contacts[0].phone, None)
        eq_(self.record.technical_contacts[0].fax, None)
        eq_(self.record.technical_contacts[0].email, "Visit portal.registry.om/whois for Web based WhoIs")

    def test_updated_on(self):
        eq_(self.record.updated_on.__class__.__name__, 'datetime')
        eq_(self.record.updated_on, time_parse('2013-10-06 18:20:12 UTC'))

    def test_domain_id(self):
        assert_raises(yawhois.exceptions.AttributeNotSupported, self.record.domain_id)

    def test_expires_on(self):
        assert_raises(yawhois.exceptions.AttributeNotSupported, self.record.expires_on)

    def test_disclaimer(self):
        assert_raises(yawhois.exceptions.AttributeNotSupported, self.record.disclaimer)
