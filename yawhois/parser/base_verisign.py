from .base_scannable import ScannableParserBase
from ..scanner.verisign import VerisignScanner

class VerisignParserBase(ScannableParserBase):

    _scanner = VerisignScanner

    @property
    def disclaimer(self):
        return self.node("Disclaimer")

    @property
    def domain(self):
        return self.node("Domain Name").lower()