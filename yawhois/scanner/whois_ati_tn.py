from .base import ScannerBase

class WhoisAtiTnScanner(ScannerBase):

    def __init__(self, *args):
        super(WhoisAtiTnScanner, self).__init__(*args)
        self._tokenizer += [
            'skip_empty_line',
            'scan_available',
            'scan_disclaimer',
            'scan_keyvalue'
        ]

    def scan_available(self):
        if self._input.skip("^Domain (.+) not found"):
            self._ast['status:available'] = True
            return True

    def scan_disclaimer(self):
        if self._input.match("All rights reserved"):
            self._ast['field:disclaimer'] = "\n".join(self._scan_lines_to_array("(.+)\n"))
            return True
