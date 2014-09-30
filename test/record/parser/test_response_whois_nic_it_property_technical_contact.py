
# This file is autogenerated. Do not edit it manually.
# If you want change the content of this file, edit
#
#   spec/fixtures/responses/whois.nic.it/property_technical_contact
#
# and regenerate the tests with the following script
#
#   $ scripts/generate_tests.py
#

from nose.tools import *
from dateutil.parser import parse as time_parse
import yawhois

class TestWhoisNicItPropertyTechnicalContact(object):

    def setUp(self):
        fixture_path = "spec/fixtures/responses/whois.nic.it/property_technical_contact.txt"
        host         = "whois.nic.it"
        part         = yawhois.record.Part(open(fixture_path, "r").read(), host)
        self.record  = yawhois.record.Record(None, [part])

    def test_technical_contacts(self):
        eq_(self.record.technical_contacts.__class__.__name__, 'list')
        eq_(len(self.record.technical_contacts), 1)
        eq_(self.record.technical_contacts[0].__class__.__name__, 'Contact')
        eq_(self.record.technical_contacts[0].type, yawhois.record.Contact.TYPE_TECHNICAL)
        eq_(self.record.technical_contacts[0].id, "TS7016-ITNIC")
        eq_(self.record.technical_contacts[0].name, "Technical Services")