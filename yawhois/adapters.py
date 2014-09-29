from exceptions import *
from .record import Part, Record
import socket
import re

BUFFER_SIZE = 1024
DEFAULT_WHOIS_PORT = 43
DEFAULT_BIND_HOST = "0.0.0.0"

class SocketHandler(object):
    '''
    The SocketHandler is the default query handler provided with the
    Whois library. It performs the WHOIS query using a synchronous
    socket connection.
    '''


    def __init__(self):
        pass

    # Performs the Socket request.
    #
    # @todo *args might probably be a Hash.
    #
    # @param  [String] query
    # @param  [Array] args
    # @return [String]
    #
    def call(self, query, server, port):
        try:
            return self.execute(query, server, port)
        except Exception, e:
            raise ConnectionError("%s") % (e)

    # Executes the low-level Socket connection.
    #
    # It opens the socket passing given +args+,
    # sends the +query+ and reads the response.
    #
    # @param  [String] query
    # @param  [String] server
    # @param  [String] port
    # @return [String]
    #
    # @api private
    #
    def execute(self, query, server, port):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client.connect((server, port))
            client.send(query+"\r\n")
            buffer = ""
            while True:
                data = client.recv(BUFFER_SIZE)
                if not data:
                    break
                buffer += data
            return buffer
        except Exception, e:
            print e
            client.close()

        return None

class BaseAdapter(object):

    # Default WHOIS request port.
    DEFAULT_WHOIS_PORT = 43

    # Default bind hostname.
    DEFAULT_BIND_HOST = "0.0.0.0"

    __query_handler = SocketHandler()

    # @param  [Symbol] whois_type
    #         The type of WHOIS adapter to define.
    #         Known values are :tld, :ipv4, :ipv6.
    # @param  [String] allocation
    #         The allocation, range or hostname, this server is responsible for.
    # @param  [String, nil] host
    #         The server hostname. Use nil if unknown or not available.
    # @param  [Hash] options Optional adapter properties.
    #
    def __init__(self, whois_type, allocation, host, options = {}):
        self.type       = whois_type
        self.allocation = allocation
        self.host       = host
        self.options    = options or {}
        self.__buffer   = None

    # Checks self and other for equality.
    #
    # @param  [The Whois::Server::Adapters::Base] other
    # @return [Boolean] Returns true if the other is the same object,
    #         or <tt>other</tt> attributes matches this object attributes.
    #
    def __eq__(self, other):

        if self is other: 
            return True

        if type(other) == type(self) and other.type == self.type and \
            other.allocation == self.allocation and other.host == self.host and \
            other.options == self.options:
            return True

        return False

    # Merges given +settings+ into current {#options}.
    #
    # @param  [dict] settings
    # @return [dict] The updated options for this object.
    #
    def configure(self, settings):
        if settings.has_key('host'):
            self.host = settings.get('host') 
        self.options.update(settings)
        
    # Performs a Whois lookup for <tt>string</tt>
    # using the current server adapter.
    #
    # Internally, this method calls {#request}
    # using the Template Method design pattern.
    #
    #   server.lookup("google.com")
    #   # => Whois::Record
    #
    # @param  [String] string The string to be sent as query parameter.
    # @return [Whois::Record]
    #
    def lookup(self, string):
        self.reset_buffer()
        self.request(string)
        return Record(self, self.__buffer)

    def reset_buffer(self):
        self.__buffer = []

    # Store a record part in buffer
    #
    # @param [String] body
    # @param [String] host
    #
    def append_buffer(self, body, host):
        self.__buffer.append(Part(body, host))

    def request(self):
        raise NotImplementedError

    def query(self, query, host, port = None):
        port = port or self.options.get('port') or DEFAULT_WHOIS_PORT
        return self.__query_handler.call(query, host, port)

class VerisignAdapter(BaseAdapter):

    WHOIS_SERVER_PATTERN = re.compile("Whois Server: (.+?)$", re.M)

    def __init__(self, *args):
        super(VerisignAdapter, self).__init__(*args)

    def request(self, string):
        response = self.query("=" + string, self.host)
        self.append_buffer(response, self.host)

        referral = self.extract_referral(response)
        if self.options.get('referral') != False and referral is not None:
            response = self.query(string, referral)
            self.append_buffer(response, referral)

    def extract_referral(self, response):
        if "Domain Name:" in response:
            server = self.WHOIS_SERVER_PATTERN.findall(response)
            if server:
                server = server[-1].strip()
                if server == "not defined":
                    return None

                return server

        return None
