
# This file is autogenerated. Do not edit it manually.
# If you want change the content of this file, edit
#
#   spec/fixtures/responses/whois.dns.lu/status_registered
#
# and regenerate the tests with the following script
#
#   $ scripts/generate_tests.py
#

from nose.tools import *
from dateutil.parser import parse as time_parse
import yawhois

class TestWhoisDnsLuStatusRegistered(object):

    def setUp(self):
        fixture_path = "spec/fixtures/responses/whois.dns.lu/status_registered.txt"
        host         = "whois.dns.lu"
        part         = yawhois.record.Part(open(fixture_path, "r").read(), host)
        self.record  = yawhois.record.Record(None, [part])

    def test_status(self):
        eq_(self.record.status, 'registered')

    def test_available(self):
        eq_(self.record.available, False)

    def test_nameservers(self):
        eq_(self.record.nameservers.__class__.__name__, 'list')
        eq_(len(self.record.nameservers), 4)
        eq_(self.record.nameservers[0].__class__.__name__, 'Nameserver')
        eq_(self.record.nameservers[0].name, "ns1.google.com")
        eq_(self.record.nameservers[1].__class__.__name__, 'Nameserver')
        eq_(self.record.nameservers[1].name, "ns2.google.com")
        eq_(self.record.nameservers[2].__class__.__name__, 'Nameserver')
        eq_(self.record.nameservers[2].name, "ns3.google.com")
        eq_(self.record.nameservers[3].__class__.__name__, 'Nameserver')
        eq_(self.record.nameservers[3].name, "ns4.google.com")

    def test_admin_contacts(self):
        eq_(self.record.admin_contacts.__class__.__name__, 'list')
        eq_(len(self.record.admin_contacts), 1)
        eq_(self.record.admin_contacts[0].__class__.__name__, 'Contact')
        eq_(self.record.admin_contacts[0].type, yawhois.record.Contact.TYPE_ADMINISTRATIVE)
        eq_(self.record.admin_contacts[0].name, "DNS Admin")
        eq_(self.record.admin_contacts[0].address, "Google Inc., 1600 Amphitheatre Parkway")
        eq_(self.record.admin_contacts[0].city, "Mountain View")
        eq_(self.record.admin_contacts[0].zip, "94043")
        eq_(self.record.admin_contacts[0].country_code, "US")
        eq_(self.record.admin_contacts[0].email, "dns-admin@google.com")

    def test_registered(self):
        eq_(self.record.registered, True)

    def test_created_on(self):
        eq_(self.record.created_on.__class__.__name__, 'datetime')
        eq_(self.record.created_on, time_parse('2003-06-04 00:00:00 UTC'))

    def test_registrar(self):
        eq_(self.record.registrar.__class__.__name__, 'Registrar')
        eq_(self.record.registrar.name, "Markmonitor")
        eq_(self.record.registrar.url, "http://www.markmonitor.com/")

    def test_registrant_contacts(self):
        eq_(self.record.registrant_contacts.__class__.__name__, 'list')
        eq_(len(self.record.registrant_contacts), 1)
        eq_(self.record.registrant_contacts[0].__class__.__name__, 'Contact')
        eq_(self.record.registrant_contacts[0].type, yawhois.record.Contact.TYPE_REGISTRANT)
        eq_(self.record.registrant_contacts[0].name, "Google Inc.")
        eq_(self.record.registrant_contacts[0].address, "1600 Amphitheatre Parkway")
        eq_(self.record.registrant_contacts[0].city, "Mountain View")
        eq_(self.record.registrant_contacts[0].zip, "94043")
        eq_(self.record.registrant_contacts[0].country_code, "US")

    def test_technical_contacts(self):
        eq_(self.record.technical_contacts.__class__.__name__, 'list')
        eq_(len(self.record.technical_contacts), 1)
        eq_(self.record.technical_contacts[0].__class__.__name__, 'Contact')
        eq_(self.record.technical_contacts[0].type, yawhois.record.Contact.TYPE_TECHNICAL)
        eq_(self.record.technical_contacts[0].name, "DNS Admin")
        eq_(self.record.technical_contacts[0].address, "Google Inc., 1600 Amphitheatre Parkway")
        eq_(self.record.technical_contacts[0].city, "Mountain View")
        eq_(self.record.technical_contacts[0].zip, "94043")
        eq_(self.record.technical_contacts[0].country_code, "US")
        eq_(self.record.technical_contacts[0].email, "dns-admin@google.com")

    def test_updated_on(self):
        assert_raises(yawhois.exceptions.AttributeNotSupported, self.record.updated_on)

    def test_expires_on(self):
        assert_raises(yawhois.exceptions.AttributeNotSupported, self.record.expires_on)
