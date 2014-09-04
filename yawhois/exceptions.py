
# The base error class for all <tt>Whois</tt> error classes.
class Error(StandardError):
    pass

# Raised when the connection to the WHOIS server fails.
class ConnectionError(Error):
    pass

# Generic class for server errors.
class ServerError(Error):
    pass

# Raised when we know about a specific functionality
# but this functionality has not been implemented yet.
# This is usually the result of a porting from a third-party library.
#
# Definition is recognized.
class ServerNotImplemented(ServerError):
    pass

# Raised when no WHOIS server is known for this kind of object. (\x05)
#
# Definition is recognized.
class ServerNotSupported(ServerError):
    pass

# Raised when unknown AS number or IP network. (\x06)
#
# Definition is recognized.
class AllocationUnknown(ServerError):
    pass

# Generic class for interfaces not supported.
class InterfaceNotSupported(ServerError):
    pass

# Raised when a server is known to not be available for this kind of object
# or because this specific object doesn't support WHOIS.
class NoInterfaceError(InterfaceNotSupported):
    pass

# Raised when the class has found a server but it doesn't support the
# standard WHOIS interface via port 43. This is the case of some
# specific domains that only provide a web-based WHOIS interface. 
class WebInterfaceError(InterfaceNotSupported):

    def __init__(self, url):
        self.url = url
        super(WebInterfaceError, self).__init__("This TLD has no WHOIS server, but you can access the WHOIS database at `%s'" % url)

# Generic class for parser errors.
class ParserError(Error):
    pass

# Raised when the library hasn't been able to load a valid parser
# according to current settings and you're trying to access a property
# that requires a valid parser.
class ParserNotFound(ParserError):
    pass

# Raised when you are trying to access an attribute that has not been implemented.
class AttributeNotImplemented(ParserError):
    pass

# Raised when you are trying to access an attribute that is not supported.
class AttributeNotSupported(ParserError):
    pass

# Generic class for response errors.
class ResponseError(Error):
    pass

# Raised when attempting to access a property when the response is throttled.
#
# @see Whois::Record::Parser::Base#response_throttled?
class ResponseIsThrottled(ResponseError):
    pass

# Raised when attempting to access a property when the response is unavailable.
#
# @see Whois::Record::Parser::Base#response_unavailable?
class ResponseIsUnavailable(ResponseError):
    pass
