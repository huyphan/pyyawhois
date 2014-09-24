# encoding: utf-8

# This file is autogenerated. Do not edit it manually.
# If you want change the content of this file, edit
#
#   /spec/fixtures/responses/whois.dreamhost.com/status_registered.expected
#
# and regenerate the tests with the following rake task
#
#   $ rake spec:generate
#

require 'spec_helper'
require 'whois/record/parser/whois.dreamhost.com.rb'

describe Whois::Record::Parser::WhoisDreamhostCom, "status_registered.expected" do

  subject do
    file = fixture("responses", "whois.dreamhost.com/status_registered.txt")
    part = Whois::Record::Part.new(body: File.read(file))
    described_class.new(part)
  end

  describe "#status" do
    it do
      expect(subject.status).to eq(:registered)
    end
  end
  describe "#available?" do
    it do
      expect(subject.available?).to eq(false)
    end
  end
  describe "#registered?" do
    it do
      expect(subject.registered?).to eq(true)
    end
  end
  describe "#created_on" do
    it do
      expect(subject.created_on).to be_a(Time)
      expect(subject.created_on).to eq(Time.parse("1997-09-22 21:00:00 UTC"))
    end
  end
  describe "#updated_on" do
    it do
      expect(subject.updated_on).to be_a(Time)
      expect(subject.updated_on).to eq(Time.parse("2013-12-14 16:53:27 UTC"))
    end
  end
  describe "#expires_on" do
    it do
      expect(subject.expires_on).to be_a(Time)
      expect(subject.expires_on).to eq(Time.parse("2015-09-22 04:00:00 UTC"))
    end
  end
  describe "#registrar" do
    it do
      expect(subject.registrar).to be_a(Whois::Record::Registrar)
      expect(subject.registrar.id).to eq("431")
      expect(subject.registrar.name).to eq("DREAMHOST")
      expect(subject.registrar.organization).to eq("DREAMHOST")
      expect(subject.registrar.url).to eq("www.dreamhost.com")
    end
  end
  describe "#registrant_contacts" do
    it do
      expect(subject.registrant_contacts).to be_a(Array)
      expect(subject.registrant_contacts).to have(1).items
      expect(subject.registrant_contacts[0]).to be_a(Whois::Record::Contact)
      expect(subject.registrant_contacts[0].type).to eq(Whois::Record::Contact::TYPE_REGISTRANT)
      expect(subject.registrant_contacts[0].name).to eq("PRIVATE REGISTRANT")
      expect(subject.registrant_contacts[0].organization).to eq("A HAPPY DREAMHOST CUSTOMER")
      expect(subject.registrant_contacts[0].address).to eq("417 ASSOCIATED RD #324, C/O DREAMHOST.COM")
      expect(subject.registrant_contacts[0].city).to eq("BREA")
      expect(subject.registrant_contacts[0].zip).to eq("92821")
      expect(subject.registrant_contacts[0].state).to eq("CA")
      expect(subject.registrant_contacts[0].country_code).to eq("US")
      expect(subject.registrant_contacts[0].phone).to eq("+1.7147064182")
      expect(subject.registrant_contacts[0].fax).to eq("")
      expect(subject.registrant_contacts[0].email).to eq("YW3GAZMC77BTMTF@PROXY.DREAMHOST.COM")
    end
  end
  describe "#admin_contacts" do
    it do
      expect(subject.admin_contacts).to be_a(Array)
      expect(subject.admin_contacts).to have(1).items
      expect(subject.admin_contacts[0]).to be_a(Whois::Record::Contact)
      expect(subject.admin_contacts[0].type).to eq(Whois::Record::Contact::TYPE_ADMINISTRATIVE)
      expect(subject.admin_contacts[0].name).to eq("PRIVATE REGISTRANT")
      expect(subject.admin_contacts[0].organization).to eq("A HAPPY DREAMHOST CUSTOMER")
      expect(subject.admin_contacts[0].address).to eq("417 ASSOCIATED RD #324, C/O DREAMHOST.COM")
      expect(subject.admin_contacts[0].city).to eq("BREA")
      expect(subject.admin_contacts[0].zip).to eq("92821")
      expect(subject.admin_contacts[0].state).to eq("CA")
      expect(subject.admin_contacts[0].country_code).to eq("US")
      expect(subject.admin_contacts[0].phone).to eq("+1.7147064182")
      expect(subject.admin_contacts[0].fax).to eq("")
      expect(subject.admin_contacts[0].email).to eq("YW3GAZMC77BTMTF@PROXY.DREAMHOST.COM")
    end
  end
  describe "#technical_contacts" do
    it do
      expect(subject.technical_contacts).to be_a(Array)
      expect(subject.technical_contacts).to have(1).items
      expect(subject.technical_contacts[0]).to be_a(Whois::Record::Contact)
      expect(subject.technical_contacts[0].type).to eq(Whois::Record::Contact::TYPE_TECHNICAL)
      expect(subject.technical_contacts[0].name).to eq("PRIVATE REGISTRANT")
      expect(subject.technical_contacts[0].organization).to eq("A HAPPY DREAMHOST CUSTOMER")
      expect(subject.technical_contacts[0].address).to eq("417 ASSOCIATED RD #324, C/O DREAMHOST.COM")
      expect(subject.technical_contacts[0].city).to eq("BREA")
      expect(subject.technical_contacts[0].zip).to eq("92821")
      expect(subject.technical_contacts[0].state).to eq("CA")
      expect(subject.technical_contacts[0].country_code).to eq("US")
      expect(subject.technical_contacts[0].phone).to eq("+1.7147064182")
      expect(subject.technical_contacts[0].fax).to eq("")
      expect(subject.technical_contacts[0].email).to eq("YW3GAZMC77BTMTF@PROXY.DREAMHOST.COM")
    end
  end
  describe "#nameservers" do
    it do
      expect(subject.nameservers).to be_a(Array)
      expect(subject.nameservers).to have(3).items
      expect(subject.nameservers[0]).to be_a(Whois::Record::Nameserver)
      expect(subject.nameservers[0].name).to eq("ns1.dreamhost.com")
      expect(subject.nameservers[1]).to be_a(Whois::Record::Nameserver)
      expect(subject.nameservers[1].name).to eq("ns2.dreamhost.com")
      expect(subject.nameservers[2]).to be_a(Whois::Record::Nameserver)
      expect(subject.nameservers[2].name).to eq("ns3.dreamhost.com")
    end
  end
end
