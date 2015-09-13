from .za_central_registry import ZaCentralRegistryParser

class CapetownWhoisRegistryNetZaParser(ZaCentralRegistryParser):

    def __init__(self, *args):
        super(CapetownWhoisRegistryNetZaParser, self).__init__(*args)
