
# This file is autogenerated. Do not edit it manually.
# If you want change the content of this file, edit
#
#   spec/fixtures/responses/whois.dns.be/status_available
#
# and regenerate the tests with the following script
#
#   $ scripts/generate_tests.py
#

from nose.tools import *
from dateutil.parser import parse as time_parse
import yawhois

class TestWhoisDnsBeStatusAvailable(object):

    def setUp(self):
        fixture_path = "spec/fixtures/responses/whois.dns.be/status_available.txt"
        host         = "whois.dns.be"
        part         = yawhois.record.Part(open(fixture_path, "r").read(), host)
        self.record  = yawhois.record.Record(None, [part])

    def test_status(self):
        eq_(self.record.status, 'available')

    def test_available(self):
        eq_(self.record.available, True)

    def test_domain(self):
        eq_(self.record.domain, "u34jedzcq.be")

    def test_nameservers(self):
        eq_(self.record.nameservers.__class__.__name__, 'list')
        eq_(self.record.nameservers, [])

    def test_registered(self):
        eq_(self.record.registered, False)

    def test_response_throttled(self):
        eq_(self.record.response_throttled, False)

    def test_invalid(self):
        eq_(self.record.invalid, False)

    def test_created_on(self):
        eq_(self.record.created_on, None)

    def test_registrar(self):
        eq_(self.record.registrar, None)

    def test_updated_on(self):
        assert_raises(yawhois.exceptions.AttributeNotSupported, self.record.updated_on)

    def test_expires_on(self):
        assert_raises(yawhois.exceptions.AttributeNotSupported, self.record.expires_on)
