# encoding: utf-8

# This file is autogenerated. Do not edit it manually.
# If you want change the content of this file, edit
#
#   /spec/fixtures/responses/whois.nic.cd/status_registered.expected
#
# and regenerate the tests with the following rake task
#
#   $ rake spec:generate
#

require 'spec_helper'
require 'whois/record/parser/whois.nic.cd.rb'

describe Whois::Record::Parser::WhoisNicCd, "status_registered.expected" do

  subject do
    file = fixture("responses", "whois.nic.cd/status_registered.txt")
    part = Whois::Record::Part.new(body: File.read(file))
    described_class.new(part)
  end

  describe "#domain" do
    it do
      expect(subject.domain).to eq("google.cd")
    end
  end
  describe "#domain_id" do
    it do
      expect(subject.domain_id).to eq("5758-CD")
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
      expect(subject.created_on).to eq(nil)
    end
  end
  describe "#updated_on" do
    it do
      expect(subject.updated_on).to eq(nil)
    end
  end
  describe "#expires_on" do
    it do
      expect(subject.expires_on).to eq(nil)
    end
  end
  describe "#registrar" do
    it do
      expect(subject.registrar).to be_a(Whois::Record::Registrar)
      expect(subject.registrar.id).to eq(nil)
      expect(subject.registrar.name).to eq("MARKMONITOR")
      expect(subject.registrar.organization).to eq(nil)
      expect(subject.registrar.url).to eq(nil)
    end
  end
  describe "#nameservers" do
    it do
      expect(subject.nameservers).to be_a(Array)
      expect(subject.nameservers).to have(0).items
    end
  end
end
