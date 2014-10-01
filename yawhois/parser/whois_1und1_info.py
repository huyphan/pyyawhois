from ..scanner.base_icann_compliant import BaseIcannCompliantScanner
from .base_icann_compliant import BaseIcannCompliantParser

class Whois1und1InfoParser(BaseIcannCompliantParser):

    _scanner = BaseIcannCompliantScanner, { "pattern_available": "Domain (.+) is not registered here."}
