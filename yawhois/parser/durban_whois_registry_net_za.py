from .za_central_registry import ZaCentralRegistryParser

class DurbanWhoisRegistryNetZaParser(ZaCentralRegistryParser):

    def __init__(self, *args):
        super(DurbanWhoisRegistryNetZaParser, self).__init__(*args)
