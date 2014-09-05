class Record(Object):

    # Initializes a new instance with given server and parts
    #
    # @param [Server] server
    # @param [Array<Part>] parts
    #
    def __init__(self, server, parts):
        self.server = server
        self.parts  = parts

