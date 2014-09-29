
# This file is autogenerated. Do not edit it manually.
# If you want change the content of this file, edit
#
#   spec/fixtures/responses/whois.educause.edu/property_contact_registrant_without_zip
#
# and regenerate the tests with the following script
#
#   $ scripts/generate_tests.py
#

from nose.tools import *
from dateutil.parser import parse as time_parse
import yawhois

class TestWhoisEducauseEduPropertyContactRegistrantWithoutZip(object):

    def setUp(self):
        fixture_path = "spec/fixtures/responses/whois.educause.edu/property_contact_registrant_without_zip.txt"
        host         = "whois.educause.edu"
        part         = yawhois.record.Part(open(fixture_path, "r").read(), host)
        self.record  = yawhois.record.Record(None, [part])

    def test_registrant_contacts(self):
        eq_(self.record.registrant_contacts.__class__.__name__, 'list')
        eq_(len(self.record.registrant_contacts), 1)
        eq_(self.record.registrant_contacts[0].__class__.__name__, 'Contact')
        eq_(self.record.registrant_contacts[0].type, yawhois.record.Contact.TYPE_REGISTRANT)
        eq_(self.record.registrant_contacts[0].id, None)
        eq_(self.record.registrant_contacts[0].name, None)
        eq_(self.record.registrant_contacts[0].organization, "The American University of the Caribbean School of Medicine")
        eq_(self.record.registrant_contacts[0].address, "c/o Campbell Corporate Services, Ltd.\nScotiabank Building, P. O. Box 268")
        eq_(self.record.registrant_contacts[0].city, "Grand Cayman")
        eq_(self.record.registrant_contacts[0].zip, None)
        eq_(self.record.registrant_contacts[0].state, None)
        eq_(self.record.registrant_contacts[0].country, "CAYMAN ISLANDS")
        eq_(self.record.registrant_contacts[0].country_code, None)
        eq_(self.record.registrant_contacts[0].phone, None)
        eq_(self.record.registrant_contacts[0].fax, None)
        eq_(self.record.registrant_contacts[0].email, None)
