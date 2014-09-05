from .client import Client

def lookup(object):
    return Client().lookup(object)
