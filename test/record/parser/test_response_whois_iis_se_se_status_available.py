
# This file is autogenerated. Do not edit it manually.
# If you want change the content of this file, edit
#
#   spec/fixtures/responses/whois.iis.se/se/status_available
#
# and regenerate the tests with the following script
#
#   $ scripts/generate_tests.py
#

from nose.tools import *
from dateutil.parser import parse as time_parse
import yawhois

class TestWhoisIisSeSeStatusAvailable(object):

    def setUp(self):
        fixture_path = "spec/fixtures/responses/whois.iis.se/se/status_available.txt"
        host         = "whois.iis.se"
        part         = yawhois.record.Part(open(fixture_path, "r").read(), host)
        self.record  = yawhois.record.Record(None, [part])

    def test_status(self):
        eq_(self.record.status, 'available')

    def test_available(self):
        eq_(self.record.available, True)

    def test_domain(self):
        eq_(self.record.domain, None)

    def test_nameservers(self):
        eq_(self.record.nameservers.__class__.__name__, 'list')
        eq_(self.record.nameservers, [])

    def test_admin_contacts(self):
        eq_(self.record.admin_contacts.__class__.__name__, 'list')
        eq_(self.record.admin_contacts, [])

    def test_registered(self):
        eq_(self.record.registered, False)

    def test_created_on(self):
        eq_(self.record.created_on, None)

    def test_registrar(self):
        eq_(self.record.registrar, None)

    def test_registrant_contacts(self):
        eq_(self.record.registrant_contacts.__class__.__name__, 'list')
        eq_(self.record.registrant_contacts, [])

    def test_technical_contacts(self):
        eq_(self.record.technical_contacts.__class__.__name__, 'list')
        eq_(self.record.technical_contacts, [])

    def test_updated_on(self):
        eq_(self.record.updated_on, None)

    def test_domain_id(self):
        assert_raises(yawhois.exceptions.AttributeNotSupported, self.record.domain_id)

    def test_expires_on(self):
        eq_(self.record.expires_on, None)

    def test_disclaimer(self):
        eq_(self.record.disclaimer, "Copyright (c) 1997- .SE (The Internet Infrastructure Foundation). All rights reserved. The information obtained through searches, or otherwise, is protected by the Swedish Copyright Act (1960:729) and international conventions. It is also subject to database protection according to the Swedish Copyright Act. Any use of this material to target advertising or similar activities is forbidden and will be prosecuted. If any of the information below is transferred to a third party, it must be done in its entirety. This server must not be used as a backend for a search engine. Result of search for registered domain names under the .SE top level domain. This whois printout is printed with UTF-8 encoding.")
