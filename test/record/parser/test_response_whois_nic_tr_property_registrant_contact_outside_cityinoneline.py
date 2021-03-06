
# This file is autogenerated. Do not edit it manually.
# If you want change the content of this file, edit
#
#   spec/fixtures/responses/whois.nic.tr/property_registrant_contact_outside_cityinoneline
#
# and regenerate the tests with the following script
#
#   $ scripts/generate_tests.py
#

from nose.tools import *
from dateutil.parser import parse as time_parse
import yawhois

class TestWhoisNicTrPropertyRegistrantContactOutsideCityinoneline(object):

    def setUp(self):
        fixture_path = "spec/fixtures/responses/whois.nic.tr/property_registrant_contact_outside_cityinoneline.txt"
        host         = "whois.nic.tr"
        part         = yawhois.record.Part(open(fixture_path, "r").read(), host)
        self.record  = yawhois.record.Record(None, [part])

    def test_registrant_contacts(self):
        eq_(self.record.registrant_contacts.__class__.__name__, 'list')
        eq_(len(self.record.registrant_contacts), 1)
        eq_(self.record.registrant_contacts[0].__class__.__name__, 'Contact')
        eq_(self.record.registrant_contacts[0].type, yawhois.record.Contact.TYPE_REGISTRANT)
        eq_(self.record.registrant_contacts[0].id, None)
        eq_(self.record.registrant_contacts[0].name, "Yahoo Ýnc.")
        eq_(self.record.registrant_contacts[0].organization, None)
        eq_(self.record.registrant_contacts[0].address, "701 First Avenue Sunnyvale Ca 94089")
        eq_(self.record.registrant_contacts[0].city, None)
        eq_(self.record.registrant_contacts[0].zip, None)
        eq_(self.record.registrant_contacts[0].state, None)
        eq_(self.record.registrant_contacts[0].country, "United States of America")
        eq_(self.record.registrant_contacts[0].country_code, None)
        eq_(self.record.registrant_contacts[0].phone, "+ 901-408-3493300-")
        eq_(self.record.registrant_contacts[0].fax, "+ 901-408-3493301")
        eq_(self.record.registrant_contacts[0].email, "domainadmin@yahoo-inc.com")
