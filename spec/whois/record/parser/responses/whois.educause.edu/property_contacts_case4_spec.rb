# encoding: utf-8

# This file is autogenerated. Do not edit it manually.
# If you want change the content of this file, edit
#
#   /spec/fixtures/responses/whois.educause.edu/property_contacts_case4.expected
#
# and regenerate the tests with the following rake task
#
#   $ rake spec:generate
#

require 'spec_helper'
require 'whois/record/parser/whois.educause.edu.rb'

describe Whois::Record::Parser::WhoisEducauseEdu, "property_contacts_case4.expected" do

  subject do
    file = fixture("responses", "whois.educause.edu/property_contacts_case4.txt")
    part = Whois::Record::Part.new(body: File.read(file))
    described_class.new(part)
  end

  describe "#admin_contacts" do
    it do
      expect(subject.admin_contacts).to be_a(Array)
      expect(subject.admin_contacts).to have(1).items
      expect(subject.admin_contacts[0]).to be_a(Whois::Record::Contact)
      expect(subject.admin_contacts[0].id).to eq(nil)
      expect(subject.admin_contacts[0].name).to eq("ITS Business Office\nSyracuse University\nInformation Technology and Services\nCenter for Science and Technology")
      expect(subject.admin_contacts[0].organization).to eq(nil)
      expect(subject.admin_contacts[0].address).to eq(nil)
      expect(subject.admin_contacts[0].city).to eq("Syracuse")
      expect(subject.admin_contacts[0].zip).to eq("13244")
      expect(subject.admin_contacts[0].state).to eq("NY")
      expect(subject.admin_contacts[0].country).to eq("UNITED STATES")
      expect(subject.admin_contacts[0].country_code).to eq(nil)
      expect(subject.admin_contacts[0].phone).to eq("(315) 443-6189")
      expect(subject.admin_contacts[0].fax).to eq(nil)
      expect(subject.admin_contacts[0].email).to eq("itsoffice@syr.edu")
    end
  end
end
