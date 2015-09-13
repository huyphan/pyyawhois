from .za_central_registry import ZaCentralRegistryParser

class JoburgWhoisRegistryNetZaParser(ZaCentralRegistryParser):

    def __init__(self, *args):
        super(JoburgWhoisRegistryNetZaParser, self).__init__(*args)
