from .base import ScannerBase

class BaseCocca2Scanner(ScannerBase):
        
    DISCLAIMER_MATCHES = [
        "TERMS OF USE:", # global
        "Terminos de Uso:", # whois.nic.hn
        "The data in the WHOIS database of Meridian", # whois.meridiantld.net
        "This information is provided", # whois.gg
    ]

    
    def __init__(self, *args):
        super(BaseCocca2Scanner, self).__init__(*args)
        self._tokenizer += [
            'skip_empty_line',
            'scan_disclaimer',
            'skip_lastupdate',
            'skip_token_additionalsection',
            'scan_keyvalue'
        ]

    def scan_disclaimer(self):
        if self._input.match("^" + "|".join(self.DISCLAIMER_MATCHES)):
            self._ast["field:disclaimer"] = self._input.scan_until(">>>") or self._input.scan_until("\Z")
            return True
            
    def scan_skip_lastupdate(self):
        return self._input.skip(">>>(.+?)<<<\n")

    def skip_token_additionalsection(self):
        return  self._input.skip("Additional Section\n")
