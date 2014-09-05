import re

class ParserFactory(object):

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
        'nameservers'
    ]

    # Returns the proper parser instance for given <tt>part</tt>.
    # The parser class is selected according to the
    # value of the <tt>#host</tt> attribute for given <tt>part</tt>.
    #
    # @param  [Whois::Record::Part] part The part to get the parser for.
    #
    # @return [Whois::Record::Parser::Base]
    #         An instance of the specific parser for given part.
    #         The instance is expected to be a child of {Whois::Record::Parser::Base}.
    #
    # @example
    #
    #   # Parser for a known host
    #   Parser.parser_for("whois.example.com")
    #   # => #<Whois::Record::Parser::WhoisExampleCom>
    #
    #   # Parser for an unknown host
    #   Parser.parser_for("missing.example.com")
    #   # => #<Whois::Record::Parser::Blank>
    #
    @classmethod
    def parser_for(part):
        try:
            Parser.parser_class(part.host)(part)
        except Exception, e:
            return Blank(part)

    # Detects the proper parser class according to given <tt>host</tt>
    # and returns the class constant.
    #
    # This method autoloads missing parser classes. If you want to define
    # a custom parser, simple make sure the class is loaded in the Ruby
    # environment before this method is called.
    #
    # @param  [String] host The server host.
    #
    # @return [Class] The instance of Class representing the parser Class
    #         corresponding to <tt>host</tt>. If <tt>host</tt> doesn't have
    #         a specific parser implementation, then returns
    #         the {Whois::Record::Parser::Blank} {Class}.
    #         The {Class} is expected to be a child of {Whois::Record::Parser::Base}.
    # @raises LoadError If the class is not found.
    #
    # @example
    #
    #   Parser.parser_klass("whois.example.com")
    #   # => Whois::Record::Parser::WhoisExampleCom
    #
    @classmethod
    def parser_class(host):
        name = Parser.host_to_parser(host)
        return getattr(".parser", name)

    @classmethod
    def host_to_parser(host):
        host = host.lower()
        host = re.sub(r'[.-]', '_', host)
        host = re.sub(r"(?:^|_)(.)", lambda x: x.group(0)[-1].upper(), host)
        return host

    def __init__(self, record):
        self.record    = record
        self.__parsers = []

    # Returns an array with all host-specific parsers initialized for the parts
    # contained into this parser.
    # The array is lazy-initialized.
    #
    # @return [Array<Whois::Record::Parser::Base>]
    #
    def parsers(self):
        if not self.__parsers:
            self.__parsers = self.init_parsers()
        return self.__parsers

    # Loops through all record parts, for each part
    # tries to guess the appropriate parser object whenever available,
    # and returns the final array of server-specific parsers.
    #
    # Parsers are initialized in reverse order for performance reason.
    #
    # @return [Array<Class>] An array of Class,
    #         where each item is the parts reverse-N specific parser {Class}.
    #         Each {Class} is expected to be a child of {Whois::Record::Parser::Base}.
    #
    # @example
    #
    #   parser.parts
    #   # => [whois.foo.com, whois.bar.com]
    #
    #   parser.parsers
    #   # => [Whois::Record::Parser::WhoisBarCom, Whois::Record::Parser::WhoisFooCom]
    #
    # @api private
    def init_parsers(self):
        return [ Parser.parser_for(part) for part in self.record.parts[::-1]]    

    def is_supporting_property(self):
        pass

    # Checks whether this is an incomplete response.
    #
    # @return [Boolean]
    #
    #
    def is_response_incomplete(self):
        pass

    # Checks whether this is a throttle response.
    #
    # @return [Boolean]
    #
    def is_response_throttled(self):
        pass

    # Checks whether this is an unavailable response.
    #
    # @return [Boolean]
    #
    def is_response_unavailable(self):
        pass