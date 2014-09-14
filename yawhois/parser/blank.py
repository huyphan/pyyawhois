from .base import ParserBase

class BlankParser(ParserBase):

    def __init__(self, *args):
        super(Blank, self).__init__(*args)

    def __getattr__(self, attr):
        raise ParserNotFound("Unable to find a parser for the server `%s`" % self.__part.host)