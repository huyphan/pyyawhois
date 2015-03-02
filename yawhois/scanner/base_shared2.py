from .base import ScannerBase

class BaseShared2Scanner(ScannerBase):

    def __init__(self, *args):
        super(BaseShared2Scanner, self).__init__(*args)
        self._tokenizer += [
            'skip_blank_line',
            'scan_available',
            'scan_keyvalue',
            'skip_lastupdate',
            'skip_fuffa'
        ]

    def scan_available(self):
        if self._input.scan("^Not found: (.+)\n"):
            self._ast["Domain Name"] = self._input.results[1]
            self._ast["status:available"] = True
            return True

    def skip_last_update(self):
        return self._input.skip(">>>(.+?)<<<\n")

    def skip_fuffa(self):
        return self._input.skip("^\S(.+)\n")
