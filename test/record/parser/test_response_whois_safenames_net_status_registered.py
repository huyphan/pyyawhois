
# This file is autogenerated. Do not edit it manually.
# If you want change the content of this file, edit
#
#   spec/fixtures/responses/whois.safenames.net/status_registered
#
# and regenerate the tests with the following script
#
#   $ scripts/generate_tests.py
#

from nose.tools import *
from dateutil.parser import parse as time_parse
import yawhois

class TestWhoisSafenamesNetStatusRegistered(object):

    def setUp(self):
        fixture_path = "spec/fixtures/responses/whois.safenames.net/status_registered.txt"
        host         = "whois.safenames.net"
        part         = yawhois.record.Part(open(fixture_path, "r").read(), host)
        self.record  = yawhois.record.Record(None, [part])

    def test_status(self):
        eq_(self.record.status, 'registered')

    def test_available(self):
        eq_(self.record.available, False)

    def test_domain(self):
        eq_(self.record.domain, "stripe.com")

    def test_nameservers(self):
        eq_(self.record.nameservers.__class__.__name__, 'list')
        eq_(len(self.record.nameservers), 2)
        eq_(self.record.nameservers[0].__class__.__name__, 'Nameserver')
        eq_(self.record.nameservers[0].name, "dns1.idp365.net")
        eq_(self.record.nameservers[1].__class__.__name__, 'Nameserver')
        eq_(self.record.nameservers[1].name, "dns2.idp365.net")

    def test_admin_contacts(self):
        eq_(self.record.admin_contacts.__class__.__name__, 'list')
        eq_(len(self.record.admin_contacts), 1)
        eq_(self.record.admin_contacts[0].__class__.__name__, 'Contact')
        eq_(self.record.admin_contacts[0].type, yawhois.record.Contact.TYPE_ADMINISTRATIVE)
        eq_(self.record.admin_contacts[0].id, None)
        eq_(self.record.admin_contacts[0].name, "Domain Admin")
        eq_(self.record.admin_contacts[0].organization, "Stripe")
        eq_(self.record.admin_contacts[0].address, "3180 18th St")
        eq_(self.record.admin_contacts[0].city, "San Francisco")
        eq_(self.record.admin_contacts[0].zip, "94110")
        eq_(self.record.admin_contacts[0].state, "CA")
        eq_(self.record.admin_contacts[0].country, None)
        eq_(self.record.admin_contacts[0].country_code, "US")
        eq_(self.record.admin_contacts[0].phone, "+1.8772544179")
        eq_(self.record.admin_contacts[0].fax, None)
        eq_(self.record.admin_contacts[0].email, "dns@stripe.com")
        eq_(self.record.admin_contacts[0].created_on, None)
        eq_(self.record.admin_contacts[0].updated_on, None)

    def test_registered(self):
        eq_(self.record.registered, True)

    def test_created_on(self):
        eq_(self.record.created_on.__class__.__name__, 'datetime')
        eq_(self.record.created_on, time_parse('1995-09-12T04:00:00Z'))

    def test_registrar(self):
        eq_(self.record.registrar.__class__.__name__, 'Registrar')
        eq_(self.record.registrar.id, "447")
        eq_(self.record.registrar.name, "Safenames Ltd")
        eq_(self.record.registrar.organization, "Safenames Ltd")
        eq_(self.record.registrar.url, "http://www.safenames.net")

    def test_registrant_contacts(self):
        eq_(self.record.registrant_contacts.__class__.__name__, 'list')
        eq_(len(self.record.registrant_contacts), 1)
        eq_(self.record.registrant_contacts[0].__class__.__name__, 'Contact')
        eq_(self.record.registrant_contacts[0].type, yawhois.record.Contact.TYPE_REGISTRANT)
        eq_(self.record.registrant_contacts[0].id, None)
        eq_(self.record.registrant_contacts[0].name, "Domain Admin")
        eq_(self.record.registrant_contacts[0].organization, "Stripe")
        eq_(self.record.registrant_contacts[0].address, "3180 18th St")
        eq_(self.record.registrant_contacts[0].city, "San Francisco")
        eq_(self.record.registrant_contacts[0].zip, "94110")
        eq_(self.record.registrant_contacts[0].state, "CA")
        eq_(self.record.registrant_contacts[0].country, None)
        eq_(self.record.registrant_contacts[0].country_code, "US")
        eq_(self.record.registrant_contacts[0].phone, "+1.8772544179")
        eq_(self.record.registrant_contacts[0].fax, None)
        eq_(self.record.registrant_contacts[0].email, "dns@stripe.com")
        eq_(self.record.registrant_contacts[0].created_on, None)
        eq_(self.record.registrant_contacts[0].updated_on, None)

    def test_technical_contacts(self):
        eq_(self.record.technical_contacts.__class__.__name__, 'list')
        eq_(len(self.record.technical_contacts), 1)
        eq_(self.record.technical_contacts[0].__class__.__name__, 'Contact')
        eq_(self.record.technical_contacts[0].type, yawhois.record.Contact.TYPE_TECHNICAL)
        eq_(self.record.technical_contacts[0].id, None)
        eq_(self.record.technical_contacts[0].name, "Domain Admin")
        eq_(self.record.technical_contacts[0].organization, "Stripe")
        eq_(self.record.technical_contacts[0].address, "3180 18th St")
        eq_(self.record.technical_contacts[0].city, "San Francisco")
        eq_(self.record.technical_contacts[0].zip, "94110")
        eq_(self.record.technical_contacts[0].state, "CA")
        eq_(self.record.technical_contacts[0].country, None)
        eq_(self.record.technical_contacts[0].country_code, "US")
        eq_(self.record.technical_contacts[0].phone, "+1.8772544179")
        eq_(self.record.technical_contacts[0].fax, None)
        eq_(self.record.technical_contacts[0].email, "dns@stripe.com")
        eq_(self.record.technical_contacts[0].created_on, None)
        eq_(self.record.technical_contacts[0].updated_on, None)

    def test_updated_on(self):
        eq_(self.record.updated_on.__class__.__name__, 'datetime')
        eq_(self.record.updated_on, time_parse('2014-10-02T15:33:46Z'))

    def test_domain_id(self):
        eq_(self.record.domain_id, None)

    def test_expires_on(self):
        eq_(self.record.expires_on.__class__.__name__, 'datetime')
        eq_(self.record.expires_on, time_parse('2024-09-11T04:00:00Z'))
