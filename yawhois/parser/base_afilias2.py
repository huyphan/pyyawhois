import re
from dateutil import parser as timeparser
from .base_afilias import BaseAfiliasParser
from ..scanner.base_afilias import BaseAfiliasScanner
from ..utils import array_wrapper
from ..record import *
from ..exceptions import ParserError

class BaseAfilias2Parser(BaseAfiliasParser):

    @property
    def status(self):
        return array_wrapper(self.node("Domain Status"))

    @property
    def created_on(self):
        if self.node("Creation Date"):
            return timeparser.parse(self.node("Creation Date"))

    @property
    def updated_on(self):
        if self.node("Updated Date"):
            return timeparser.parse(self.node("Updated Date"))

    @property
    def expires_on(self):
        if self.node("Registry Expiry Date"):
            return timeparser.parse(self.node("Registry Expiry Date"))