class ParserBase(object):
    
    __properties = {}

    def __init__(self, part):
        self.__part = part
        self.__cached_properties = {}

    @classmethod
    def is_property_supported(self, prop):
        return hasattr(self, prop)

    @property
    def content(self):
        return self.__part.body
        
    @property
    def content_for_scanner(self):
        return self.content.replace("\r\n", "\n")

    @property
    def contacts(self):
        contacts = []
        for c in ('registrant_contacts', 'admin_contacts', 'technical_contacts'):
            if self.is_property_supported(c):
                contacts.append(getattr(self, c))
        return contacts

