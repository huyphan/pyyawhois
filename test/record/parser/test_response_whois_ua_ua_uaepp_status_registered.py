
# This file is autogenerated. Do not edit it manually.
# If you want change the content of this file, edit
#
#   spec/fixtures/responses/whois.ua/ua/uaepp/status_registered
#
# and regenerate the tests with the following script
#
#   $ scripts/generate_tests.py
#

from nose.tools import *
from dateutil.parser import parse as time_parse
import yawhois

class TestWhoisUaUaUaeppStatusRegistered(object):

    def setUp(self):
        fixture_path = "spec/fixtures/responses/whois.ua/ua/uaepp/status_registered.txt"
        host         = "whois.ua"
        part         = yawhois.record.Part(open(fixture_path, "r").read(), host)
        self.record  = yawhois.record.Record(None, [part])

    def test_status(self):
        eq_(self.record.status, 'registered')

    def test_available(self):
        eq_(self.record.available, False)

    def test_domain(self):
        eq_(self.record.domain, "google.com.ua")

    def test_nameservers(self):
        eq_(self.record.nameservers.__class__.__name__, 'list')
        eq_(len(self.record.nameservers), 4)
        eq_(self.record.nameservers[0].__class__.__name__, 'Nameserver')
        eq_(self.record.nameservers[0].name, "ns3.google.com")
        eq_(self.record.nameservers[1].__class__.__name__, 'Nameserver')
        eq_(self.record.nameservers[1].name, "ns1.google.com")
        eq_(self.record.nameservers[2].__class__.__name__, 'Nameserver')
        eq_(self.record.nameservers[2].name, "ns4.google.com")
        eq_(self.record.nameservers[3].__class__.__name__, 'Nameserver')
        eq_(self.record.nameservers[3].name, "ns2.google.com")

    def test_admin_contacts(self):
        eq_(self.record.admin_contacts.__class__.__name__, 'list')
        eq_(len(self.record.admin_contacts), 1)
        eq_(self.record.admin_contacts[0].__class__.__name__, 'Contact')
        eq_(self.record.admin_contacts[0].type, yawhois.record.Contact.TYPE_ADMINISTRATIVE)
        eq_(self.record.admin_contacts[0].id, "com-gi8-1")
        eq_(self.record.admin_contacts[0].name, "Google Inc.")
        eq_(self.record.admin_contacts[0].organization, "Google Inc.")
        eq_(self.record.admin_contacts[0].address, "1600 Amphitheatre Parkway Mountain View CA 94043 US")
        eq_(self.record.admin_contacts[0].city, None)
        eq_(self.record.admin_contacts[0].zip, None)
        eq_(self.record.admin_contacts[0].state, None)
        eq_(self.record.admin_contacts[0].country, "UA")
        eq_(self.record.admin_contacts[0].country_code, None)
        eq_(self.record.admin_contacts[0].phone, "+16503300100")
        eq_(self.record.admin_contacts[0].fax, "+16506188571")
        eq_(self.record.admin_contacts[0].email, "dns-admin@google.com")
        eq_(self.record.admin_contacts[0].created_on, time_parse('2013-03-31 19:13:45 +03:00'))
        eq_(self.record.admin_contacts[0].updated_on, None)

    def test_registered(self):
        eq_(self.record.registered, True)

    def test_created_on(self):
        eq_(self.record.created_on.__class__.__name__, 'datetime')
        eq_(self.record.created_on, time_parse('2002-12-04 00:00:00 +02:00'))

    def test_registrar(self):
        assert_raises(yawhois.exceptions.AttributeNotSupported, self.record.registrar)

    def test_registrant_contacts(self):
        eq_(self.record.registrant_contacts.__class__.__name__, 'list')
        eq_(len(self.record.registrant_contacts), 1)
        eq_(self.record.registrant_contacts[0].__class__.__name__, 'Contact')
        eq_(self.record.registrant_contacts[0].type, yawhois.record.Contact.TYPE_ADMINISTRATIVE)
        eq_(self.record.registrant_contacts[0].id, "com-gi8-1")
        eq_(self.record.registrant_contacts[0].name, "Google Inc.")
        eq_(self.record.registrant_contacts[0].organization, "Google Inc.")
        eq_(self.record.registrant_contacts[0].address, "1600 Amphitheatre Parkway Mountain View CA 94043 US")
        eq_(self.record.registrant_contacts[0].city, None)
        eq_(self.record.registrant_contacts[0].zip, None)
        eq_(self.record.registrant_contacts[0].state, None)
        eq_(self.record.registrant_contacts[0].country, "UA")
        eq_(self.record.registrant_contacts[0].country_code, None)
        eq_(self.record.registrant_contacts[0].phone, "+16503300100")
        eq_(self.record.registrant_contacts[0].fax, "+16506188571")
        eq_(self.record.registrant_contacts[0].email, "dns-admin@google.com")
        eq_(self.record.registrant_contacts[0].created_on, time_parse('2013-03-31 19:13:45 +03:00'))
        eq_(self.record.registrant_contacts[0].updated_on, None)

    def test_technical_contacts(self):
        eq_(self.record.technical_contacts.__class__.__name__, 'list')
        eq_(len(self.record.technical_contacts), 1)
        eq_(self.record.technical_contacts[0].__class__.__name__, 'Contact')
        eq_(self.record.technical_contacts[0].type, yawhois.record.Contact.TYPE_TECHNICAL)
        eq_(self.record.technical_contacts[0].id, "com-gi8-1")
        eq_(self.record.technical_contacts[0].name, "Google Inc.")
        eq_(self.record.technical_contacts[0].organization, "Google Inc.")
        eq_(self.record.technical_contacts[0].address, "1600 Amphitheatre Parkway Mountain View CA 94043 US")
        eq_(self.record.technical_contacts[0].city, None)
        eq_(self.record.technical_contacts[0].zip, None)
        eq_(self.record.technical_contacts[0].state, None)
        eq_(self.record.technical_contacts[0].country, "UA")
        eq_(self.record.technical_contacts[0].country_code, None)
        eq_(self.record.technical_contacts[0].phone, "+16503300100")
        eq_(self.record.technical_contacts[0].fax, "+16506188571")
        eq_(self.record.technical_contacts[0].email, "dns-admin@google.com")
        eq_(self.record.technical_contacts[0].created_on, time_parse('2013-03-31 19:13:45 +03:00'))
        eq_(self.record.technical_contacts[0].updated_on, None)

    def test_updated_on(self):
        eq_(self.record.updated_on.__class__.__name__, 'datetime')
        eq_(self.record.updated_on, time_parse('2013-04-15 20:00:10 +03:00'))

    def test_domain_id(self):
        assert_raises(yawhois.exceptions.AttributeNotSupported, self.record.domain_id)

    def test_expires_on(self):
        eq_(self.record.expires_on.__class__.__name__, 'datetime')
        eq_(self.record.expires_on, time_parse('2013-12-04 00:00:00 +02:00'))
