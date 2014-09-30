
# This file is autogenerated. Do not edit it manually.
# If you want change the content of this file, edit
#
#   spec/fixtures/responses/whois.jprs.jp/co.jp/property_state_deleted
#
# and regenerate the tests with the following script
#
#   $ scripts/generate_tests.py
#

from nose.tools import *
from dateutil.parser import parse as time_parse
import yawhois

class TestWhoisJprsJpCoJpPropertyStateDeleted(object):

    def setUp(self):
        fixture_path = "spec/fixtures/responses/whois.jprs.jp/co.jp/property_state_deleted.txt"
        host         = "whois.jprs.jp"
        part         = yawhois.record.Part(open(fixture_path, "r").read(), host)
        self.record  = yawhois.record.Record(None, [part])

    def test_status(self):
        eq_(self.record.status, 'suspended')

    def test_available(self):
        eq_(self.record.available, False)

    def test_registered(self):
        eq_(self.record.registered, True)