from ..exceptions import ParserError
import re

class StringScanner(object):

    def __init__(self, string):
        self._input   = string
        self._offset  = 0
        self.results   = []

    @property
    def buffer(self):
        return buffer(self._input, self._offset)

    def eos(self):
        return self._offset >= len(self._input)

    def _search(self, pattern, flags = re.MULTILINE):
        pattern = re.compile(pattern, flags)
        match   = pattern.search(self.buffer)
        return match

    def _search_from_start(self, pattern, flags = re.MULTILINE):
        return self._search("\A" + pattern, flags)

    def match(self, pattern, flags = re.MULTILINE):
        match = self._search_from_start(pattern, flags)
        if match is not None:
            return len(match.group())
      
    def skip(self, pattern, flags = re.MULTILINE):
        match = self._search_from_start(pattern, flags)
        if match is not None:
            old_offset    = self._offset
            self._offset += match.end()
            return self._offset - old_offset

    def scan(self, pattern, flags = re.MULTILINE):
        match = self._search_from_start(pattern, flags)

        if match is not None:
            self._offset += match.end()
            self.results  = (match.group(),) + match.groups()
            
            return True

        self.results = []
        return False

    def skip_until(self, pattern, flags = re.MULTILINE):
        match = self._search(pattern, flags)
        if match is not None:
            self._offset += match.end()
            return match.end()

        return None

    def check_until(self, pattern, flags = re.MULTILINE):
        match = self._search(pattern, flags)

        if match is not None:
            self.results = [self._input[self._offset:self._offset + match.end()]]
            return True
        
        self.results = []
        return False

    def scan_until(self, pattern, flags = re.MULTILINE):
        if self.check_until(pattern, flags):
            self._offset += len(self.results[0])
            return self.results

        return None

    def remaining(self):
        return self._input[self._offset:]

    def terminate(self):
        self._offset = len(self._input)
        self.results  = []

    @property
    def pos(self):
        return self._offset

class ScannerBase(object):

    def __init__(self, settings = None):
        self._settings  = settings or {}
        self._tokenizer = []

    def parse(self, content):
        self._tmp = {}
        self._ast = {}
        
        self._input  = StringScanner(content)
        self._offset = 0

        while not self._input.eos():
            self.tokenize()

        return self._ast

    def skip_empty_line(self):
        return self._input.skip("^\n")

    def skip_blank_line(self):
        return self._input.skip("^[\s]*\n")

    def skip_new_line(self):
        return self._input.skip("\n")

    def scan_keyvalue(self):
        if self._input.scan("(.+?):(.*?)(\n|\Z)"):
            key, value = self._input.results[1].strip(), self._input.results[2].strip()
            if self._tmp.get("_section"):
                target = self._ast[self._tmp.get("_section")] or {}
            else:
                target = self._ast

            if value:
                if not target.has_key(key):
                    target[key] = value
                elif isinstance(target[key], list):
                    target[key].append(value)
                else:
                    target[key] = [target[key], value]

            return True

    def _scan_lines_to_array(self, pattern):
        results = []
        while self._input.scan(pattern):
            results.append(self._input.results[1].strip())
        return results

    def _scan_lines_to_hash(self, pattern):
        results = []
        while self._input.scan(pattern):
            key, value = self._input.results[1], self._input.results[2]
            results[key.strip()] = value.strip()
        return results

    def _scan_keyvalues(self, pattern):
        results = []
        if self._input.scan("(.+?):(.*?)(\n|\z)"):
            key, value = self._input.results[1], self._input.results[2]
            if not results.has_key(key):
                results[key] = value
            elif isinstance(results[key], list):
                results[key].results(value)
            else:
                results[key] = [results[key], value]
        return results
        
    def tokenize(self):
        for tokenizer in self._tokenizer:
            if hasattr(self, tokenizer):
                r = getattr(self, tokenizer)()
                if r:
                    return
        
        self.error("Unexpected token")

    def error(self, message):
        raise ParserError("%s: %s" % (message, self._input.remaining()))
