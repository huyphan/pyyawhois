from .parser import *

class Part(object):

    def __init__(self, body, host):
        self.body = body
        self.host = host

class Record(object):

    # Initializes a new instance with given server and parts
    #
    # @param [Server] server
    # @param [List<Part>] parts
    #
    def __init__(self, server, parts):
        self.server = server
        self.parts  = parts
        self.__parser = None      

    def __str__(self):
        return self.content

    @property
    def content(self):
        return "\n".join([part.body for part in self.parts])

    @property
    def parser(self):
        if self.__parser == None:
            self.__parser = Parser()

        return self.__parser

    def is_supporting_property(self, prop):
        return self.parser.is_supporting_property(prop)

    @property
    def registrant_contact(self):
        if self.is_supporting_property('registrant_contacts'):
            return self.parser.registrant_contacts[0]

    @property
    def admin_contact(self):
        if self.is_supporting_property('admin_contacts'):
            return self.parser.admin_contacts[0]

    @property
    def technical_contact(self):
        if self.is_supporting_property('technical_contacts'):
            return self.parser.technical_contacts[0]

    # Returns a Hash containing all supported properties for this record
    # along with corresponding values.
    #
    # @return [{ property => object }]
    #
    @property
    def properties(self):
        props = {}

        for prop in Parser.PROPERTIES:
            if self.is_supporting_property(prop):
                props[prop] = self.prop

        return props

    # Collects and returns all the contacts.
    #
    # @return [List<Contact>]
    #
    #
    @property   
    def contacts(self):
        return self.parser.contacts

    # Checks whether this is an incomplete response.
    #
    # @return [Boolean]
    #
    #
    def is_response_incomplete(self):
        return self.parser.is_response_incomplete()

    # Checks whether this is a throttle response.
    #
    # @return [Boolean]
    #
    def is_response_throttled(self):
        return self.parser.response_throttled()

    # Checks whether this is an unavailable response.
    #
    # @return [Boolean]
    #
    def is_response_unavailable(self):
        return self.parser.response_unavailable()
