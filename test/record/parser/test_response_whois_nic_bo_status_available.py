
# This file is autogenerated. Do not edit it manually.
# If you want change the content of this file, edit
#
#   spec/fixtures/responses/whois.nic.bo/status_available
#
# and regenerate the tests with the following script
#
#   $ scripts/generate_tests.py
#

from nose.tools import *
from dateutil.parser import parse as time_parse
import yawhois

class TestWhoisNicBoStatusAvailable(object):

    def setUp(self):
        fixture_path = "spec/fixtures/responses/whois.nic.bo/status_available.txt"
        host         = "whois.nic.bo"
        part         = yawhois.record.Part(open(fixture_path, "r").read(), host)
        self.record  = yawhois.record.Record(None, [part])

    def test_status(self):
        eq_(self.record.status, 'available')

    def test_available(self):
        eq_(self.record.available, True)

    def test_domain(self):
        eq_(self.record.domain, None)

    def test_nameservers(self):
        assert_raises(yawhois.exceptions.AttributeNotSupported, self.record.nameservers)

    def test_registered(self):
        eq_(self.record.registered, False)

    def test_created_on(self):
        eq_(self.record.created_on, None)

    def test_updated_on(self):
        assert_raises(yawhois.exceptions.AttributeNotSupported, self.record.updated_on)

    def test_domain_id(self):
        assert_raises(yawhois.exceptions.AttributeNotSupported, self.record.domain_id)

    def test_expires_on(self):
        eq_(self.record.expires_on, None)
