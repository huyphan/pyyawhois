
# This file is autogenerated. Do not edit it manually.
# If you want change the content of this file, edit
#
#   spec/fixtures/responses/whois.ati.tn/status_registered
#
# and regenerate the tests with the following script
#
#   $ scripts/generate_tests.py
#

from nose.tools import *
from dateutil.parser import parse as time_parse
import yawhois

class TestWhoisAtiTnStatusRegistered(object):

    def setUp(self):
        fixture_path = "spec/fixtures/responses/whois.ati.tn/status_registered.txt"
        host         = "whois.ati.tn"
        part         = yawhois.record.Part(open(fixture_path, "r").read(), host)
        self.record  = yawhois.record.Record(None, [part])

    def test_status(self):
        eq_(self.record.status, 'registered')

    def test_available(self):
        eq_(self.record.available, False)

    def test_domain(self):
        eq_(self.record.domain, "google.tn")

    def test_nameservers(self):
        eq_(self.record.nameservers.__class__.__name__, 'list')
        eq_(len(self.record.nameservers), 4)
        eq_(self.record.nameservers[0].__class__.__name__, 'Nameserver')
        eq_(self.record.nameservers[0].name, "ns1.google.com")
        eq_(self.record.nameservers[0].ipv4, "216.239.32.10")
        eq_(self.record.nameservers[1].__class__.__name__, 'Nameserver')
        eq_(self.record.nameservers[1].name, "ns2.google.com")
        eq_(self.record.nameservers[1].ipv4, "216.239.34.10")
        eq_(self.record.nameservers[2].__class__.__name__, 'Nameserver')
        eq_(self.record.nameservers[2].name, "ns3.google.com")
        eq_(self.record.nameservers[2].ipv4, "216.239.36.10")
        eq_(self.record.nameservers[3].__class__.__name__, 'Nameserver')
        eq_(self.record.nameservers[3].name, "ns4.google.com")
        eq_(self.record.nameservers[3].ipv4, "216.239.38.10")

    def test_admin_contacts(self):
        eq_(self.record.admin_contacts.__class__.__name__, 'list')
        eq_(len(self.record.admin_contacts), 1)
        eq_(self.record.admin_contacts[0].__class__.__name__, 'Contact')
        eq_(self.record.admin_contacts[0].type, yawhois.record.Contact.TYPE_ADMINISTRATIVE)
        eq_(self.record.admin_contacts[0].id, None)
        eq_(self.record.admin_contacts[0].name, "GOOGLE Inc")
        eq_(self.record.admin_contacts[0].organization, None)
        eq_(self.record.admin_contacts[0].address, "PO BOX 2050 Moutain view CA 94042 USA")
        eq_(self.record.admin_contacts[0].city, None)
        eq_(self.record.admin_contacts[0].zip, None)
        eq_(self.record.admin_contacts[0].state, None)
        eq_(self.record.admin_contacts[0].country, None)
        eq_(self.record.admin_contacts[0].country_code, None)
        eq_(self.record.admin_contacts[0].phone, "+1 925 685 9600")
        eq_(self.record.admin_contacts[0].fax, "+1 925 685 9620")
        eq_(self.record.admin_contacts[0].email, "dns-admin@google.com")
        eq_(self.record.admin_contacts[0].created_on, time_parse('2009-05-14 00:00:00'))
        eq_(self.record.admin_contacts[0].updated_on, time_parse('2010-07-18 00:00:00'))

    def test_registered(self):
        eq_(self.record.registered, True)

    def test_created_on(self):
        eq_(self.record.created_on.__class__.__name__, 'datetime')
        eq_(self.record.created_on, time_parse('2009-05-14 00:00:00'))

    def test_registrar(self):
        eq_(self.record.registrar.__class__.__name__, 'Registrar')
        eq_(self.record.registrar.id, None)
        eq_(self.record.registrar.name, "3S Global Net")
        eq_(self.record.registrar.organization, None)
        eq_(self.record.registrar.url, None)

    def test_registrant_contacts(self):
        eq_(self.record.registrant_contacts.__class__.__name__, 'list')
        eq_(len(self.record.registrant_contacts), 1)
        eq_(self.record.registrant_contacts[0].__class__.__name__, 'Contact')
        eq_(self.record.registrant_contacts[0].type, yawhois.record.Contact.TYPE_REGISTRANT)
        eq_(self.record.registrant_contacts[0].id, None)
        eq_(self.record.registrant_contacts[0].name, "GOOGLE Inc")
        eq_(self.record.registrant_contacts[0].organization, None)
        eq_(self.record.registrant_contacts[0].address, "PO BOX 2050 Moutain view CA 94042 USA")
        eq_(self.record.registrant_contacts[0].city, None)
        eq_(self.record.registrant_contacts[0].zip, None)
        eq_(self.record.registrant_contacts[0].state, None)
        eq_(self.record.registrant_contacts[0].country, None)
        eq_(self.record.registrant_contacts[0].country_code, None)
        eq_(self.record.registrant_contacts[0].phone, "+1 925 685 9600")
        eq_(self.record.registrant_contacts[0].fax, "+1 925 685 9620")
        eq_(self.record.registrant_contacts[0].email, "dns-admin@google.com")
        eq_(self.record.registrant_contacts[0].created_on, time_parse('2009-05-14 00:00:00'))
        eq_(self.record.registrant_contacts[0].updated_on, time_parse('2010-07-18 00:00:00'))

    def test_technical_contacts(self):
        eq_(self.record.technical_contacts.__class__.__name__, 'list')
        eq_(len(self.record.technical_contacts), 1)
        eq_(self.record.technical_contacts[0].__class__.__name__, 'Contact')
        eq_(self.record.technical_contacts[0].type, yawhois.record.Contact.TYPE_TECHNICAL)
        eq_(self.record.technical_contacts[0].id, None)
        eq_(self.record.technical_contacts[0].name, "GOOGLE Inc")
        eq_(self.record.technical_contacts[0].organization, None)
        eq_(self.record.technical_contacts[0].address, "PO BOX 2050 Moutain view CA 94042 USA")
        eq_(self.record.technical_contacts[0].city, None)
        eq_(self.record.technical_contacts[0].zip, None)
        eq_(self.record.technical_contacts[0].state, None)
        eq_(self.record.technical_contacts[0].country, None)
        eq_(self.record.technical_contacts[0].country_code, None)
        eq_(self.record.technical_contacts[0].phone, "+1 925 685 9600")
        eq_(self.record.technical_contacts[0].fax, "+1 925 685 9620")
        eq_(self.record.technical_contacts[0].email, "dns-admin@google.com")
        eq_(self.record.technical_contacts[0].created_on, time_parse('2009-05-14 00:00:00'))
        eq_(self.record.technical_contacts[0].updated_on, time_parse('2010-07-18 00:00:00'))

    def test_updated_on(self):
        assert_raises(yawhois.exceptions.AttributeNotSupported, self.record.updated_on)

    def test_domain_id(self):
        assert_raises(yawhois.exceptions.AttributeNotSupported, self.record.domain_id)

    def test_expires_on(self):
        assert_raises(yawhois.exceptions.AttributeNotSupported, self.record.expires_on)

    def test_disclaimer(self):
        eq_(self.record.disclaimer, "All rights reserved.\nCopyright \"Tunisian Internet Agency - http://whois.tn\"")