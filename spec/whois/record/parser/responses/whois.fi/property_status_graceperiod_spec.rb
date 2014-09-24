# encoding: utf-8

# This file is autogenerated. Do not edit it manually.
# If you want change the content of this file, edit
#
#   /spec/fixtures/responses/whois.fi/property_status_graceperiod.expected
#
# and regenerate the tests with the following rake task
#
#   $ rake spec:generate
#

require 'spec_helper'
require 'whois/record/parser/whois.fi.rb'

describe Whois::Record::Parser::WhoisFi, "property_status_graceperiod.expected" do

  subject do
    file = fixture("responses", "whois.fi/property_status_graceperiod.txt")
    part = Whois::Record::Part.new(body: File.read(file))
    described_class.new(part)
  end

  describe "#disclaimer" do
    it do
      expect(subject.disclaimer).to eq("More information is available at https://domain.fi/\nCopyright (c) Finnish Communications Regulatory Authority")
    end
  end
  describe "#domain" do
    it do
      expect(subject.domain).to eq("oogle.fi")
    end
  end
  describe "#domain_id" do
    it do
      expect { subject.domain_id }.to raise_error(Whois::AttributeNotSupported)
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
      expect(subject.created_on).to eq(Time.parse("2012-06-21"))
    end
  end
  describe "#updated_on" do
    it do
      expect(subject.updated_on).to be_a(Time)
      expect(subject.updated_on).to eq(Time.parse("2013-06-22"))
    end
  end
  describe "#expires_on" do
    it do
      expect(subject.expires_on).to be_a(Time)
      expect(subject.expires_on).to eq(Time.parse("2013-06-21"))
    end
  end
  describe "#registrar" do
    it do
      expect { subject.registrar }.to raise_error(Whois::AttributeNotSupported)
    end
  end
  describe "#registrant_contacts" do
    it do
      expect(subject.registrant_contacts).to be_a(Array)
      expect(subject.registrant_contacts).to have(1).items
      expect(subject.registrant_contacts[0]).to be_a(Whois::Record::Contact)
      expect(subject.registrant_contacts[0].type).to eq(Whois::Record::Contact::TYPE_REGISTRANT)
      expect(subject.registrant_contacts[0].id).to eq("NURMI")
      expect(subject.registrant_contacts[0].name).to eq("-")
      expect(subject.registrant_contacts[0].organization).to eq("Minna")
      expect(subject.registrant_contacts[0].address).to eq("Huovitie 3")
      expect(subject.registrant_contacts[0].city).to eq("HELSINKI")
      expect(subject.registrant_contacts[0].zip).to eq("00400")
      expect(subject.registrant_contacts[0].state).to eq(nil)
      expect(subject.registrant_contacts[0].country).to eq(nil)
      expect(subject.registrant_contacts[0].country_code).to eq(nil)
      expect(subject.registrant_contacts[0].phone).to eq("+358201599789")
      expect(subject.registrant_contacts[0].fax).to eq(nil)
      expect(subject.registrant_contacts[0].email).to eq(nil)
      expect(subject.registrant_contacts[0].created_on).to eq(nil)
      expect(subject.registrant_contacts[0].updated_on).to eq(nil)
    end
  end
  describe "#admin_contacts" do
    it do
      expect { subject.admin_contacts }.to raise_error(Whois::AttributeNotSupported)
    end
  end
  describe "#technical_contacts" do
    it do
      expect { subject.technical_contacts }.to raise_error(Whois::AttributeNotSupported)
    end
  end
  describe "#nameservers" do
    it do
      expect(subject.nameservers).to be_a(Array)
      expect(subject.nameservers).to have(2).items
      expect(subject.nameservers[0]).to be_a(Whois::Record::Nameserver)
      expect(subject.nameservers[0].name).to eq("a.ns.netim.net")
      expect(subject.nameservers[1]).to be_a(Whois::Record::Nameserver)
      expect(subject.nameservers[1].name).to eq("b.ns.netim.net")
    end
  end
end
