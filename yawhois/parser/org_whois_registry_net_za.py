from .za_central_registry import ZaCentralRegistryParser

class OrgWhoisRegistryNetZaParser(ZaCentralRegistryParser):

    def __init__(self, *args):
        super(OrgWhoisRegistryNetZaParser, self).__init__(*args)
