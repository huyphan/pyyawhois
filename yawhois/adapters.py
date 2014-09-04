from exceptions import *
import socket

BUFFER_SIZE = 1024

# The SocketHandler is the default query handler provided with the
# Whois library. It performs the WHOIS query using a synchronous
# socket connection.
class SocketHandler(object):

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
    def call(self, query, *args):
        try:
            self.execute(query, *args)
        except Excpetion, e:
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
        except:
            client.close()

        return None

class Base(object):

    # Default WHOIS request port.
    DEFAULT_WHOIS_PORT = 43

    # Default bind hostname.
    DEFAULT_BIND_HOST = "0.0.0.0"

    _query_handler = socket.socket()

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
    def lookup(string):
      buffer_start do |buffer|
        request(string)
        Whois::Record.new(self, buffer)
      end
