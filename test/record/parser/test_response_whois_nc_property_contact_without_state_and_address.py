
# This file is autogenerated. Do not edit it manually.
# If you want change the content of this file, edit
#
#   spec/fixtures/responses/whois.nc/property_contact_without_state_and_address
#
# and regenerate the tests with the following script
#
#   $ scripts/generate_tests.py
#

from nose.tools import *
from dateutil.parser import parse as time_parse
import yawhois

class TestWhoisNcPropertyContactWithoutStateAndAddress(object):

    def setUp(self):
        fixture_path = "spec/fixtures/responses/whois.nc/property_contact_without_state_and_address.txt"
        host         = "whois.nc"
        part         = yawhois.record.Part(open(fixture_path, "r").read(), host)
        self.record  = yawhois.record.Record(None, [part])

    def test_registrant_contacts(self):
        eq_(self.record.registrant_contacts.__class__.__name__, 'list')
        eq_(len(self.record.registrant_contacts), 1)
        eq_(self.record.registrant_contacts[0].__class__.__name__, 'Contact')
        eq_(self.record.registrant_contacts[0].type, yawhois.record.Contact.TYPE_REGISTRANT)
        eq_(self.record.registrant_contacts[0].name, "DTSI")
        eq_(self.record.registrant_contacts[0].organization, None)
        eq_(self.record.registrant_contacts[0].address, "BP 15101")
        eq_(self.record.registrant_contacts[0].city, "NOUMEA CEDEX")
        eq_(self.record.registrant_contacts[0].zip, "98804")
        eq_(self.record.registrant_contacts[0].state, None)
        eq_(self.record.registrant_contacts[0].country, None)
        eq_(self.record.registrant_contacts[0].phone, None)
        eq_(self.record.registrant_contacts[0].fax, None)
        eq_(self.record.registrant_contacts[0].email, None)
