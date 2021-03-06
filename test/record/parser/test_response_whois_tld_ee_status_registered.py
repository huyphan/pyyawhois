
# This file is autogenerated. Do not edit it manually.
# If you want change the content of this file, edit
#
#   spec/fixtures/responses/whois.tld.ee/status_registered
#
# and regenerate the tests with the following script
#
#   $ scripts/generate_tests.py
#

from nose.tools import *
from dateutil.parser import parse as time_parse
import yawhois

class TestWhoisTldEeStatusRegistered(object):

    def setUp(self):
        fixture_path = "spec/fixtures/responses/whois.tld.ee/status_registered.txt"
        host         = "whois.tld.ee"
        part         = yawhois.record.Part(open(fixture_path, "r").read(), host)
        self.record  = yawhois.record.Record(None, [part])

    def test_status(self):
        eq_(self.record.status, 'registered')

    def test_available(self):
        eq_(self.record.available, False)

    def test_domain(self):
        eq_(self.record.domain, "edicy.ee")

    def test_nameservers(self):
        eq_(self.record.nameservers.__class__.__name__, 'list')
        eq_(len(self.record.nameservers), 2)
        eq_(self.record.nameservers[0].__class__.__name__, 'Nameserver')
        eq_(self.record.nameservers[0].name, "ns3.edicy.net")
        eq_(self.record.nameservers[0].ipv4, "82.129.24.69")
        eq_(self.record.nameservers[1].__class__.__name__, 'Nameserver')
        eq_(self.record.nameservers[1].name, "ns4.edicy.net")
        eq_(self.record.nameservers[1].ipv4, "82.199.86.42")

    def test_admin_contacts(self):
        eq_(self.record.admin_contacts.__class__.__name__, 'list')
        eq_(len(self.record.admin_contacts), 1)
        eq_(self.record.admin_contacts[0].__class__.__name__, 'Contact')
        eq_(self.record.admin_contacts[0].type, yawhois.record.Contact.TYPE_ADMINISTRATIVE)
        eq_(self.record.admin_contacts[0].id, "CID:FRAKTAL:7")
        eq_(self.record.admin_contacts[0].name, "Tõnu Runnel")
        eq_(self.record.admin_contacts[0].organization, None)
        eq_(self.record.admin_contacts[0].address, None)
        eq_(self.record.admin_contacts[0].city, None)
        eq_(self.record.admin_contacts[0].zip, None)
        eq_(self.record.admin_contacts[0].state, None)
        eq_(self.record.admin_contacts[0].country, None)
        eq_(self.record.admin_contacts[0].country_code, None)
        eq_(self.record.admin_contacts[0].phone, None)
        eq_(self.record.admin_contacts[0].fax, None)
        eq_(self.record.admin_contacts[0].email, "Not Disclosed - Visit www.eestiinternet.ee for webbased WHOIS")
        eq_(self.record.admin_contacts[0].created_on, time_parse('2010-12-10 13:35:38'))

    def test_registered(self):
        eq_(self.record.registered, True)

    def test_created_on(self):
        eq_(self.record.created_on.__class__.__name__, 'datetime')
        eq_(self.record.created_on, time_parse('2010-07-04 07:10:32'))

    def test_registrar(self):
        eq_(self.record.registrar.__class__.__name__, 'Registrar')
        eq_(self.record.registrar.id, "fraktal")
        eq_(self.record.registrar.name, "fraktal")
        eq_(self.record.registrar.organization, None)
        eq_(self.record.registrar.url, None)

    def test_registrant_contacts(self):
        eq_(self.record.registrant_contacts.__class__.__name__, 'list')
        eq_(len(self.record.registrant_contacts), 1)
        eq_(self.record.registrant_contacts[0].__class__.__name__, 'Contact')
        eq_(self.record.registrant_contacts[0].type, yawhois.record.Contact.TYPE_REGISTRANT)
        eq_(self.record.registrant_contacts[0].id, "CID:FRAKTAL:1")
        eq_(self.record.registrant_contacts[0].name, "Priit Haamer")
        eq_(self.record.registrant_contacts[0].organization, None)
        eq_(self.record.registrant_contacts[0].address, None)
        eq_(self.record.registrant_contacts[0].city, None)
        eq_(self.record.registrant_contacts[0].zip, None)
        eq_(self.record.registrant_contacts[0].state, None)
        eq_(self.record.registrant_contacts[0].country, None)
        eq_(self.record.registrant_contacts[0].country_code, None)
        eq_(self.record.registrant_contacts[0].phone, None)
        eq_(self.record.registrant_contacts[0].fax, None)
        eq_(self.record.registrant_contacts[0].email, "Not Disclosed - Visit www.eestiinternet.ee for webbased WHOIS")
        eq_(self.record.registrant_contacts[0].created_on, time_parse('2010-12-09 16:08:33'))

    def test_technical_contacts(self):
        eq_(self.record.technical_contacts.__class__.__name__, 'list')
        eq_(len(self.record.technical_contacts), 1)
        eq_(self.record.technical_contacts[0].__class__.__name__, 'Contact')
        eq_(self.record.technical_contacts[0].type, yawhois.record.Contact.TYPE_TECHNICAL)
        eq_(self.record.technical_contacts[0].id, "CID:FRAKTAL:1")
        eq_(self.record.technical_contacts[0].name, "Priit Haamer")
        eq_(self.record.technical_contacts[0].organization, None)
        eq_(self.record.technical_contacts[0].address, None)
        eq_(self.record.technical_contacts[0].city, None)
        eq_(self.record.technical_contacts[0].zip, None)
        eq_(self.record.technical_contacts[0].state, None)
        eq_(self.record.technical_contacts[0].country, None)
        eq_(self.record.technical_contacts[0].country_code, None)
        eq_(self.record.technical_contacts[0].phone, None)
        eq_(self.record.technical_contacts[0].fax, None)
        eq_(self.record.technical_contacts[0].email, "Not Disclosed - Visit www.eestiinternet.ee for webbased WHOIS")
        eq_(self.record.technical_contacts[0].created_on, time_parse('2010-12-09 16:08:33'))

    def test_updated_on(self):
        eq_(self.record.updated_on.__class__.__name__, 'datetime')
        eq_(self.record.updated_on, time_parse('2010-12-10 13:37:11'))

    def test_domain_id(self):
        assert_raises(yawhois.exceptions.AttributeNotSupported, self.record.domain_id)

    def test_expires_on(self):
        eq_(self.record.expires_on.__class__.__name__, 'datetime')
        eq_(self.record.expires_on, time_parse('2012-12-10'))
