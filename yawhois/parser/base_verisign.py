from .base_scannable import ScannableParserBase

class VerisignBase(ScannableParserBase):

    @property
    def disclaimer(self):
        return self.node("Disclaimer")
