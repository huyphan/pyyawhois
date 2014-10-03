from .base import ScannerBase

class BaseAfiliasScanner(ScannerBase):

    def __init__(self, *args):
        super(BaseAfiliasScanner, self).__init__(*args)       
        self._tokenizer += [
            'skip_empty_line',
            'scan_available',
            'scan_reserved',
            'scan_throttled',
            'scan_disclaimer',
            'scan_keyvalue'
        ]

    def scan_available(self):
        if self._input.scan("^NOT FOUND\n"):
            self._ast["status:available"] = True
            return True

    def scan_reserved(self):
        if self._input.scan("^Reserved by ICM Registry\n"):
            self._ast["status:reserved"] = True
            return True

    def scan_throttled(self):
        if self._input.match("^WHOIS LIMIT EXCEEDED"):
            self._ast["response:throttled"] = True
            return self._input.skip("^.+\n")

    def scan_disclaimer(self):
        if self._settings.get("pattern_disclaimer"):
            if self._input.match(self._settings["pattern_disclaimer"]):
                self._ast["field:disclaimer"] = " ".join(self._scan_lines_to_array("^(.+)\n"))
                return True
        elif self._input.pos == 0 and self._input.match("^(.+\n){3,}\n"):
            self._ast["field:disclaimer"] = " ".join(self._scan_lines_to_array("^(.+)\n"))
            return True
