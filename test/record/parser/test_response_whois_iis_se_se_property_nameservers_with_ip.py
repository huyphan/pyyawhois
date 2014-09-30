
# This file is autogenerated. Do not edit it manually.
# If you want change the content of this file, edit
#
#   spec/fixtures/responses/whois.iis.se/se/property_nameservers_with_ip
#
# and regenerate the tests with the following script
#
#   $ scripts/generate_tests.py
#

from nose.tools import *
from dateutil.parser import parse as time_parse
import yawhois

class TestWhoisIisSeSePropertyNameserversWithIp(object):

    def setUp(self):
        fixture_path = "spec/fixtures/responses/whois.iis.se/se/property_nameservers_with_ip.txt"
        host         = "whois.iis.se"
        part         = yawhois.record.Part(open(fixture_path, "r").read(), host)
        self.record  = yawhois.record.Record(None, [part])

    def test_nameservers(self):
        eq_(self.record.nameservers.__class__.__name__, 'list')
        eq_(len(self.record.nameservers), 4)
        eq_(self.record.nameservers[0].__class__.__name__, 'Nameserver')
        eq_(self.record.nameservers[0].name, "ns2.loopia.se")
        eq_(self.record.nameservers[0].ipv4, "93.188.0.21")
        eq_(self.record.nameservers[1].__class__.__name__, 'Nameserver')
        eq_(self.record.nameservers[1].name, "ns4.loopia.se")
        eq_(self.record.nameservers[1].ipv4, "93.188.0.20")
        eq_(self.record.nameservers[2].__class__.__name__, 'Nameserver')
        eq_(self.record.nameservers[2].name, "ns3.loopia.se")
        eq_(self.record.nameservers[2].ipv4, "93.188.0.21")
        eq_(self.record.nameservers[3].__class__.__name__, 'Nameserver')
        eq_(self.record.nameservers[3].name, "ns1.loopia.se")
        eq_(self.record.nameservers[3].ipv4, "93.188.0.20")