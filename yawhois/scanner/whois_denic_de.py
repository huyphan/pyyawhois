from .base import ScannerBase

class WhoisDenicDeScanner(ScannerBase):

    def __init__(self, *args):
        super(WhoisDenicDeScanner, self).__init__(*args)
        self._tokenizer += [
            'skip_empty_line',
            'scan_response_throttled',
            'scan_response_error',
            'scan_disclaimer',
            'scan_pair',
            'scan_contact',
            'skip_db_time'
        ]

    def scan_response_throttled(self):
        if self._input.match("^% Error: 55000000002"):
            self._ast["response:throttled"] = True
            self._input.skip("^.+\n")
            return True

    def scan_response_error(self):
        if self._input.match("^% Error: 55000000010"):
            self._ast["response:error"] = True
            self._input.skip("^.+\n")
            return True

    def scan_disclaimer(self):
        if self._input.match("% Copyright \(c\) *\d{4} by DENIC\n"):
            self._input.scan_until("% Terms and Conditions of Use\n")
            lines = []
            while self._input.match("%") and self._input.scan("%(.*)\n"):
                if self._input.results[1].strip() != "":
                    lines.append(self._input.results[1].strip())
            self._ast["Disclaimer"] = " ".join(lines)
            return True

    def scan_pair(self):
        return self._parse_pair(self._ast)
        
    def scan_contact(self):
        if self._input.scan("\[(.*)\]\n"):
            contact_name = self._input.results[1]
            contact = {}

            while self._parse_pair(contact):
                pass

            self._ast[contact_name] = {
                "id" : None,
                "name" : contact.get('Name'),
                "organization" : contact.get('Organisation'),
                "address" : contact.get('Address'),
                "city" : contact.get('City'),
                "zip" : contact.get('PostalCode'),
                "state" : None,
                "country" : contact.get('Country'),
                "country_code" : contact.get('CountryCode'),
                "phone" : contact.get('Phone'),
                "fax" : contact.get('Fax'),
                "email" : contact.get('Email'),
                "created_on" : None,
                "updated_on" : contact.get('Changed')
            }

            return True


    def skip_db_time(self):
        return self._input.skip("^% DB time is (.+)\n")

    def _parse_pair(self, store):
        if self._input.scan("([^  \[]*):(.*)\n"):
            key, value = self._input.results[1].strip(), self._input.results[2].strip()
            if store.get(key) == None:
                store[key] = value
            else:
                if not isinstance(store.get(key), list):
                    store[key] = [store[key]]
                store[key].append(value)
            return True