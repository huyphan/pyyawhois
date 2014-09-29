
# This file is autogenerated. Do not edit it manually.
# If you want change the content of this file, edit
#
#   spec/fixtures/responses/whois.nic.xxx/status_reserved
#
# and regenerate the tests with the following script
#
#   $ scripts/generate_tests.py
#

from nose.tools import *
from dateutil.parser import parse as time_parse
import yawhois

class TestWhoisNicXxxStatusReserved(object):

    def setUp(self):
        fixture_path = "spec/fixtures/responses/whois.nic.xxx/status_reserved.txt"
        host         = "whois.nic.xxx"
        part         = yawhois.record.Part(open(fixture_path, "r").read(), host)
        self.record  = yawhois.record.Record(None, [part])

    def test_status(self):
        eq_(self.record.status, 'reserved')

    def test_available(self):
        eq_(self.record.available, False)

    def test_registered(self):
        eq_(self.record.registered, True)

    def test_reserved(self):
        eq_(self.record.reserved, True)
