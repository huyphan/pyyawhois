
# This file is autogenerated. Do not edit it manually.
# If you want change the content of this file, edit
#
#   spec/fixtures/responses/whois.dreamhost.com/property_contact_private
#
# and regenerate the tests with the following script
#
#   $ scripts/generate_tests.py
#

from nose.tools import *
from dateutil.parser import parse as time_parse
import yawhois

class TestWhoisDreamhostComPropertyContactPrivate(object):

    def setUp(self):
        fixture_path = "spec/fixtures/responses/whois.dreamhost.com/property_contact_private.txt"
        host         = "whois.dreamhost.com"
        part         = yawhois.record.Part(open(fixture_path, "r").read(), host)
        self.record  = yawhois.record.Record(None, [part])

    def test_admin_contacts(self):
        eq_(self.record.admin_contacts.__class__.__name__, 'list')
        eq_(len(self.record.admin_contacts), 1)
        eq_(self.record.admin_contacts[0].__class__.__name__, 'Contact')
        eq_(self.record.admin_contacts[0].type, yawhois.record.Contact.TYPE_ADMINISTRATIVE)
        eq_(self.record.admin_contacts[0].name, "PRIVATE REGISTRANT")
        eq_(self.record.admin_contacts[0].organization, "A HAPPY DREAMHOST CUSTOMER")
        eq_(self.record.admin_contacts[0].address, "417 ASSOCIATED RD #324, C/O ADEQUATEHQ.COM")
        eq_(self.record.admin_contacts[0].city, "BREA")
        eq_(self.record.admin_contacts[0].zip, "92821")
        eq_(self.record.admin_contacts[0].state, "CA")
        eq_(self.record.admin_contacts[0].country_code, "US")
        eq_(self.record.admin_contacts[0].phone, "+1.7147064182")
        eq_(self.record.admin_contacts[0].fax, None)
        eq_(self.record.admin_contacts[0].email, "ADEQUATEHQ.COM@PROXY.DREAMHOST.COM")

    def test_registrant_contacts(self):
        eq_(self.record.registrant_contacts.__class__.__name__, 'list')
        eq_(len(self.record.registrant_contacts), 1)
        eq_(self.record.registrant_contacts[0].__class__.__name__, 'Contact')
        eq_(self.record.registrant_contacts[0].type, yawhois.record.Contact.TYPE_REGISTRANT)
        eq_(self.record.registrant_contacts[0].name, "PRIVATE REGISTRANT")
        eq_(self.record.registrant_contacts[0].organization, "A HAPPY DREAMHOST CUSTOMER")
        eq_(self.record.registrant_contacts[0].address, "417 ASSOCIATED RD #324, C/O ADEQUATEHQ.COM")
        eq_(self.record.registrant_contacts[0].city, "BREA")
        eq_(self.record.registrant_contacts[0].zip, "92821")
        eq_(self.record.registrant_contacts[0].state, "CA")
        eq_(self.record.registrant_contacts[0].country_code, "US")
        eq_(self.record.registrant_contacts[0].phone, "+1.7147064182")
        eq_(self.record.registrant_contacts[0].fax, None)
        eq_(self.record.registrant_contacts[0].email, "ADEQUATEHQ.COM@PROXY.DREAMHOST.COM")

    def test_technical_contacts(self):
        eq_(self.record.technical_contacts.__class__.__name__, 'list')
        eq_(len(self.record.technical_contacts), 1)
        eq_(self.record.technical_contacts[0].__class__.__name__, 'Contact')
        eq_(self.record.technical_contacts[0].type, yawhois.record.Contact.TYPE_TECHNICAL)
        eq_(self.record.technical_contacts[0].name, "PRIVATE REGISTRANT")
        eq_(self.record.technical_contacts[0].organization, "A HAPPY DREAMHOST CUSTOMER")
        eq_(self.record.technical_contacts[0].address, "417 ASSOCIATED RD #324, C/O ADEQUATEHQ.COM")
        eq_(self.record.technical_contacts[0].city, "BREA")
        eq_(self.record.technical_contacts[0].zip, "92821")
        eq_(self.record.technical_contacts[0].state, "CA")
        eq_(self.record.technical_contacts[0].country_code, "US")
        eq_(self.record.technical_contacts[0].phone, "+1.7147064182")
        eq_(self.record.technical_contacts[0].fax, None)
        eq_(self.record.technical_contacts[0].email, "ADEQUATEHQ.COM@PROXY.DREAMHOST.COM")
