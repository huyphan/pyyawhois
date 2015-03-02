from .base import ScannerBase
from ..exceptions import ParserError

class WhoisCiraCaScanner(ScannerBase):

    def __init__(self, *args):
        super(WhoisCiraCaScanner, self).__init__(*args)
        self._tokenizer += [
            'skip_empty_line',
            'scan_disclaimer',
            'skip_comment',
            'scan_header',
            'scan_keyvalue',
            'scan_nameserver'
        ]

    def scan_disclaimer(self):
        if self._input.match("^% Use of CIRA"):
            self._ast["field:disclaimer"] = "\n".join(self._scan_lines_to_array("^%(.*)\n"))
            return True

    def scan_header(self):
        if self._input.scan("^(.+?):\n"):
            self._tmp["group"] = self._input.results[1]
            return True

    def scan_keyvalue(self):
        if self._input.scan("^(.+?):(.*?)\n"):
            start = self._input.results[1]
            key, value = start.strip(), self._input.results[2].strip()

            # This is a nested key
            if start[0] == " ":
                if self._tmp.get("group") is None:
                    raise ParserError("Expected group.")
                self._ast[self._tmp["group"]] = self._ast.get(self._tmp["group"]) or {}
                target = self._ast[self._tmp["group"]]
            else:
                if self._tmp.get("group") is not None:
                    del self._tmp["group"]
                target = self._ast

            more  = self._scan_lines_to_array("^\s{#{start.size}}(.+)\n")
            if len(more) != 0:
                more.insert(0, value)
                value = "\n".join(more)

            if target.get(key) is None:
                target[key] = value
            else:
                target[key] = array_wrapper(target[key])
                target[key].append(value)

            return True

    def scan_nameserver(self):
        if self._input.scan("^\s+(.+?)\n") and self._tmp["group"] == "Name servers":
            self._ast["field:nameservers"] = self._ast["field:nameservers"] or []
            self._ast["field:nameservers"].append(self._input.results[1].strip())
            return True

    def skip_comment(self):
          return self._input.skip("^%.*\n")
