
# This file is autogenerated. Do not edit it manually.
# If you want change the content of this file, edit
#
#   spec/fixtures/responses/whois.enom.com/status_registered_with_blank_updated_date
#
# and regenerate the tests with the following script
#
#   $ scripts/generate_tests.py
#

from nose.tools import *
from dateutil.parser import parse as time_parse
import yawhois

class TestWhoisEnomComStatusRegisteredWithBlankUpdatedDate(object):

    def setUp(self):
        fixture_path = "spec/fixtures/responses/whois.enom.com/status_registered_with_blank_updated_date.txt"
        host         = "whois.enom.com"
        part         = yawhois.record.Part(open(fixture_path, "r").read(), host)
        self.record  = yawhois.record.Record(None, [part])

    def test_updated_on(self):
        eq_(self.record.updated_on, None)