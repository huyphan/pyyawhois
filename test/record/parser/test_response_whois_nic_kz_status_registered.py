
# This file is autogenerated. Do not edit it manually.
# If you want change the content of this file, edit
#
#   spec/fixtures/responses/whois.nic.kz/status_registered
#
# and regenerate the tests with the following script
#
#   $ scripts/generate_tests.py
#

from nose.tools import *
from dateutil.parser import parse as time_parse
import yawhois

class TestWhoisNicKzStatusRegistered(object):

    def setUp(self):
        fixture_path = "spec/fixtures/responses/whois.nic.kz/status_registered.txt"
        host         = "whois.nic.kz"
        part         = yawhois.record.Part(open(fixture_path, "r").read(), host)
        self.record  = yawhois.record.Record(None, [part])

    def test_status(self):
        eq_(self.record.status, ["ok"])

    def test_available(self):
        eq_(self.record.available, False)

    def test_nameservers(self):
        eq_(self.record.nameservers.__class__.__name__, 'list')
        eq_(len(self.record.nameservers), 2)
        eq_(self.record.nameservers[0].__class__.__name__, 'Nameserver')
        eq_(self.record.nameservers[0].name, "ns1.google.com")
        eq_(self.record.nameservers[1].__class__.__name__, 'Nameserver')
        eq_(self.record.nameservers[1].name, "ns2.google.com")

    def test_registered(self):
        eq_(self.record.registered, True)

    def test_created_on(self):
        eq_(self.record.created_on.__class__.__name__, 'datetime')
        eq_(self.record.created_on, time_parse('1999-06-07 13:01:43'))

    def test_updated_on(self):
        eq_(self.record.updated_on.__class__.__name__, 'datetime')
        eq_(self.record.updated_on, time_parse('2012-11-28 03:16:59'))

    def test_expires_on(self):
        assert_raises(yawhois.exceptions.AttributeNotSupported, self.record.expires_on)
