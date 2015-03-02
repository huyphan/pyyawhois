from .base import ScannerBase

class WhoisAudnsNetAuScanner(ScannerBase):

    def __init__(self, *args):
        super(WhoisAudnsNetAuScanner, self).__init__(*args)
        self._tokenizer += [
            'skip_empty_line',
            'scan_available',
            'scan_keyvalue'
        ]

    def scan_available(self):
        if self._input.skip("^No Data Found\n"):
            self._ast['status:available'] = True
            return True