
# This file is autogenerated. Do not edit it manually.
# If you want change the content of this file, edit
#
#   spec/fixtures/responses/whois.nic.it/property_contact_province
#
# and regenerate the tests with the following script
#
#   $ scripts/generate_tests.py
#

from nose.tools import *
from dateutil.parser import parse as time_parse
import yawhois

class TestWhoisNicItPropertyContactProvince(object):

    def setUp(self):
        fixture_path = "spec/fixtures/responses/whois.nic.it/property_contact_province.txt"
        host         = "whois.nic.it"
        part         = yawhois.record.Part(open(fixture_path, "r").read(), host)
        self.record  = yawhois.record.Record(None, [part])

    def test_registrant_contacts(self):
        eq_(self.record.registrant_contacts.__class__.__name__, 'list')
        eq_(len(self.record.registrant_contacts), 1)
        eq_(self.record.registrant_contacts[0].__class__.__name__, 'Contact')
        eq_(self.record.registrant_contacts[0].type, yawhois.record.Contact.TYPE_REGISTRANT)
        eq_(self.record.registrant_contacts[0].id, "HTML1-ITNIC")
        eq_(self.record.registrant_contacts[0].name, "HTML.it srl")
        eq_(self.record.registrant_contacts[0].organization, "HTML.it srl")
        eq_(self.record.registrant_contacts[0].address, "Viale Alessandrino, 595")
        eq_(self.record.registrant_contacts[0].city, "Roma")
        eq_(self.record.registrant_contacts[0].zip, "00172")
        eq_(self.record.registrant_contacts[0].state, "RM")
        eq_(self.record.registrant_contacts[0].country_code, "IT")
        eq_(self.record.registrant_contacts[0].created_on, time_parse('2007-03-01 10:28:08'))
        eq_(self.record.registrant_contacts[0].updated_on, time_parse('2007-03-01 10:28:08'))
