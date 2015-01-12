from .base_afilias2 import BaseAfilias2Parser
from ..scanner.base_afilias import BaseAfiliasScanner

class WhoisAfiliasInfoParser(BaseAfilias2Parser):
    _scanner = BaseAfiliasScanner, { 'pattern_disclaimer': '^(Access to|The  WHOIS information)'}
    