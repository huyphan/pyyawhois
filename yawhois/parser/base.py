class ParserBase(object):
    
    PROPERTY_STATE_NOT_IMPLEMENTED = 'not_implemented'
    PROPERTY_STATE_NOT_SUPPORTED   = 'not_supported'
    PROPERTY_STATE_SUPPORTED       = 'supported'

    __properties = {}

    def __init__(self, part):
        self.__part = part
        self.__cached_properties = {}

    @classmethod
    def is_property_supported(self, prop):
        return self.__properties.get(prop) == ParserBase.PROPERTY_STATE_SUPPORTED

    @property
    def contacts(self):
        contacts = []
        for c in ('registrant_contacts', 'admin_contacts', 'technical_contacts'):
            if self.is_property_supported(c):
                contacts.append(getattr(self, c))
        return contacts