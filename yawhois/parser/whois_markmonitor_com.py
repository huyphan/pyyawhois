from ..scanner.base_icann_compliant import BaseIcannCompliantScanner
from .base_icann_compliant import BaseIcannCompliantParser

class WhoisMarkmonitorComParser(BaseIcannCompliantParser):

    _scanner = BaseIcannCompliantScanner, { "pattern_available": "^No match for", "pattern_throttled": "^You have exceeded your quota of queries\."}

    def response_throttled(self):
        return self.nod("response:throttled")