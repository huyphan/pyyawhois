
# This file is autogenerated. Do not edit it manually.
# If you want change the content of this file, edit
#
#   spec/fixtures/responses/whois.centralnic.com/ru.com/status_registered
#
# and regenerate the tests with the following script
#
#   $ scripts/generate_tests.py
#

from nose.tools import *
from dateutil.parser import parse as time_parse
import yawhois

class TestWhoisCentralnicComRuComStatusRegistered(object):

    def setUp(self):
        fixture_path = "spec/fixtures/responses/whois.centralnic.com/ru.com/status_registered.txt"
        host         = "whois.centralnic.com"
        part         = yawhois.record.Part(open(fixture_path, "r").read(), host)
        self.record  = yawhois.record.Record(None, [part])

    def test_status(self):
        eq_(self.record.status, ["ok"])

    def test_available(self):
        eq_(self.record.available, False)

    def test_domain(self):
        eq_(self.record.domain, "srk.ru.com")

    def test_nameservers(self):
        eq_(self.record.nameservers.__class__.__name__, 'list')
        eq_(len(self.record.nameservers), 2)
        eq_(self.record.nameservers[0].__class__.__name__, 'Nameserver')
        eq_(self.record.nameservers[0].name, "ns7.zoneedit.com")
        eq_(self.record.nameservers[1].__class__.__name__, 'Nameserver')
        eq_(self.record.nameservers[1].name, "ns12.zoneedit.com")

    def test_admin_contacts(self):
        eq_(self.record.admin_contacts.__class__.__name__, 'list')
        eq_(len(self.record.admin_contacts), 1)
        eq_(self.record.admin_contacts[0].__class__.__name__, 'Contact')
        eq_(self.record.admin_contacts[0].type, yawhois.record.Contact.TYPE_ADMINISTRATIVE)
        eq_(self.record.admin_contacts[0].id, "H265405")
        eq_(self.record.admin_contacts[0].name, "Anthony Lloyd")
        eq_(self.record.admin_contacts[0].organization, "SRK Consulting (UK) Limited")
        eq_(self.record.admin_contacts[0].address, "5th Floor\nChurchill House\n17 Churchill Way")
        eq_(self.record.admin_contacts[0].city, "Cardiff")
        eq_(self.record.admin_contacts[0].zip, "CF10 2HH")
        eq_(self.record.admin_contacts[0].state, None)
        eq_(self.record.admin_contacts[0].country, None)
        eq_(self.record.admin_contacts[0].country_code, "GB")
        eq_(self.record.admin_contacts[0].phone, "+44.2920348150")
        eq_(self.record.admin_contacts[0].fax, None)
        eq_(self.record.admin_contacts[0].email, "alloyd@srk.co.uk")

    def test_registered(self):
        eq_(self.record.registered, True)

    def test_created_on(self):
        eq_(self.record.created_on.__class__.__name__, 'datetime')
        eq_(self.record.created_on, time_parse('2006-07-31 10:06:04 UTC'))

    def test_registrar(self):
        eq_(self.record.registrar, None)

    def test_registrant_contacts(self):
        eq_(self.record.registrant_contacts.__class__.__name__, 'list')
        eq_(len(self.record.registrant_contacts), 1)
        eq_(self.record.registrant_contacts[0].__class__.__name__, 'Contact')
        eq_(self.record.registrant_contacts[0].type, yawhois.record.Contact.TYPE_REGISTRANT)
        eq_(self.record.registrant_contacts[0].id, "H1037013")
        eq_(self.record.registrant_contacts[0].name, "Anthony Lloyd, SRK Consulting (UK) Limited")
        eq_(self.record.registrant_contacts[0].organization, None)
        eq_(self.record.registrant_contacts[0].address, "5th Floor\nChurchill House\n17 Churchill Way")
        eq_(self.record.registrant_contacts[0].city, "Cardiff")
        eq_(self.record.registrant_contacts[0].zip, "CF10 2HH")
        eq_(self.record.registrant_contacts[0].state, None)
        eq_(self.record.registrant_contacts[0].country, None)
        eq_(self.record.registrant_contacts[0].country_code, "GB")
        eq_(self.record.registrant_contacts[0].phone, "+44.2920348150")
        eq_(self.record.registrant_contacts[0].fax, None)
        eq_(self.record.registrant_contacts[0].email, "alloyd@srk.co.uk")

    def test_technical_contacts(self):
        eq_(self.record.technical_contacts.__class__.__name__, 'list')
        eq_(len(self.record.technical_contacts), 1)
        eq_(self.record.technical_contacts[0].__class__.__name__, 'Contact')
        eq_(self.record.technical_contacts[0].type, yawhois.record.Contact.TYPE_TECHNICAL)
        eq_(self.record.technical_contacts[0].id, "H265405")
        eq_(self.record.technical_contacts[0].name, "Anthony Lloyd")
        eq_(self.record.technical_contacts[0].organization, "SRK Consulting (UK) Limited")
        eq_(self.record.technical_contacts[0].address, "5th Floor\nChurchill House\n17 Churchill Way")
        eq_(self.record.technical_contacts[0].city, "Cardiff")
        eq_(self.record.technical_contacts[0].zip, "CF10 2HH")
        eq_(self.record.technical_contacts[0].state, None)
        eq_(self.record.technical_contacts[0].country, None)
        eq_(self.record.technical_contacts[0].country_code, "GB")
        eq_(self.record.technical_contacts[0].phone, "+44.2920348150")
        eq_(self.record.technical_contacts[0].fax, None)
        eq_(self.record.technical_contacts[0].email, "alloyd@srk.co.uk")

    def test_updated_on(self):
        eq_(self.record.updated_on.__class__.__name__, 'datetime')
        eq_(self.record.updated_on, time_parse('2012-07-10 08:16:19 UTC'))

    def test_domain_id(self):
        eq_(self.record.domain_id, "CNIC-DO450826")

    def test_expires_on(self):
        eq_(self.record.expires_on.__class__.__name__, 'datetime')
        eq_(self.record.expires_on, time_parse('2014-07-31 23:59:59 UTC'))

    def test_disclaimer(self):
        eq_(self.record.disclaimer, "This whois service is provided by CentralNic Ltd and only contains information pertaining to Internet domain names we have registered for our customers. By using this service you are agreeing (1) not to use any information presented here for any purpose other than determining ownership of domain names, (2) not to store or reproduce this data in any way, (3) not to use any high-volume, automated, electronic processes to obtain data from this service. Abuse of this service is monitored and actions in contravention of these terms will result in being permanently blacklisted. All data is (c) CentralNic Ltd https://www.centralnic.com/")