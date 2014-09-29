
# This file is autogenerated. Do not edit it manually.
# If you want change the content of this file, edit
#
#   spec/fixtures/responses/whois.pir.org/status_registered
#
# and regenerate the tests with the following script
#
#   $ scripts/generate_tests.py
#

from nose.tools import *
from dateutil.parser import parse as time_parse
import yawhois

class TestWhoisPirOrgStatusRegistered(object):

    def setUp(self):
        fixture_path = "spec/fixtures/responses/whois.pir.org/status_registered.txt"
        host         = "whois.pir.org"
        part         = yawhois.record.Part(open(fixture_path, "r").read(), host)
        self.record  = yawhois.record.Record(None, [part])

    def test_status(self):
        eq_(self.record.status, ["clientDeleteProhibited", "clientTransferProhibited", "clientUpdateProhibited"])

    def test_available(self):
        eq_(self.record.available, False)

    def test_domain(self):
        eq_(self.record.domain, "google.org")

    def test_nameservers(self):
        eq_(self.record.nameservers.__class__.__name__, 'list')
        eq_(len(self.record.nameservers), 4)
        eq_(self.record.nameservers[0].__class__.__name__, 'Nameserver')
        eq_(self.record.nameservers[0].name, "ns2.google.com")
        eq_(self.record.nameservers[1].__class__.__name__, 'Nameserver')
        eq_(self.record.nameservers[1].name, "ns1.google.com")
        eq_(self.record.nameservers[2].__class__.__name__, 'Nameserver')
        eq_(self.record.nameservers[2].name, "ns3.google.com")
        eq_(self.record.nameservers[3].__class__.__name__, 'Nameserver')
        eq_(self.record.nameservers[3].name, "ns4.google.com")

    def test_admin_contacts(self):
        eq_(self.record.admin_contacts.__class__.__name__, 'list')
        eq_(len(self.record.admin_contacts), 1)
        eq_(self.record.admin_contacts[0].__class__.__name__, 'Contact')
        eq_(self.record.admin_contacts[0].type, yawhois.record.Contact.TYPE_ADMINISTRATIVE)
        eq_(self.record.admin_contacts[0].id, "mmr-32097")
        eq_(self.record.admin_contacts[0].name, "DNS Admin")
        eq_(self.record.admin_contacts[0].organization, "Google Inc.")
        eq_(self.record.admin_contacts[0].address, "1600 Amphitheatre Parkway")
        eq_(self.record.admin_contacts[0].city, "Mountain View")
        eq_(self.record.admin_contacts[0].zip, "94043")
        eq_(self.record.admin_contacts[0].state, "CA")
        eq_(self.record.admin_contacts[0].country_code, "US")
        eq_(self.record.admin_contacts[0].phone, "+1.6506234000")
        eq_(self.record.admin_contacts[0].fax, "+1.6506188571")
        eq_(self.record.admin_contacts[0].email, "dns-admin@google.com")

    def test_registered(self):
        eq_(self.record.registered, True)

    def test_response_throttled(self):
        eq_(self.record.response_throttled, False)

    def test_created_on(self):
        eq_(self.record.created_on.__class__.__name__, 'datetime')
        eq_(self.record.created_on, time_parse('1998-10-21 04:00:00 UTC'))

    def test_registrar(self):
        eq_(self.record.registrar.__class__.__name__, 'Registrar')
        eq_(self.record.registrar.id, "292")
        eq_(self.record.registrar.name, "MarkMonitor Inc. (R37-LROR)")
        eq_(self.record.registrar.organization, None)
        eq_(self.record.registrar.url, None)

    def test_registrant_contacts(self):
        eq_(self.record.registrant_contacts.__class__.__name__, 'list')
        eq_(len(self.record.registrant_contacts), 1)
        eq_(self.record.registrant_contacts[0].__class__.__name__, 'Contact')
        eq_(self.record.registrant_contacts[0].type, yawhois.record.Contact.TYPE_REGISTRANT)
        eq_(self.record.registrant_contacts[0].id, "mmr-32097")
        eq_(self.record.registrant_contacts[0].name, "DNS Admin")
        eq_(self.record.registrant_contacts[0].organization, "Google Inc.")
        eq_(self.record.registrant_contacts[0].address, "1600 Amphitheatre Parkway")
        eq_(self.record.registrant_contacts[0].city, "Mountain View")
        eq_(self.record.registrant_contacts[0].zip, "94043")
        eq_(self.record.registrant_contacts[0].state, "CA")
        eq_(self.record.registrant_contacts[0].country_code, "US")
        eq_(self.record.registrant_contacts[0].phone, "+1.6506234000")
        eq_(self.record.registrant_contacts[0].fax, "+1.6506188571")
        eq_(self.record.registrant_contacts[0].email, "dns-admin@google.com")

    def test_technical_contacts(self):
        eq_(self.record.technical_contacts.__class__.__name__, 'list')
        eq_(len(self.record.technical_contacts), 1)
        eq_(self.record.technical_contacts[0].__class__.__name__, 'Contact')
        eq_(self.record.technical_contacts[0].type, yawhois.record.Contact.TYPE_TECHNICAL)
        eq_(self.record.technical_contacts[0].id, "mmr-32097")
        eq_(self.record.technical_contacts[0].name, "DNS Admin")
        eq_(self.record.technical_contacts[0].organization, "Google Inc.")
        eq_(self.record.technical_contacts[0].address, "1600 Amphitheatre Parkway")
        eq_(self.record.technical_contacts[0].city, "Mountain View")
        eq_(self.record.technical_contacts[0].zip, "94043")
        eq_(self.record.technical_contacts[0].state, "CA")
        eq_(self.record.technical_contacts[0].country_code, "US")
        eq_(self.record.technical_contacts[0].phone, "+1.6506234000")
        eq_(self.record.technical_contacts[0].fax, "+1.6506188571")
        eq_(self.record.technical_contacts[0].email, "dns-admin@google.com")

    def test_updated_on(self):
        eq_(self.record.updated_on.__class__.__name__, 'datetime')
        eq_(self.record.updated_on, time_parse('2013-09-18 09:17:35 UTC'))

    def test_domain_id(self):
        eq_(self.record.domain_id, "D2244233-LROR")

    def test_expires_on(self):
        eq_(self.record.expires_on.__class__.__name__, 'datetime')
        eq_(self.record.expires_on, time_parse('2014-10-20 04:00:00 UTC'))

    def test_disclaimer(self):
        eq_(self.record.disclaimer, "Access to Public Interest Registry WHOIS information is provided to assist persons in determining the contents of a domain name registration record in the Public Interest Registry registry database. The data in this record is provided by Public Interest Registry for informational purposes only, and Public Interest Registry does not guarantee its accuracy. This service is intended only for query-based access. You agree that you will use this data only for lawful purposes and that, under no circumstances will you use this data to(a) allow, enable, or otherwise support the transmission by e-mail, telephone, or facsimile of mass unsolicited, commercial advertising or solicitations to entities other than the data recipient's own existing customers; or (b) enable high volume, automated, electronic processes that send queries or data to the systems of Registry Operator, a Registrar, or Afilias except as reasonably necessary to register domain names or modify existing registrations. All rights reserved. Public Interest Registry reserves the right to modify these terms at any time. By submitting this query, you agree to abide by this policy.")
