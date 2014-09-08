from .base import ParserBase

class ScannableParserBase(ParserBase):

    '''
    ScannableParserBase tries to emulate a super-simple Abstract Syntax Tree structure
    including method for accessing ast nodes.

    == Usage

    Inherit ScannableParserBase class and set the `__scanner` value.

    class ParserFoo(ScannableParserBase):
        __scanner = ScannerFoo

    Now you can access the AST using the <tt>node</tt> method.

    node("created_on")
    # => "2009-12-12"
    '''

    __scanner = None
    __ast     = None

    def node(self, key):
        return self.ast[key]

    def parse(self):
        if type(self.__scanner) == list:
            scanner  = self.__scanner[0]
            settings = self.__scanner[-1]
        else:
            scanner  = self.__scanner
            settings = {}

        return scanner(settings).parse(self.content_for_scanner)

    @property
    def ast(self):
        if self.__ast is None:
            self.__ast = self.parse()

        return self.__ast