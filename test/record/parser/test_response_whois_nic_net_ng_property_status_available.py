
# This file is autogenerated. Do not edit it manually.
# If you want change the content of this file, edit
#
#   spec/fixtures/responses/whois.nic.net.ng/property_status_available
#
# and regenerate the tests with the following script
#
#   $ scripts/generate_tests.py
#

from nose.tools import *
from dateutil.parser import parse as time_parse
import yawhois

class TestWhoisNicNetNgPropertyStatusAvailable(object):

    def setUp(self):
        fixture_path = "spec/fixtures/responses/whois.nic.net.ng/property_status_available.txt"
        host         = "whois.nic.net.ng"
        part         = yawhois.record.Part(open(fixture_path, "r").read(), host)
        self.record  = yawhois.record.Record(None, [part])

    def test_status(self):
        eq_(self.record.status, 'available')

    def test_available(self):
        eq_(self.record.available, True)

    def test_registered(self):
        eq_(self.record.registered, False)
