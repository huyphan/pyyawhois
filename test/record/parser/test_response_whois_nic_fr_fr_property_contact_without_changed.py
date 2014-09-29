
# This file is autogenerated. Do not edit it manually.
# If you want change the content of this file, edit
#
#   spec/fixtures/responses/whois.nic.fr/fr/property_contact_without_changed
#
# and regenerate the tests with the following script
#
#   $ scripts/generate_tests.py
#

from nose.tools import *
from dateutil.parser import parse as time_parse
import yawhois

class TestWhoisNicFrFrPropertyContactWithoutChanged(object):

    def setUp(self):
        fixture_path = "spec/fixtures/responses/whois.nic.fr/fr/property_contact_without_changed.txt"
        host         = "whois.nic.fr"
        part         = yawhois.record.Part(open(fixture_path, "r").read(), host)
        self.record  = yawhois.record.Record(None, [part])

    def test_admin_contacts(self):
        eq_(self.record.admin_contacts.__class__.__name__, 'list')
        eq_(len(self.record.admin_contacts), 1)
        eq_(self.record.admin_contacts[0].__class__.__name__, 'Contact')
        eq_(self.record.admin_contacts[0].type, yawhois.record.Contact.TYPE_ADMINISTRATIVE)
        eq_(self.record.admin_contacts[0].id, "JMR39-FRNIC")
        eq_(self.record.admin_contacts[0].name, "Jean Marc Raimondo")
        eq_(self.record.admin_contacts[0].organization, "1C2")
        eq_(self.record.admin_contacts[0].address, "20-22, rue Louis Armand\n75015 Paris")
        eq_(self.record.admin_contacts[0].city, None)
        eq_(self.record.admin_contacts[0].zip, None)
        eq_(self.record.admin_contacts[0].state, None)
        eq_(self.record.admin_contacts[0].country, None)
        eq_(self.record.admin_contacts[0].country_code, "FR")
        eq_(self.record.admin_contacts[0].phone, "+33 1 30 62 40 06")
        eq_(self.record.admin_contacts[0].fax, None)
        eq_(self.record.admin_contacts[0].email, "jmr@1c2.com")
        eq_(self.record.admin_contacts[0].updated_on, None)
