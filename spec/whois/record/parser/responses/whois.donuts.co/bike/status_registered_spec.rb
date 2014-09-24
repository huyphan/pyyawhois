# encoding: utf-8

# This file is autogenerated. Do not edit it manually.
# If you want change the content of this file, edit
#
#   /spec/fixtures/responses/whois.donuts.co/bike/status_registered.expected
#
# and regenerate the tests with the following rake task
#
#   $ rake spec:generate
#

require 'spec_helper'
require 'whois/record/parser/whois.donuts.co.rb'

describe Whois::Record::Parser::WhoisDonutsCo, "status_registered.expected" do

  subject do
    file = fixture("responses", "whois.donuts.co/bike/status_registered.txt")
    part = Whois::Record::Part.new(body: File.read(file))
    described_class.new(part)
  end

  describe "#domain" do
    it do
      expect(subject.domain).to eq("whereismy.bike")
    end
  end
  describe "#domain_id" do
    it do
      expect(subject.domain_id).to eq("C52CECC9AF044831A7335E8A0ECBC349-D")
    end
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
      expect(subject.created_on).to eq(Time.parse("2014-02-21 22:55:07 UTC"))
    end
  end
  describe "#updated_on" do
    it do
      expect(subject.updated_on).to be_a(Time)
      expect(subject.updated_on).to eq(Time.parse("2014-02-21 22:55:08 UTC"))
    end
  end
  describe "#expires_on" do
    it do
      expect(subject.expires_on).to be_a(Time)
      expect(subject.expires_on).to eq(Time.parse("2015-02-21 22:55:07 UTC"))
    end
  end
  describe "#registrar" do
    it do
      expect(subject.registrar).to be_a(Whois::Record::Registrar)
      expect(subject.registrar.id).to eq("48")
      expect(subject.registrar.name).to eq("Enom, Inc.")
      expect(subject.registrar.organization).to eq("Enom, Inc.")
      expect(subject.registrar.url).to eq(nil)
    end
  end
  describe "#registrant_contacts" do
    it do
      expect(subject.registrant_contacts).to be_a(Array)
      expect(subject.registrant_contacts).to have(1).items
      expect(subject.registrant_contacts[0]).to be_a(Whois::Record::Contact)
      expect(subject.registrant_contacts[0].type).to eq(Whois::Record::Contact::TYPE_REGISTRANT)
      expect(subject.registrant_contacts[0].id).to eq("8ff85c48fbd456f1")
      expect(subject.registrant_contacts[0].name).to eq("whoisguard protected")
      expect(subject.registrant_contacts[0].organization).to eq("WhoisGuard, Inc.")
      expect(subject.registrant_contacts[0].address).to eq("P.O. Box 0823-03411")
      expect(subject.registrant_contacts[0].city).to eq("Panama")
      expect(subject.registrant_contacts[0].zip).to eq("00000")
      expect(subject.registrant_contacts[0].state).to eq("Panama")
      expect(subject.registrant_contacts[0].country).to eq(nil)
      expect(subject.registrant_contacts[0].country_code).to eq("PA")
      expect(subject.registrant_contacts[0].phone).to eq("+507.8365503")
      expect(subject.registrant_contacts[0].fax).to eq("+51.17057182")
      expect(subject.registrant_contacts[0].email).to eq("legal@whoisguard.com")
      expect(subject.registrant_contacts[0].created_on).to eq(nil)
      expect(subject.registrant_contacts[0].updated_on).to eq(nil)
    end
  end
  describe "#admin_contacts" do
    it do
      expect(subject.admin_contacts).to be_a(Array)
      expect(subject.admin_contacts).to have(1).items
      expect(subject.admin_contacts[0]).to be_a(Whois::Record::Contact)
      expect(subject.admin_contacts[0].type).to eq(Whois::Record::Contact::TYPE_ADMINISTRATIVE)
      expect(subject.admin_contacts[0].id).to eq("8ff85c48fbd456f1")
      expect(subject.admin_contacts[0].name).to eq("whoisguard protected")
      expect(subject.admin_contacts[0].organization).to eq("WhoisGuard, Inc.")
      expect(subject.admin_contacts[0].address).to eq("P.O. Box 0823-03411")
      expect(subject.admin_contacts[0].city).to eq("Panama")
      expect(subject.admin_contacts[0].zip).to eq("00000")
      expect(subject.admin_contacts[0].state).to eq("Panama")
      expect(subject.admin_contacts[0].country).to eq(nil)
      expect(subject.admin_contacts[0].country_code).to eq("PA")
      expect(subject.admin_contacts[0].phone).to eq("+507.8365503")
      expect(subject.admin_contacts[0].fax).to eq("+51.17057182")
      expect(subject.admin_contacts[0].email).to eq("legal@whoisguard.com")
      expect(subject.admin_contacts[0].created_on).to eq(nil)
      expect(subject.admin_contacts[0].updated_on).to eq(nil)
    end
  end
  describe "#technical_contacts" do
    it do
      expect(subject.technical_contacts).to be_a(Array)
      expect(subject.technical_contacts).to have(1).items
      expect(subject.technical_contacts[0]).to be_a(Whois::Record::Contact)
      expect(subject.technical_contacts[0].type).to eq(Whois::Record::Contact::TYPE_TECHNICAL)
      expect(subject.technical_contacts[0].id).to eq("8ff85c48fbd456f1")
      expect(subject.technical_contacts[0].name).to eq("whoisguard protected")
      expect(subject.technical_contacts[0].organization).to eq("WhoisGuard, Inc.")
      expect(subject.technical_contacts[0].address).to eq("P.O. Box 0823-03411")
      expect(subject.technical_contacts[0].city).to eq("Panama")
      expect(subject.technical_contacts[0].zip).to eq("00000")
      expect(subject.technical_contacts[0].state).to eq("Panama")
      expect(subject.technical_contacts[0].country).to eq(nil)
      expect(subject.technical_contacts[0].country_code).to eq("PA")
      expect(subject.technical_contacts[0].phone).to eq("+507.8365503")
      expect(subject.technical_contacts[0].fax).to eq("+51.17057182")
      expect(subject.technical_contacts[0].email).to eq("legal@whoisguard.com")
      expect(subject.technical_contacts[0].created_on).to eq(nil)
      expect(subject.technical_contacts[0].updated_on).to eq(nil)
    end
  end
  describe "#nameservers" do
    it do
      expect(subject.nameservers).to be_a(Array)
      expect(subject.nameservers).to have(5).items
      expect(subject.nameservers[0]).to be_a(Whois::Record::Nameserver)
      expect(subject.nameservers[0].name).to eq("dns5.registrar-servers.com")
      expect(subject.nameservers[0].ipv4).to eq(nil)
      expect(subject.nameservers[0].ipv6).to eq(nil)
      expect(subject.nameservers[1]).to be_a(Whois::Record::Nameserver)
      expect(subject.nameservers[1].name).to eq("dns3.registrar-servers.com")
      expect(subject.nameservers[1].ipv4).to eq(nil)
      expect(subject.nameservers[1].ipv6).to eq(nil)
      expect(subject.nameservers[2]).to be_a(Whois::Record::Nameserver)
      expect(subject.nameservers[2].name).to eq("dns2.registrar-servers.com")
      expect(subject.nameservers[2].ipv4).to eq(nil)
      expect(subject.nameservers[2].ipv6).to eq(nil)
      expect(subject.nameservers[3]).to be_a(Whois::Record::Nameserver)
      expect(subject.nameservers[3].name).to eq("dns1.registrar-servers.com")
      expect(subject.nameservers[3].ipv4).to eq(nil)
      expect(subject.nameservers[3].ipv6).to eq(nil)
      expect(subject.nameservers[4]).to be_a(Whois::Record::Nameserver)
      expect(subject.nameservers[4].name).to eq("dns4.registrar-servers.com")
      expect(subject.nameservers[4].ipv4).to eq(nil)
      expect(subject.nameservers[4].ipv6).to eq(nil)
    end
  end
end
