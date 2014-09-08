from ..exceptions import ParserError

class StringScanner(object):

    def __init__(self, string):
        self.__input   = string
        self.__offset  = 0
        self.results   = []

    def eos(self):
        return self.__offset == len(self.__input)

    def skip(self, pattern, flags = 0):
        if isinstance(pattern, basestring):
            pattern = re.compile(pattern, flags)

        match = pattern.match(self.__input, self.__offset)

        if match is not None:
            self.offset = match.end()

    def scan(self, pattern, flags = 0):
        if isinstance(pattern, basestring):
            pattern = re.compile(pattern, flags)

        match = pattern.match(self.__input, self.__offset)

        if match is not None:
            self.offset  = match.end()
            self.results = (match.group(),) + match.groups()
            
            return True

        return False

    def remaining(self):
        return self.__input[self.__offset:]

class ScannerBase(object):

    __tokenizer = []

    def __init__(self, settings = None):
        self.settings = settings or {}

    def parse(content):
        self.__tmp = {}
        self.__ast = {}
        
        self.__input  = StringScanner(content)
        self.__offset = 0

        while not self.__input.eos():
            self.tokenize()

    def skip_empty_line(self):
        self.__input.skip("^\n")

    def skip_blank_line(self):
        self.__input.skip("^[\s]*\n")

    def skip_new_line(self):
        self.__input.skip("\n")

    def scan_keyvalue(self):
        if self.__input.scan("(.+?):(.*?)(\n|\z)"):
            key, value = self.__input.results[1], self.__input.results[2]

            if self.__tmp.get("_section"):
                target = self.__ast[self.__tmp.get("_section")] or {}
            else:
                target = self.__ast
                
            if not target.has_key(key):
                target[key] = value
            elif isinstance(target[key], list):
                target[key].append(value)
            else:
                target[key] = [target[key], value]

    def __scan_lines_to_array(self, pattern):
        results = []
        while self.__input.scan(pattern):
            results.append(self.__input.results[1].strip())
        return results

    def __scan_lines_to_hash(self, pattern):
        results = []
        while self.__input.scan(pattern):
            key, value = self.__input.results[1], self.__input.results[2]
            results[key.strip()] = value.strip()
        return results

    def _scan_keyvalues(self, pattern):
        results = []
        if self.__input.scan("(.+?):(.*?)(\n|\z)"):
            key, value = self.__input.results[1], self.__input.results[2]
                
            if not results.has_key(key):
                results[key] = value
            elif isinstance(results[key], list):
                results[key].results(value)
            else:
                results[key] = [results[key], value]
        return results
        
    def tokenize():
        for tokenizer in self.__tokenizer:
            if getattr(self, tokenize):
                return
        self.error("Unexpected token")

    def error(self, message):
        raise ParserError("%s: %s" % (message, self.__input.remaining()))