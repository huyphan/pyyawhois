# The SocketHandler is the default query handler provided with the
# Whois library. It performs the WHOIS query using a synchronous
# socket connection.
class SocketHandler(object):

    # Array of connection errors to rescue
    # and wrap into a {Whois::ConnectionError}
    RESCUABLE_CONNECTION_ERRORS = [
        SystemCallError,
        SocketError,
    ]

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
        except RESCUABLE_CONNECTION_ERRORS, error:
            raise ConnectionError("%s: %s") % (error, error.message)

      

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
    def __init__(self, whois_type, allocation, host, options = {})
        self.type       = whois_type
        self.allocation = allocation
        self.host       = host
        self.options    = options or {}
    end