
# This file is autogenerated. Do not edit it manually.
# If you want change the content of this file, edit
#
#   spec/fixtures/responses/whois.nic.io/status_registered
#
# and regenerate the tests with the following script
#
#   $ scripts/generate_tests.py
#

from nose.tools import *
from dateutil.parser import parse as time_parse
import yawhois

class TestWhoisNicIoStatusRegistered(object):

    def setUp(self):
        fixture_path = "spec/fixtures/responses/whois.nic.io/status_registered.txt"
        host         = "whois.nic.io"
        part         = yawhois.record.Part(open(fixture_path, "r").read(), host)
        self.record  = yawhois.record.Record(None, [part])

    def test_status(self):
        eq_(self.record.status, 'registered')

    def test_available(self):
        eq_(self.record.available, False)

    def test_domain(self):
        eq_(self.record.domain, "redis.io")

    def test_reserved(self):
        eq_(self.record.reserved, False)

    def test_nameservers(self):
        eq_(self.record.nameservers.__class__.__name__, 'list')
        eq_(len(self.record.nameservers), 4)
        eq_(self.record.nameservers[0].__class__.__name__, 'Nameserver')
        eq_(self.record.nameservers[0].name, "ns1.iwantmyname.net")
        eq_(self.record.nameservers[1].__class__.__name__, 'Nameserver')
        eq_(self.record.nameservers[1].name, "ns2.iwantmyname.net")
        eq_(self.record.nameservers[2].__class__.__name__, 'Nameserver')
        eq_(self.record.nameservers[2].name, "ns3.iwantmyname.net")
        eq_(self.record.nameservers[3].__class__.__name__, 'Nameserver')
        eq_(self.record.nameservers[3].name, "ns4.iwantmyname.net")

    def test_admin_contacts(self):
        assert_raises(yawhois.exceptions.AttributeNotSupported, self.record.admin_contacts)

    def test_registered(self):
        eq_(self.record.registered, True)

    def test_created_on(self):
        assert_raises(yawhois.exceptions.AttributeNotSupported, self.record.created_on)

    def test_registrar(self):
        assert_raises(yawhois.exceptions.AttributeNotSupported, self.record.registrar)

    def test_registrant_contacts(self):
        eq_(self.record.registrant_contacts.__class__.__name__, 'list')
        eq_(len(self.record.registrant_contacts), 1)
        eq_(self.record.registrant_contacts[0].__class__.__name__, 'Contact')
        eq_(self.record.registrant_contacts[0].type, yawhois.record.Contact.TYPE_REGISTRANT)
        eq_(self.record.registrant_contacts[0].id, None)
        eq_(self.record.registrant_contacts[0].name, "Salvatore Sanfilippo")
        eq_(self.record.registrant_contacts[0].organization, "Salvatore Sanfilippo")
        eq_(self.record.registrant_contacts[0].address, "Via F.Alaimo, 2")
        eq_(self.record.registrant_contacts[0].city, "Campobello di Licata (AG")
        eq_(self.record.registrant_contacts[0].zip, None)
        eq_(self.record.registrant_contacts[0].state, ".")
        eq_(self.record.registrant_contacts[0].country, "IT")
        eq_(self.record.registrant_contacts[0].country_code, None)
        eq_(self.record.registrant_contacts[0].phone, None)
        eq_(self.record.registrant_contacts[0].fax, None)
        eq_(self.record.registrant_contacts[0].email, None)
        eq_(self.record.registrant_contacts[0].created_on, None)
        eq_(self.record.registrant_contacts[0].updated_on, None)

    def test_technical_contacts(self):
        assert_raises(yawhois.exceptions.AttributeNotSupported, self.record.technical_contacts)

    def test_updated_on(self):
        assert_raises(yawhois.exceptions.AttributeNotSupported, self.record.updated_on)

    def test_domain_id(self):
        assert_raises(yawhois.exceptions.AttributeNotSupported, self.record.domain_id)

    def test_expires_on(self):
        eq_(self.record.expires_on.__class__.__name__, 'datetime')
        eq_(self.record.expires_on, time_parse('2014-05-28'))

    def test_disclaimer(self):
        assert_raises(yawhois.exceptions.AttributeNotSupported, self.record.disclaimer)
