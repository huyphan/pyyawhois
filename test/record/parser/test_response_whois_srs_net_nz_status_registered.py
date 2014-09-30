
# This file is autogenerated. Do not edit it manually.
# If you want change the content of this file, edit
#
#   spec/fixtures/responses/whois.srs.net.nz/status_registered
#
# and regenerate the tests with the following script
#
#   $ scripts/generate_tests.py
#

from nose.tools import *
from dateutil.parser import parse as time_parse
import yawhois

class TestWhoisSrsNetNzStatusRegistered(object):

    def setUp(self):
        fixture_path = "spec/fixtures/responses/whois.srs.net.nz/status_registered.txt"
        host         = "whois.srs.net.nz"
        part         = yawhois.record.Part(open(fixture_path, "r").read(), host)
        self.record  = yawhois.record.Record(None, [part])

    def test_status(self):
        eq_(self.record.status, 'registered')

    def test_available(self):
        eq_(self.record.available, False)

    def test_domain(self):
        eq_(self.record.domain, "google.co.nz")

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
        eq_(self.record.admin_contacts[0].id, None)
        eq_(self.record.admin_contacts[0].name, "Google Inc")
        eq_(self.record.admin_contacts[0].organization, None)
        eq_(self.record.admin_contacts[0].address, "1600 Amphitheatre Parkway")
        eq_(self.record.admin_contacts[0].city, "Mountain View")
        eq_(self.record.admin_contacts[0].zip, "94043")
        eq_(self.record.admin_contacts[0].state, "CA")
        eq_(self.record.admin_contacts[0].country, "US (UNITED STATES)")
        eq_(self.record.admin_contacts[0].country_code, None)
        eq_(self.record.admin_contacts[0].phone, "+1 650 +1 650 3300100")
        eq_(self.record.admin_contacts[0].fax, "+1 650 +1 650 6181434")
        eq_(self.record.admin_contacts[0].email, "dns-admin@google.com")
        eq_(self.record.admin_contacts[0].created_on, None)
        eq_(self.record.admin_contacts[0].updated_on, None)

    def test_registered(self):
        eq_(self.record.registered, True)

    def test_response_throttled(self):
        eq_(self.record.response_throttled, False)

    def test_created_on(self):
        eq_(self.record.created_on.__class__.__name__, 'datetime')
        eq_(self.record.created_on, time_parse('1999-02-17 00:00:00 +13:00'))

    def test_registrar(self):
        eq_(self.record.registrar.__class__.__name__, 'Registrar')
        eq_(self.record.registrar.id, None)
        eq_(self.record.registrar.name, "MarkMonitor")
        eq_(self.record.registrar.organization, None)
        eq_(self.record.registrar.url, None)

    def test_registrant_contacts(self):
        eq_(self.record.registrant_contacts.__class__.__name__, 'list')
        eq_(len(self.record.registrant_contacts), 1)
        eq_(self.record.registrant_contacts[0].__class__.__name__, 'Contact')
        eq_(self.record.registrant_contacts[0].type, yawhois.record.Contact.TYPE_REGISTRANT)
        eq_(self.record.registrant_contacts[0].id, None)
        eq_(self.record.registrant_contacts[0].name, "Google Inc")
        eq_(self.record.registrant_contacts[0].organization, None)
        eq_(self.record.registrant_contacts[0].address, "1600 Amphitheatre Parkway")
        eq_(self.record.registrant_contacts[0].city, "Mountain View")
        eq_(self.record.registrant_contacts[0].zip, "94043")
        eq_(self.record.registrant_contacts[0].state, "CA")
        eq_(self.record.registrant_contacts[0].country, "US (UNITED STATES)")
        eq_(self.record.registrant_contacts[0].country_code, None)
        eq_(self.record.registrant_contacts[0].phone, "+1 650 +1 650 3300100")
        eq_(self.record.registrant_contacts[0].fax, "+1 650 +1 650 6181434")
        eq_(self.record.registrant_contacts[0].email, "dns-admin@google.com")
        eq_(self.record.registrant_contacts[0].created_on, None)
        eq_(self.record.registrant_contacts[0].updated_on, None)

    def test_technical_contacts(self):
        eq_(self.record.technical_contacts.__class__.__name__, 'list')
        eq_(len(self.record.technical_contacts), 1)
        eq_(self.record.technical_contacts[0].__class__.__name__, 'Contact')
        eq_(self.record.technical_contacts[0].type, yawhois.record.Contact.TYPE_TECHNICAL)
        eq_(self.record.technical_contacts[0].id, None)
        eq_(self.record.technical_contacts[0].name, "Google Inc")
        eq_(self.record.technical_contacts[0].organization, None)
        eq_(self.record.technical_contacts[0].address, "1600 Amphitheatre Parkway")
        eq_(self.record.technical_contacts[0].city, "Mountain View")
        eq_(self.record.technical_contacts[0].zip, "94043")
        eq_(self.record.technical_contacts[0].state, "CA")
        eq_(self.record.technical_contacts[0].country, "US (UNITED STATES)")
        eq_(self.record.technical_contacts[0].country_code, None)
        eq_(self.record.technical_contacts[0].phone, "+1 650 +1 650 3300100")
        eq_(self.record.technical_contacts[0].fax, "+  +1 650 6181434")
        eq_(self.record.technical_contacts[0].email, "dns-admin@google.com")
        eq_(self.record.technical_contacts[0].created_on, None)
        eq_(self.record.technical_contacts[0].updated_on, None)

    def test_updated_on(self):
        eq_(self.record.updated_on.__class__.__name__, 'datetime')
        eq_(self.record.updated_on, time_parse('2013-01-16 23:20:24 +13:00'))

    def test_domain_id(self):
        assert_raises(yawhois.exceptions.AttributeNotSupported, self.record.domain_id)

    def test_expires_on(self):
        eq_(self.record.expires_on.__class__.__name__, 'datetime')
        eq_(self.record.expires_on, time_parse('2014-02-17 00:00:00 +13:00'))