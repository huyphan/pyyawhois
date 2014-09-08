from base import ScannerBase

class Verisign(ScannerBase):

    def __init__(self, *args):
        super(Verisign, self).__init__(*args)
        self.__tokenizer += [
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