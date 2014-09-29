
# This file is autogenerated. Do not edit it manually.
# If you want change the content of this file, edit
#
#   spec/fixtures/responses/whois.nic.uk/property_registrar_godaddy
#
# and regenerate the tests with the following script
#
#   $ scripts/generate_tests.py
#

from nose.tools import *
from dateutil.parser import parse as time_parse
import yawhois

class TestWhoisNicUkPropertyRegistrarGodaddy(object):

    def setUp(self):
        fixture_path = "spec/fixtures/responses/whois.nic.uk/property_registrar_godaddy.txt"
        host         = "whois.nic.uk"
        part         = yawhois.record.Part(open(fixture_path, "r").read(), host)
        self.record  = yawhois.record.Record(None, [part])

    def test_registrar(self):
        eq_(self.record.registrar.__class__.__name__, 'Registrar')
        eq_(self.record.registrar.id, "GODADDY")
        eq_(self.record.registrar.name, "GoDaddy.com, LLP.")
        eq_(self.record.registrar.name, "GoDaddy.com, LLP.")
        eq_(self.record.registrar.url, None)
