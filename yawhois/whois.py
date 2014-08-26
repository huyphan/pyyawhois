
from .client import Client
import logging

def lookup(domain):
    return Client().lookup(domain)

def is_available(domain):
    result = lookup(domain).is_available
    if result is None:
        logging.warning("Availability check is not supported for %s domain. Use Whois.lookup('%s') instead")
    
    return result

def is_registered(domain):
    result = lookup(domain).is_available
    if result is None:
        logging.warning("Availability check is not supported for %s domain. Use Whois.lookup('%s') instead")
    
    return result