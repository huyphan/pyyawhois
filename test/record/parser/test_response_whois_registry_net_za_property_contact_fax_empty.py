
# This file is autogenerated. Do not edit it manually.
# If you want change the content of this file, edit
#
#   spec/fixtures/responses/whois.registry.net.za/property_contact_fax_empty
#
# and regenerate the tests with the following script
#
#   $ scripts/generate_tests.py
#

from nose.tools import *
from dateutil.parser import parse as time_parse
import yawhois

class TestWhoisRegistryNetZaPropertyContactFaxEmpty(object):

    def setUp(self):
        fixture_path = "spec/fixtures/responses/whois.registry.net.za/property_contact_fax_empty.txt"
        host         = "whois.registry.net.za"
        part         = yawhois.record.Part(open(fixture_path, "r").read(), host)
        self.record  = yawhois.record.Record(None, [part])

    def test_registrant_contacts(self):
        eq_(self.record.registrant_contacts.__class__.__name__, 'list')
        eq_(len(self.record.registrant_contacts), 1)
        eq_(self.record.registrant_contacts[0].__class__.__name__, 'Contact')
        eq_(self.record.registrant_contacts[0].type, yawhois.record.Contact.TYPE_REGISTRANT)
        eq_(self.record.registrant_contacts[0].name, "FirstRand Bank Limited")
        eq_(self.record.registrant_contacts[0].organization, None)
        eq_(self.record.registrant_contacts[0].address, "2nd floor 4 Merchant Place\nCnr Rivonia and Sandton Drive\nSandton\nGauteng\nZA\n2196")
        eq_(self.record.registrant_contacts[0].city, None)
        eq_(self.record.registrant_contacts[0].zip, None)
        eq_(self.record.registrant_contacts[0].state, None)
        eq_(self.record.registrant_contacts[0].country_code, None)
        eq_(self.record.registrant_contacts[0].phone, "+27.112828000")
        eq_(self.record.registrant_contacts[0].fax, None)
        eq_(self.record.registrant_contacts[0].email, "domreg.admins@firstrand.co.za")
        eq_(self.record.registrant_contacts[0].created_on, None)
        eq_(self.record.registrant_contacts[0].updated_on, None)
