
# This file is autogenerated. Do not edit it manually.
# If you want change the content of this file, edit
#
#   spec/fixtures/responses/whois.sgnic.sg/property_nameservers_schema_1_with_ip
#
# and regenerate the tests with the following script
#
#   $ scripts/generate_tests.py
#

from nose.tools import *
from dateutil.parser import parse as time_parse
import yawhois

class TestWhoisSgnicSgPropertyNameserversSchema1WithIp(object):

    def setUp(self):
        fixture_path = "spec/fixtures/responses/whois.sgnic.sg/property_nameservers_schema_1_with_ip.txt"
        host         = "whois.sgnic.sg"
        part         = yawhois.record.Part(open(fixture_path, "r").read(), host)
        self.record  = yawhois.record.Record(None, [part])

    def test_nameservers(self):
        eq_(self.record.nameservers.__class__.__name__, 'list')
        eq_(len(self.record.nameservers), 3)
        eq_(self.record.nameservers[0].__class__.__name__, 'Nameserver')
        eq_(self.record.nameservers[0].name, "dnssec1.singnet.com.sg")
        eq_(self.record.nameservers[0].ipv4, "165.21.83.11")
        eq_(self.record.nameservers[1].__class__.__name__, 'Nameserver')
        eq_(self.record.nameservers[1].name, "dnssec2.singnet.com.sg")
        eq_(self.record.nameservers[1].ipv4, "195.13.10.226")
        eq_(self.record.nameservers[2].__class__.__name__, 'Nameserver')
        eq_(self.record.nameservers[2].name, "dnssec3.singnet.com.sg")
        eq_(self.record.nameservers[2].ipv4, "165.21.100.11")
