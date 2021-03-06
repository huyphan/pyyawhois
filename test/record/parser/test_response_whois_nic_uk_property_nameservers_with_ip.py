
# This file is autogenerated. Do not edit it manually.
# If you want change the content of this file, edit
#
#   spec/fixtures/responses/whois.nic.uk/property_nameservers_with_ip
#
# and regenerate the tests with the following script
#
#   $ scripts/generate_tests.py
#

from nose.tools import *
from dateutil.parser import parse as time_parse
import yawhois

class TestWhoisNicUkPropertyNameserversWithIp(object):

    def setUp(self):
        fixture_path = "spec/fixtures/responses/whois.nic.uk/property_nameservers_with_ip.txt"
        host         = "whois.nic.uk"
        part         = yawhois.record.Part(open(fixture_path, "r").read(), host)
        self.record  = yawhois.record.Record(None, [part])

    def test_nameservers(self):
        eq_(self.record.nameservers.__class__.__name__, 'list')
        eq_(len(self.record.nameservers), 2)
        eq_(self.record.nameservers[0].__class__.__name__, 'Nameserver')
        eq_(self.record.nameservers[0].name, "ns0.netbenefit.co.uk")
        eq_(self.record.nameservers[0].ipv4, "212.53.64.30")
        eq_(self.record.nameservers[1].__class__.__name__, 'Nameserver')
        eq_(self.record.nameservers[1].name, "ns1.netbenefit.co.uk")
        eq_(self.record.nameservers[1].ipv4, "212.53.77.30")
