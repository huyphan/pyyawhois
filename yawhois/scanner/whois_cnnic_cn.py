from .base import ScannerBase

class WhoisCnnicCnScanner(ScannerBase):

    def __init__(self, *args):
        super(WhoisCnnicCnScanner, self).__init__(*args)
        self._tokenizer += [
            'skip_empty_line',
            'scan_reserved',
            'scan_reserved_list',
            'scan_available',
            'scan_keyvalue'
        ]

    def scan_available(self):
        if self._input.match("^no matching record"):
            self._ast["status:available"] = True
            self._input.scan_until("\n")
            return True

    def scan_reserved(self):
        if self._input.match("^The domain you requested is prohibited"):
            self._ast["status:reserved"] = True
            self._input.scan_until("\n")
            return True

    def scan_reserved_list(self):
        if self._input.scan("^Sorry, The domain you requested is in the reserved list"):
            self._ast["status:reserved"] = True
            self._input.scan_until("\n")
            return True
