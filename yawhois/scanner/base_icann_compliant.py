from .base import ScannerBase

class BaseIcannCompliantScanner(ScannerBase):
    
    def __init__(self, *args):
        super(BaseIcannCompliantScanner, self).__init__(*args)
        self._tokenizer += [
            'skip_head',
            'scan_available',
            'scan_throttled',
            'skip_empty_line',
            'skip_blank_line',
            'scan_keyvalue',
            'skip_end'
        ]

    def scan_available(self):
        if self._settings.get('pattern_available') and self._input.skip_until(self._settings.get('pattern_available')):
            self._ast['status:available'] = True
            return True

    def scan_throttled(self):
        if self._settings.get('pattern_throttled') and self._input.skip_until(self._settings.get('pattern_throttled')):
            self._ast['status:throttled'] = True
            return True

    def skip_head(self):
        if self._input.skip_until("Domain Name:"):
            self._input.scan("\s?(.+)\n")
            self._ast["Domain Name"] = self._input.results[1].strip()
            return True

    def skip_end(self):
        self._input.terminate()
        return True