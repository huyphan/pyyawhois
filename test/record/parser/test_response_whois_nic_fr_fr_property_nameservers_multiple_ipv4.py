
# This file is autogenerated. Do not edit it manually.
# If you want change the content of this file, edit
#
#   spec/fixtures/responses/whois.nic.fr/fr/property_nameservers_multiple_ipv4
#
# and regenerate the tests with the following script
#
#   $ scripts/generate_tests.py
#

from nose.tools import *
from dateutil.parser import parse as time_parse
import yawhois

class TestWhoisNicFrFrPropertyNameserversMultipleIpv4(object):

    def setUp(self):
        fixture_path = "spec/fixtures/responses/whois.nic.fr/fr/property_nameservers_multiple_ipv4.txt"
        host         = "whois.nic.fr"
        part         = yawhois.record.Part(open(fixture_path, "r").read(), host)
        self.record  = yawhois.record.Record(None, [part])

    def test_nameservers(self):
        eq_(self.record.nameservers.__class__.__name__, 'list')
        eq_(len(self.record.nameservers), 2)
        eq_(self.record.nameservers[0].__class__.__name__, 'Nameserver')
        eq_(self.record.nameservers[0].name, "ns1.boursedirect.fr")
        eq_(self.record.nameservers[0].ipv4, "212.157.203.190")
        eq_(self.record.nameservers[0].ipv6, None)
        eq_(self.record.nameservers[1].__class__.__name__, 'Nameserver')
        eq_(self.record.nameservers[1].name, "ns2.boursedirect.fr")
        eq_(self.record.nameservers[1].ipv4, "212.157.203.189")
        eq_(self.record.nameservers[1].ipv6, None)
