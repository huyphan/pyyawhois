from ..scanner.base_icann_compliant import BaseIcannCompliantScanner
from .base_icann_compliant import BaseIcannCompliantParser

class WhoisCorporatedomainsComParser(BaseIcannCompliantParser):

    _scanner = BaseIcannCompliantScanner, { "pattern_available": "^No match for"}