from .base import ScannerBase

class WhoisCentralnicComScanner(ScannerBase):

    def __init__(self, *args):
        super(WhoisCentralnicComScanner, self).__init__(*args)
        self._tokenizer += [
            'skip_empty_line',
            'scan_available',
            'scan_disclaimer',
            'scan_keyvalue'
        ]

    def scan_available(self):
        if self._input.skip("^DOMAIN NOT FOUND\n"):
            self._ast["status:available"] = True
            return True

    def scan_disclaimer(self):
        if self._input.match("^\S([^:]+)\n"):
            self._ast["field:disclaimer"] = " ".join(self._scan_lines_to_array("(.+)\n"))
            return True
