from .base import ScannerBase

class BaseShared3Scanner(ScannerBase):
    
    def __init__(self, *args):
        super(BaseShared3Scanner, self).__init__(*args)
        self._tokenizer += [
            'scan_disclaimer',
            'skip_empty_line',
            'skip_comment',
            'scan_available',
            'scan_keyvalue'
        ]

    def skip_comment(self):
        return self._input.skip("^;.*\n")

    def scan_available(self):
        if self._input.skip("^not found.+\n"):
            self._ast["status:available"] = True
            return True

    def scan_disclaimer(self):
        if self._input.pos == 0 and self._input.match("^;.*"):
            self._ast["field:disclaimer"] = " ".join(self._scan_lines_to_array("^;(.*)\n"))
            self._ast["field:disclaimer"].replace("  ", "\n")
            return True

