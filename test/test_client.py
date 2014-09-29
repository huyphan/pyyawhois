from nose.tools import *
from yawhois.client import Client
import yawhois

#TODO: More test cases for Client

def test_initialize_no_param():
    client = Client()

def test_initialize_accept_settings_param():
    client = Client({'foo' : 'bar'})

def test_timeout_setting():
    client = Client({'timeout' : 100})
    eq_(client.timeout, 100)

def test_timeout_setting_nil():
    client = Client({'timeout' : None})
    eq_(client.timeout, None)

def test_timeout_setting_default():
    client = Client()
    eq_(client.timeout, yawhois.client.DEFAULT_TIMEOUT)

def test_timeout_setting_default():
    client = Client()
    eq_(client.timeout, yawhois.client.DEFAULT_TIMEOUT)

def test_timeout_setting_exclude_timeout():
    client = Client({'timeout': None, 'foo': 'bar'})
    eq_(client.settings, {'foo': 'bar'})

def test_lookup_convert_arg_to_string():
    server = yawhois.adapters.BaseAdapter('tld', '.test', 'whois.test')
    server.lookup("example.test")    
