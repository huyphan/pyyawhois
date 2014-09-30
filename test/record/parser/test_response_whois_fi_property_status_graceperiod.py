
# This file is autogenerated. Do not edit it manually.
# If you want change the content of this file, edit
#
#   spec/fixtures/responses/whois.fi/property_status_graceperiod
#
# and regenerate the tests with the following script
#
#   $ scripts/generate_tests.py
#

from nose.tools import *
from dateutil.parser import parse as time_parse
import yawhois

class TestWhoisFiPropertyStatusGraceperiod(object):

    def setUp(self):
        fixture_path = "spec/fixtures/responses/whois.fi/property_status_graceperiod.txt"
        host         = "whois.fi"
        part         = yawhois.record.Part(open(fixture_path, "r").read(), host)
        self.record  = yawhois.record.Record(None, [part])

    def test_status(self):
        eq_(self.record.status, 'registered')

    def test_available(self):
        eq_(self.record.available, False)

    def test_domain(self):
        eq_(self.record.domain, "oogle.fi")

    def test_nameservers(self):
        eq_(self.record.nameservers.__class__.__name__, 'list')
        eq_(len(self.record.nameservers), 2)
        eq_(self.record.nameservers[0].__class__.__name__, 'Nameserver')
        eq_(self.record.nameservers[0].name, "a.ns.netim.net")
        eq_(self.record.nameservers[1].__class__.__name__, 'Nameserver')
        eq_(self.record.nameservers[1].name, "b.ns.netim.net")

    def test_admin_contacts(self):
        assert_raises(yawhois.exceptions.AttributeNotSupported, self.record.admin_contacts)

    def test_registered(self):
        eq_(self.record.registered, True)

    def test_created_on(self):
        eq_(self.record.created_on.__class__.__name__, 'datetime')
        eq_(self.record.created_on, time_parse('2012-06-21'))

    def test_registrar(self):
        assert_raises(yawhois.exceptions.AttributeNotSupported, self.record.registrar)

    def test_registrant_contacts(self):
        eq_(self.record.registrant_contacts.__class__.__name__, 'list')
        eq_(len(self.record.registrant_contacts), 1)
        eq_(self.record.registrant_contacts[0].__class__.__name__, 'Contact')
        eq_(self.record.registrant_contacts[0].type, yawhois.record.Contact.TYPE_REGISTRANT)
        eq_(self.record.registrant_contacts[0].id, "NURMI")
        eq_(self.record.registrant_contacts[0].name, "-")
        eq_(self.record.registrant_contacts[0].organization, "Minna")
        eq_(self.record.registrant_contacts[0].address, "Huovitie 3")
        eq_(self.record.registrant_contacts[0].city, "HELSINKI")
        eq_(self.record.registrant_contacts[0].zip, "00400")
        eq_(self.record.registrant_contacts[0].state, None)
        eq_(self.record.registrant_contacts[0].country, None)
        eq_(self.record.registrant_contacts[0].country_code, None)
        eq_(self.record.registrant_contacts[0].phone, "+358201599789")
        eq_(self.record.registrant_contacts[0].fax, None)
        eq_(self.record.registrant_contacts[0].email, None)
        eq_(self.record.registrant_contacts[0].created_on, None)
        eq_(self.record.registrant_contacts[0].updated_on, None)

    def test_technical_contacts(self):
        assert_raises(yawhois.exceptions.AttributeNotSupported, self.record.technical_contacts)

    def test_updated_on(self):
        eq_(self.record.updated_on.__class__.__name__, 'datetime')
        eq_(self.record.updated_on, time_parse('2013-06-22'))

    def test_domain_id(self):
        assert_raises(yawhois.exceptions.AttributeNotSupported, self.record.domain_id)

    def test_expires_on(self):
        eq_(self.record.expires_on.__class__.__name__, 'datetime')
        eq_(self.record.expires_on, time_parse('2013-06-21'))

    def test_disclaimer(self):
        eq_(self.record.disclaimer, "More information is available at https://domain.fi/\nCopyright (c) Finnish Communications Regulatory Authority")