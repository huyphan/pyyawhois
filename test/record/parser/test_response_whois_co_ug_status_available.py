
# This file is autogenerated. Do not edit it manually.
# If you want change the content of this file, edit
#
#   spec/fixtures/responses/whois.co.ug/status_available
#
# and regenerate the tests with the following script
#
#   $ scripts/generate_tests.py
#

from nose.tools import *
from dateutil.parser import parse as time_parse
import yawhois

class TestWhoisCoUgStatusAvailable(object):

    def setUp(self):
        fixture_path = "spec/fixtures/responses/whois.co.ug/status_available.txt"
        host         = "whois.co.ug"
        part         = yawhois.record.Part(open(fixture_path, "r").read(), host)
        self.record  = yawhois.record.Record(None, [part])

    def test_status(self):
        eq_(self.record.status, 'available')

    def test_available(self):
        eq_(self.record.available, True)

    def test_nameservers(self):
        eq_(self.record.nameservers.__class__.__name__, 'list')
        eq_(self.record.nameservers, [])

    def test_registered(self):
        eq_(self.record.registered, False)

    def test_created_on(self):
        eq_(self.record.created_on, None)

    def test_updated_on(self):
        eq_(self.record.updated_on, None)

    def test_expires_on(self):
        eq_(self.record.expires_on, None)
