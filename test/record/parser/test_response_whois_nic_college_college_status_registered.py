
# This file is autogenerated. Do not edit it manually.
# If you want change the content of this file, edit
#
#   spec/fixtures/responses/whois.nic.college/college/status_registered
#
# and regenerate the tests with the following script
#
#   $ scripts/generate_tests.py
#

from nose.tools import *
from dateutil.parser import parse as time_parse
import yawhois

class TestWhoisNicCollegeCollegeStatusRegistered(object):

    def setUp(self):
        fixture_path = "spec/fixtures/responses/whois.nic.college/college/status_registered.txt"
        host         = "whois.nic.college"
        part         = yawhois.record.Part(open(fixture_path, "r").read(), host)
        self.record  = yawhois.record.Record(None, [part])

    def test_status(self):
        eq_(self.record.status, ["serverTransferProhibited", "serverUpdateProhibited", "serverDeleteProhibited", "serverRenewProhibited"])

    def test_available(self):
        eq_(self.record.available, False)

    def test_domain(self):
        eq_(self.record.domain, "nic.college")

    def test_nameservers(self):
        eq_(self.record.nameservers.__class__.__name__, 'list')
        eq_(len(self.record.nameservers), 6)
        eq_(self.record.nameservers[0].__class__.__name__, 'Nameserver')
        eq_(self.record.nameservers[0].name, "ns0.centralnic-dns.com")
        eq_(self.record.nameservers[0].ipv4, None)
        eq_(self.record.nameservers[0].ipv6, None)
        eq_(self.record.nameservers[1].__class__.__name__, 'Nameserver')
        eq_(self.record.nameservers[1].name, "ns1.centralnic-dns.com")
        eq_(self.record.nameservers[1].ipv4, None)
        eq_(self.record.nameservers[1].ipv6, None)
        eq_(self.record.nameservers[2].__class__.__name__, 'Nameserver')
        eq_(self.record.nameservers[2].name, "ns2.centralnic-dns.com")
        eq_(self.record.nameservers[2].ipv4, None)
        eq_(self.record.nameservers[2].ipv6, None)
        eq_(self.record.nameservers[3].__class__.__name__, 'Nameserver')
        eq_(self.record.nameservers[3].name, "ns3.centralnic-dns.com")
        eq_(self.record.nameservers[3].ipv4, None)
        eq_(self.record.nameservers[3].ipv6, None)
        eq_(self.record.nameservers[4].__class__.__name__, 'Nameserver')
        eq_(self.record.nameservers[4].name, "ns4.centralnic-dns.com")
        eq_(self.record.nameservers[4].ipv4, None)
        eq_(self.record.nameservers[4].ipv6, None)
        eq_(self.record.nameservers[5].__class__.__name__, 'Nameserver')
        eq_(self.record.nameservers[5].name, "ns5.centralnic-dns.com")
        eq_(self.record.nameservers[5].ipv4, None)
        eq_(self.record.nameservers[5].ipv6, None)

    def test_admin_contacts(self):
        eq_(self.record.admin_contacts.__class__.__name__, 'list')
        eq_(len(self.record.admin_contacts), 1)
        eq_(self.record.admin_contacts[0].__class__.__name__, 'Contact')
        eq_(self.record.admin_contacts[0].type, yawhois.record.Contact.TYPE_ADMINISTRATIVE)
        eq_(self.record.admin_contacts[0].id, "H5178905")
        eq_(self.record.admin_contacts[0].name, "Domain Administrator")
        eq_(self.record.admin_contacts[0].organization, "XYZ.COM LLC")
        eq_(self.record.admin_contacts[0].address, "2121 E Tropicana Ave Suite #2")
        eq_(self.record.admin_contacts[0].city, "Las Vegas")
        eq_(self.record.admin_contacts[0].zip, "89119")
        eq_(self.record.admin_contacts[0].state, "NV")
        eq_(self.record.admin_contacts[0].country, None)
        eq_(self.record.admin_contacts[0].country_code, "US")
        eq_(self.record.admin_contacts[0].phone, "+1.8009998422")
        eq_(self.record.admin_contacts[0].fax, "+1.7023578299")
        eq_(self.record.admin_contacts[0].email, "icann@xyz.com")

    def test_registered(self):
        eq_(self.record.registered, True)

    def test_created_on(self):
        eq_(self.record.created_on.__class__.__name__, 'datetime')
        eq_(self.record.created_on, time_parse('2013-09-11 00:00:00 UTC'))

    def test_registrar(self):
        eq_(self.record.registrar.__class__.__name__, 'Registrar')
        eq_(self.record.registrar.id, "9999")
        eq_(self.record.registrar.name, "CentralNic Ltd")
        eq_(self.record.registrar.organization, None)
        eq_(self.record.registrar.url, None)

    def test_registrant_contacts(self):
        eq_(self.record.registrant_contacts.__class__.__name__, 'list')
        eq_(len(self.record.registrant_contacts), 1)
        eq_(self.record.registrant_contacts[0].__class__.__name__, 'Contact')
        eq_(self.record.registrant_contacts[0].type, yawhois.record.Contact.TYPE_REGISTRANT)
        eq_(self.record.registrant_contacts[0].id, "H5178905")
        eq_(self.record.registrant_contacts[0].name, "Domain Administrator")
        eq_(self.record.registrant_contacts[0].organization, "XYZ.COM LLC")
        eq_(self.record.registrant_contacts[0].address, "2121 E Tropicana Ave Suite #2")
        eq_(self.record.registrant_contacts[0].city, "Las Vegas")
        eq_(self.record.registrant_contacts[0].zip, "89119")
        eq_(self.record.registrant_contacts[0].state, "NV")
        eq_(self.record.registrant_contacts[0].country, None)
        eq_(self.record.registrant_contacts[0].country_code, "US")
        eq_(self.record.registrant_contacts[0].phone, "+1.8009998422")
        eq_(self.record.registrant_contacts[0].fax, "+1.7023578299")
        eq_(self.record.registrant_contacts[0].email, "icann@xyz.com")

    def test_technical_contacts(self):
        eq_(self.record.technical_contacts.__class__.__name__, 'list')
        eq_(len(self.record.technical_contacts), 1)
        eq_(self.record.technical_contacts[0].__class__.__name__, 'Contact')
        eq_(self.record.technical_contacts[0].type, yawhois.record.Contact.TYPE_TECHNICAL)
        eq_(self.record.technical_contacts[0].id, "H5178905")
        eq_(self.record.technical_contacts[0].name, "Domain Administrator")
        eq_(self.record.technical_contacts[0].organization, "XYZ.COM LLC")
        eq_(self.record.technical_contacts[0].address, "2121 E Tropicana Ave Suite #2")
        eq_(self.record.technical_contacts[0].city, "Las Vegas")
        eq_(self.record.technical_contacts[0].zip, "89119")
        eq_(self.record.technical_contacts[0].state, "NV")
        eq_(self.record.technical_contacts[0].country, None)
        eq_(self.record.technical_contacts[0].country_code, "US")
        eq_(self.record.technical_contacts[0].phone, "+1.8009998422")
        eq_(self.record.technical_contacts[0].fax, "+1.7023578299")
        eq_(self.record.technical_contacts[0].email, "icann@xyz.com")

    def test_updated_on(self):
        eq_(self.record.updated_on.__class__.__name__, 'datetime')
        eq_(self.record.updated_on, time_parse('2014-09-12 00:15:47 UTC'))

    def test_domain_id(self):
        eq_(self.record.domain_id, "D1465621-CNIC")

    def test_expires_on(self):
        eq_(self.record.expires_on.__class__.__name__, 'datetime')
        eq_(self.record.expires_on, time_parse('2015-09-11 23:59:59 UTC'))

    def test_disclaimer(self):
        eq_(self.record.disclaimer, "Access to the whois service is rate limited. For more information, please see https://registrar-console.centralnic.com/pub/whois_guidance.")
