import re
import sys
from ..exceptions import ParserNotFound

class ParserFactory(object):

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
    @staticmethod
    def parser_for(part):
        try:
            return ParserFactory.parser_class(part.host)(part)
        except Exception, e:
            print e
            module = __import__('blank', globals())
            return getattr(module, 'Blank')(part)

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
    @staticmethod
    def parser_class(host):
        module_name, class_name = ParserFactory.host_to_parser(host)
        module = getattr(__import__("", globals(), fromlist=["parser"]), module_name)
        return getattr(module, class_name)

    @staticmethod
    def host_to_parser(host):
        host = host.lower()
        module_name = re.sub(r'[.-]', '_', host)
        class_name = re.sub(r"(?:^|_)(.)", lambda x: x.group(0)[-1].upper(), module_name) + "Parser"

        return module_name, class_name

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