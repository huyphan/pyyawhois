
# This file is autogenerated. Do not edit it manually.
# If you want change the content of this file, edit
#
#   spec/fixtures/responses/whois.dreamhost.com/status_registered
#
# and regenerate the tests with the following script
#
#   $ scripts/generate_tests.py
#

from nose.tools import *
from dateutil.parser import parse as time_parse
import yawhois

class TestWhoisDreamhostComStatusRegistered(object):

    def setUp(self):
        fixture_path = "spec/fixtures/responses/whois.dreamhost.com/status_registered.txt"
        host         = "whois.dreamhost.com"
        part         = yawhois.record.Part(open(fixture_path, "r").read(), host)
        self.record  = yawhois.record.Record(None, [part])

    def test_status(self):
        eq_(self.record.status, 'registered')

    def test_available(self):
        eq_(self.record.available, False)

    def test_nameservers(self):
        eq_(self.record.nameservers.__class__.__name__, 'list')
        eq_(len(self.record.nameservers), 3)
        eq_(self.record.nameservers[0].__class__.__name__, 'Nameserver')
        eq_(self.record.nameservers[0].name, "ns1.dreamhost.com")
        eq_(self.record.nameservers[1].__class__.__name__, 'Nameserver')
        eq_(self.record.nameservers[1].name, "ns2.dreamhost.com")
        eq_(self.record.nameservers[2].__class__.__name__, 'Nameserver')
        eq_(self.record.nameservers[2].name, "ns3.dreamhost.com")

    def test_admin_contacts(self):
        eq_(self.record.admin_contacts.__class__.__name__, 'list')
        eq_(len(self.record.admin_contacts), 1)
        eq_(self.record.admin_contacts[0].__class__.__name__, 'Contact')
        eq_(self.record.admin_contacts[0].type, yawhois.record.Contact.TYPE_ADMINISTRATIVE)
        eq_(self.record.admin_contacts[0].name, "PRIVATE REGISTRANT")
        eq_(self.record.admin_contacts[0].organization, "A HAPPY DREAMHOST CUSTOMER")
        eq_(self.record.admin_contacts[0].address, "417 ASSOCIATED RD #324, C/O DREAMHOST.COM")
        eq_(self.record.admin_contacts[0].city, "BREA")
        eq_(self.record.admin_contacts[0].zip, "92821")
        eq_(self.record.admin_contacts[0].state, "CA")
        eq_(self.record.admin_contacts[0].country_code, "US")
        eq_(self.record.admin_contacts[0].phone, "+1.7147064182")
        eq_(self.record.admin_contacts[0].fax, None)
        eq_(self.record.admin_contacts[0].email, "YW3GAZMC77BTMTF@PROXY.DREAMHOST.COM")

    def test_registered(self):
        eq_(self.record.registered, True)

    def test_created_on(self):
        eq_(self.record.created_on.__class__.__name__, 'datetime')
        eq_(self.record.created_on, time_parse('1997-09-22 21:00:00 UTC'))

    def test_registrar(self):
        eq_(self.record.registrar.__class__.__name__, 'Registrar')
        eq_(self.record.registrar.id, "431")
        eq_(self.record.registrar.name, "DREAMHOST")
        eq_(self.record.registrar.organization, "DREAMHOST")
        eq_(self.record.registrar.url, "www.dreamhost.com")

    def test_registrant_contacts(self):
        eq_(self.record.registrant_contacts.__class__.__name__, 'list')
        eq_(len(self.record.registrant_contacts), 1)
        eq_(self.record.registrant_contacts[0].__class__.__name__, 'Contact')
        eq_(self.record.registrant_contacts[0].type, yawhois.record.Contact.TYPE_REGISTRANT)
        eq_(self.record.registrant_contacts[0].name, "PRIVATE REGISTRANT")
        eq_(self.record.registrant_contacts[0].organization, "A HAPPY DREAMHOST CUSTOMER")
        eq_(self.record.registrant_contacts[0].address, "417 ASSOCIATED RD #324, C/O DREAMHOST.COM")
        eq_(self.record.registrant_contacts[0].city, "BREA")
        eq_(self.record.registrant_contacts[0].zip, "92821")
        eq_(self.record.registrant_contacts[0].state, "CA")
        eq_(self.record.registrant_contacts[0].country_code, "US")
        eq_(self.record.registrant_contacts[0].phone, "+1.7147064182")
        eq_(self.record.registrant_contacts[0].fax, None)
        eq_(self.record.registrant_contacts[0].email, "YW3GAZMC77BTMTF@PROXY.DREAMHOST.COM")

    def test_technical_contacts(self):
        eq_(self.record.technical_contacts.__class__.__name__, 'list')
        eq_(len(self.record.technical_contacts), 1)
        eq_(self.record.technical_contacts[0].__class__.__name__, 'Contact')
        eq_(self.record.technical_contacts[0].type, yawhois.record.Contact.TYPE_TECHNICAL)
        eq_(self.record.technical_contacts[0].name, "PRIVATE REGISTRANT")
        eq_(self.record.technical_contacts[0].organization, "A HAPPY DREAMHOST CUSTOMER")
        eq_(self.record.technical_contacts[0].address, "417 ASSOCIATED RD #324, C/O DREAMHOST.COM")
        eq_(self.record.technical_contacts[0].city, "BREA")
        eq_(self.record.technical_contacts[0].zip, "92821")
        eq_(self.record.technical_contacts[0].state, "CA")
        eq_(self.record.technical_contacts[0].country_code, "US")
        eq_(self.record.technical_contacts[0].phone, "+1.7147064182")
        eq_(self.record.technical_contacts[0].fax, None)
        eq_(self.record.technical_contacts[0].email, "YW3GAZMC77BTMTF@PROXY.DREAMHOST.COM")

    def test_updated_on(self):
        eq_(self.record.updated_on.__class__.__name__, 'datetime')
        eq_(self.record.updated_on, time_parse('2013-12-14 16:53:27 UTC'))

    def test_expires_on(self):
        eq_(self.record.expires_on.__class__.__name__, 'datetime')
        eq_(self.record.expires_on, time_parse('2015-09-22 04:00:00 UTC'))
