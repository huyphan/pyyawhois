
# This file is autogenerated. Do not edit it manually.
# If you want change the content of this file, edit
#
#   spec/fixtures/responses/whois.nic.fr/pm/response_throttled
#
# and regenerate the tests with the following script
#
#   $ scripts/generate_tests.py
#

from nose.tools import *
from dateutil.parser import parse as time_parse
import yawhois

class TestWhoisNicFrPmResponseThrottled(object):

    def setUp(self):
        fixture_path = "spec/fixtures/responses/whois.nic.fr/pm/response_throttled.txt"
        host         = "whois.nic.fr"
        part         = yawhois.record.Part(open(fixture_path, "r").read(), host)
        self.record  = yawhois.record.Record(None, [part])

    def test_response_throttled(self):
        eq_(self.record.response_throttled, True)
