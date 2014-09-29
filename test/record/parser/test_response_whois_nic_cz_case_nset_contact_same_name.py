
# This file is autogenerated. Do not edit it manually.
# If you want change the content of this file, edit
#
#   spec/fixtures/responses/whois.nic.cz/case_nset_contact_same_name
#
# and regenerate the tests with the following script
#
#   $ scripts/generate_tests.py
#

from nose.tools import *
from dateutil.parser import parse as time_parse
import yawhois

class TestWhoisNicCzCaseNsetContactSameName(object):

    def setUp(self):
        fixture_path = "spec/fixtures/responses/whois.nic.cz/case_nset_contact_same_name.txt"
        host         = "whois.nic.cz"
        part         = yawhois.record.Part(open(fixture_path, "r").read(), host)
        self.record  = yawhois.record.Record(None, [part])

    def test_technical_contacts(self):
        eq_(self.record.technical_contacts.__class__.__name__, 'list')
        eq_(len(self.record.technical_contacts), 1)
        eq_(self.record.technical_contacts[0].__class__.__name__, 'Contact')
        eq_(self.record.technical_contacts[0].id, "WEBAREAL-CZ")
        eq_(self.record.technical_contacts[0].name, "Jaroslav Hansal")
        eq_(self.record.technical_contacts[0].organization, None)
        eq_(self.record.technical_contacts[0].address, "Rudolfovská tř. 247/85\nČeské Budějovice\n37001\nCZ")
        eq_(self.record.technical_contacts[0].city, None)
        eq_(self.record.technical_contacts[0].zip, None)
        eq_(self.record.technical_contacts[0].state, None)
        eq_(self.record.technical_contacts[0].country, None)
        eq_(self.record.technical_contacts[0].country_code, None)
        eq_(self.record.technical_contacts[0].phone, None)
        eq_(self.record.technical_contacts[0].fax, None)
        eq_(self.record.technical_contacts[0].email, "info@webareal.cz")
        eq_(self.record.technical_contacts[0].created_on, time_parse('2009-04-10 14:48:02'))
