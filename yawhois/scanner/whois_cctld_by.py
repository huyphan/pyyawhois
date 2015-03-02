from .base import ScannerBase

class WhoisCctldByScanner(ScannerBase):

    def __init__(self, *args):
        super(WhoisCctldByScanner, self).__init__(*args)
        self._tokenizer += [
            'skip_empty_line',
            'skip_dash_line',
            'scan_available',
            'scan_keyvalue',
            'skip_provider_signature'
        ]

    def scan_available(self):
        if self._input.skip("^Object does not exist"):
            self._ast["status:available"] = True
            return True
        
    def skip_dash_line(self):
        return self._input.skip("^-+\n")

    def skip_provider_signature(self):
        return self._input.scan("^(.+)\n")
