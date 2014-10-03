from dateutil import parser as timeparser
from .base_afilias import BaseAfiliasParser
from ..utils import array_wrapper

class WhoisAeroParser(BaseAfiliasParser):

    @property
    def status(self):
        return array_wrapper(self.node("Domain Status"))

    @property
    def updated_on(self):
        if self.node("Updated On"):
            return timeparser.parse(self.node("Updated On"))

    @property
    def expires_on(self):
        if self.node("Expires On"):
            return timeparser.parse(self.node("Expires On"))
