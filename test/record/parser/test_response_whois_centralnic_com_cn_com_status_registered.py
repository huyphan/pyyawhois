
# This file is autogenerated. Do not edit it manually.
# If you want change the content of this file, edit
#
#   spec/fixtures/responses/whois.centralnic.com/cn.com/status_registered
#
# and regenerate the tests with the following script
#
#   $ scripts/generate_tests.py
#

from nose.tools import *
from dateutil.parser import parse as time_parse
import yawhois

class TestWhoisCentralnicComCnComStatusRegistered(object):

    def setUp(self):
        fixture_path = "spec/fixtures/responses/whois.centralnic.com/cn.com/status_registered.txt"
        host         = "whois.centralnic.com"
        part         = yawhois.record.Part(open(fixture_path, "r").read(), host)
        self.record  = yawhois.record.Record(None, [part])

    def test_status(self):
        eq_(self.record.status, ["clientTransferProhibited", "serverTransferProhibited"])

    def test_available(self):
        eq_(self.record.available, False)

    def test_domain(self):
        eq_(self.record.domain, "gsn.cn.com")

    def test_nameservers(self):
        eq_(self.record.nameservers.__class__.__name__, 'list')
        eq_(len(self.record.nameservers), 2)
        eq_(self.record.nameservers[0].__class__.__name__, 'Nameserver')
        eq_(self.record.nameservers[0].name, "ns1.meteos.it")
        eq_(self.record.nameservers[1].__class__.__name__, 'Nameserver')
        eq_(self.record.nameservers[1].name, "ns2.meteos.it")

    def test_admin_contacts(self):
        eq_(self.record.admin_contacts.__class__.__name__, 'list')
        eq_(len(self.record.admin_contacts), 1)
        eq_(self.record.admin_contacts[0].__class__.__name__, 'Contact')
        eq_(self.record.admin_contacts[0].type, yawhois.record.Contact.TYPE_ADMINISTRATIVE)
        eq_(self.record.admin_contacts[0].id, "AUTO-DRZK-SNVHSY")
        eq_(self.record.admin_contacts[0].name, "Pauline Ang")
        eq_(self.record.admin_contacts[0].organization, "GSN Electronics Incorporation Pte Ltd")
        eq_(self.record.admin_contacts[0].address, "Straits Trading Building 9 Battery Road 16-08")
        eq_(self.record.admin_contacts[0].city, "Singapore")
        eq_(self.record.admin_contacts[0].zip, "049910")
        eq_(self.record.admin_contacts[0].state, None)
        eq_(self.record.admin_contacts[0].country, None)
        eq_(self.record.admin_contacts[0].country_code, "SG")
        eq_(self.record.admin_contacts[0].phone, "+65.62336919")
        eq_(self.record.admin_contacts[0].fax, None)
        eq_(self.record.admin_contacts[0].email, "abuse@gsn.in")

    def test_registered(self):
        eq_(self.record.registered, True)

    def test_created_on(self):
        eq_(self.record.created_on.__class__.__name__, 'datetime')
        eq_(self.record.created_on, time_parse('2005-11-23 15:44:03 UTC'))

    def test_registrar(self):
        eq_(self.record.registrar.__class__.__name__, 'Registrar')
        eq_(self.record.registrar.id, "H67436")
        eq_(self.record.registrar.name, None)
        eq_(self.record.registrar.organization, "united-domains AG")
        eq_(self.record.registrar.url, "http://www.united-domains.de")

    def test_registrant_contacts(self):
        eq_(self.record.registrant_contacts.__class__.__name__, 'list')
        eq_(len(self.record.registrant_contacts), 1)
        eq_(self.record.registrant_contacts[0].__class__.__name__, 'Contact')
        eq_(self.record.registrant_contacts[0].type, yawhois.record.Contact.TYPE_REGISTRANT)
        eq_(self.record.registrant_contacts[0].id, "H1062079")
        eq_(self.record.registrant_contacts[0].name, "GSN Electronics Incorporation Pte Ltd")
        eq_(self.record.registrant_contacts[0].organization, None)
        eq_(self.record.registrant_contacts[0].address, "Straits Trading Building 9 Battery Road 16-08\nSingapore")
        eq_(self.record.registrant_contacts[0].city, None)
        eq_(self.record.registrant_contacts[0].zip, "049910")
        eq_(self.record.registrant_contacts[0].state, None)
        eq_(self.record.registrant_contacts[0].country, None)
        eq_(self.record.registrant_contacts[0].country_code, "SG")
        eq_(self.record.registrant_contacts[0].phone, "+65.62336919")
        eq_(self.record.registrant_contacts[0].fax, None)
        eq_(self.record.registrant_contacts[0].email, "abuse@gsn.in")

    def test_technical_contacts(self):
        eq_(self.record.technical_contacts.__class__.__name__, 'list')
        eq_(len(self.record.technical_contacts), 1)
        eq_(self.record.technical_contacts[0].__class__.__name__, 'Contact')
        eq_(self.record.technical_contacts[0].type, yawhois.record.Contact.TYPE_TECHNICAL)
        eq_(self.record.technical_contacts[0].id, "C-UHM65D7-TJGULR")
        eq_(self.record.technical_contacts[0].name, "Host Master")
        eq_(self.record.technical_contacts[0].organization, "united-domains AG")
        eq_(self.record.technical_contacts[0].address, "Gautinger Str. 10")
        eq_(self.record.technical_contacts[0].city, "Starnberg")
        eq_(self.record.technical_contacts[0].zip, "82319")
        eq_(self.record.technical_contacts[0].state, "Bayern")
        eq_(self.record.technical_contacts[0].country, None)
        eq_(self.record.technical_contacts[0].country_code, "DE")
        eq_(self.record.technical_contacts[0].phone, "+49.8151368670")
        eq_(self.record.technical_contacts[0].fax, "+49.81513686777")
        eq_(self.record.technical_contacts[0].email, "hostmaster@united-domains.de")

    def test_updated_on(self):
        eq_(self.record.updated_on.__class__.__name__, 'datetime')
        eq_(self.record.updated_on, time_parse('2013-11-26 12:16:45 UTC'))

    def test_domain_id(self):
        eq_(self.record.domain_id, "CNIC-DO323367")

    def test_expires_on(self):
        eq_(self.record.expires_on.__class__.__name__, 'datetime')
        eq_(self.record.expires_on, time_parse('2014-11-23 23:59:59 UTC'))

    def test_disclaimer(self):
        eq_(self.record.disclaimer, "This whois service is provided by CentralNic Ltd and only contains information pertaining to Internet domain names we have registered for our customers. By using this service you are agreeing (1) not to use any information presented here for any purpose other than determining ownership of domain names, (2) not to store or reproduce this data in any way, (3) not to use any high-volume, automated, electronic processes to obtain data from this service. Abuse of this service is monitored and actions in contravention of these terms will result in being permanently blacklisted. All data is (c) CentralNic Ltd https://www.centralnic.com/")
