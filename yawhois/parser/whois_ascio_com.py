from .base_icann_compliant import BaseIcannCompliantParser
from ..scanner.base_icann_compliant import BaseIcannCompliantScanner

class WhoisAscioComParser(BaseIcannCompliantParser):
    _scanner = BaseIcannCompliantScanner, {'pattern_available': "^Object not found\n"}
    