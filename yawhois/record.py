from .parser.factory import ParserFactory
from .utils import array_wrapper

class SuperDict(object):

    properties = []

    def __init__(self, *args, **kwargs):

        for prop in self.properties:
            setattr(self, prop, None)

        for idx, prop in enumerate(args):
            if idx > len(self.properties):
                break
            setattr(self, self.properties[idx], prop)

        for k,v in kwargs.items():
            setattr(self, k, v)

class Contact(SuperDict):

    TYPE_REGISTRANT     = 1
    TYPE_ADMINISTRATIVE = 2
    TYPE_TECHNICAL      = 3        

    properties = ['id', 'type', 'name', 'organization',
                    'address', 'city', 'zip', 'state', 'country', 'country_code',
                    'phone', 'fax', 'email', 'url',
                    'created_on', 'updated_on']

class Part(SuperDict):
    properties = ['body', 'host']

class Registrar(SuperDict):
    properties = ['id', 'name', 'organization', 'url']

class Nameserver(SuperDict):
    properties = ['name', 'ipv4', 'ipv6']

class Record(object):

    METHODS = [
        'contacts', 'is_changed'
    ]

    PROPERTIES = [
        'disclaimer',
        'domain', 'domain_id',
        'status', 'available', 'registered',
        'created_on', 'updated_on', 'expires_on',
        'registrar',
        'registrant_contacts', 'admin_contacts', 'technical_contacts',
        'nameservers',
        'referral_url', 'referral_whois', 
    ]

    # Initializes a new instance with given server and parts
    #
    # @param [Server] server
    # @param [List<Part>] parts
    #
    def __init__(self, server, parts):
        self.server = server
        self.parts  = parts
        self.__parsers = None

    def __str__(self):
        return self.content

    def __getattr__(self, attr):
        if attr in self.PROPERTIES or attr in self.METHODS:
            for parser in self.parsers:
                if parser.is_property_supported(attr):
                    if attr.endswith("contacts") or attr == "nameservers":
                        return array_wrapper(getattr(parser, attr))
                    return getattr(parser, attr)

        return None

    @property
    def parsers(self):
        if self.__parsers is None:
            self.__parsers = [ParserFactory.parser_for(part) for part in self.parts[::-1]]            
        return self.__parsers

    @property
    def content(self):
        return "\n".join([part.body for part in self.parts])

    @property
    def registrant_contact(self):
        for parser in self.parsers:
            if parser.is_property_supported("registrant_contacts"):
                return parser.registrant_contacts[0]

    @property
    def admin_contact(self):
        for parser in self.parsers:
            if parser.is_property_supported("admin_contacts"):
                return parser.admin_contacts[0]

    @property
    def technical_contact(self):
        for parser in self.parsers:
            if parser.is_property_supported("technical_contacts"):
                print parser.technical_contacts
                return parser.technical_contacts[0]

    # Returns a Hash containing all supported properties for this record
    # along with corresponding values.
    #
    # @return [{ property => object }]
    #
    @property
    def properties(self):
        props = {}

        for prop in Record.PROPERTIES:
            if self.is_property_supported(prop):
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

    def is_property_supported(self, prop):
        return any(parser.is_property_supported(prop) for parser in self.parsers)

    # Checks whether this is an incomplete response.
    #
    # @return [Boolean]
    #
    #
    @property
    def response_incomplete(self):
        for parser in self.parsers:
            if parser.is_property_supported("response_incomplete"):
                return parser.response_incomplete

    # Checks whether this is a throttle response.
    #
    # @return [Boolean]
    #
    @property
    def response_throttled(self):
        for parser in self.parsers:
            if parser.is_property_supported("response_throttled"):
                return parser.response_throttled

    # Checks whether this is an unavailable response.
    #
    # @return [Boolean]
    #
    @property
    def response_unavailable(self):
        for parser in self.parsers:
            if parser.is_property_supported("response_unavailable"):
                return parser.response_unavailable