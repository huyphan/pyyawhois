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

    _scanner = None
    _ast    = None

    def node(self, key):
        if self._ast is None:
            self._ast = self.parse()
        return self._ast.get(key)

    def parse(self):
        if isinstance(self._scanner, (list, tuple)):
            scanner  = self._scanner[0]
            settings = self._scanner[-1]
        else:
            scanner  = self._scanner
            settings = {}

        return scanner(settings).parse(self.content_for_scanner)