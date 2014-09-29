
# This file is autogenerated. Do not edit it manually.
# If you want change the content of this file, edit
#
#   spec/fixtures/responses/whois.educause.edu/property_contacts_case2
#
# and regenerate the tests with the following script
#
#   $ scripts/generate_tests.py
#

from nose.tools import *
from dateutil.parser import parse as time_parse
import yawhois

class TestWhoisEducauseEduPropertyContactsCase2(object):

    def setUp(self):
        fixture_path = "spec/fixtures/responses/whois.educause.edu/property_contacts_case2.txt"
        host         = "whois.educause.edu"
        part         = yawhois.record.Part(open(fixture_path, "r").read(), host)
        self.record  = yawhois.record.Record(None, [part])

    def test_technical_contacts(self):
        eq_(self.record.technical_contacts.__class__.__name__, 'list')
        eq_(len(self.record.technical_contacts), 1)
        eq_(self.record.technical_contacts[0].__class__.__name__, 'Contact')
        eq_(self.record.technical_contacts[0].id, None)
        eq_(self.record.technical_contacts[0].name, "Domain Admin\nStanford University")
        eq_(self.record.technical_contacts[0].organization, None)
        eq_(self.record.technical_contacts[0].address, "241 Panama Street Pine Hall, Room 115")
        eq_(self.record.technical_contacts[0].city, "Stanford")
        eq_(self.record.technical_contacts[0].zip, "94305-4122")
        eq_(self.record.technical_contacts[0].state, "CA")
        eq_(self.record.technical_contacts[0].country, "UNITED STATES")
        eq_(self.record.technical_contacts[0].country_code, None)
        eq_(self.record.technical_contacts[0].phone, "(650) 723-4328")
        eq_(self.record.technical_contacts[0].fax, None)
        eq_(self.record.technical_contacts[0].email, "sunet-admin@stanford.edu")
