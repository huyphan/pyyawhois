from base import ScannerBase

class VerisignScanner(ScannerBase):

    def __init__(self, *args):
        super(VerisignScanner, self).__init__(*args)
        self._tokenizer += [
            'skip_empty_line',
            'scan_response_unavailable',
            'scan_available',
            'scan_disclaimer',
            'scan_notice',
            'scan_keyvalue_indented',
            'skip_ianaservice',
            'skip_lastupdate',
            'skip_fuffa',
        ]

    def scan_response_unavailable(self):
        '''
        Check if the string starts with /*
        If it does, match until the end of all /* lines
        or the end of the file and check for the content.

        Flag the block as visited to force the scanner to ignore this tokenizer
        if already used and the content didn't match the unavailable message.
        '''
        if self._input.match("^\*\n") and not self.is_visited():
            self._input.check_until("^[^\*]|\z")
            result = self._input.results[0]
            if "Sorry, the Whois database is currently down" in result:
                self._input.skip_until("^[^\*]|\z")
                self.__ast["response:unavailable"] = True
            else:
                self.mark_visited()

    def scan_available(self):
        if self._input.scan('No match for "(.+?)"\.\n'):
            self.__ast["Domain Name"] = self._input.results[1].strip()

    def scan_disclaimer(self):
        if self._input.match("^TERMS OF USE:"):
            self.__ast["Disclaimer"] = " ".join(self._scan_lines_to_array("(.+)\n"))

    def scan_notice(self):
        if self._input.match("^NOTICE:"):
            self.__ast["Notice"] = " ".join(self._scan_lines_to_array("(.+)\n"))

    def scan_keyvalue_indented(self):
        if self._input.scan("\s+(.+?):(.*?)\n"):
            key, value = self._input.results[1].strip(), self._input.results[2].strip()
            if self.__ast.get(key) is None:
                self.__ast[key] = value
            else:
                if not isinstance(self.__ast.get(key), list):
                    self.__ast[key] = [self.__ast[key]]
                self.__ast[key].append(value)

    def skip_lastupdate(self):
        self._input.skip(">>>(.+?)<<<\n")

    def skip_fuffa(self):
        self._input.scan("^\S(.+)(?:\n|\z)")

    def skip_ianaservice(self):
        if self._input.match("IANA Whois Service"):
            self.__ast["IANA"] = True
            self._input.terminate()

    def is_visited(self):
        return self.__tmp.get("visited:" + self._input.pos)

    def mark_visited(self):
        self.__tmp["visited:" + self._input.pos] = True