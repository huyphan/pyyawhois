import re

def is_valid_ipv4(addr):
    match = re.compile("\A(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})\Z").match(addr)
    if match:
        return sum(map(lambda x: int(x) < 256, groups)) == 4
    return False

def is_valid_ipv6(addr):
    # IPv6 (normal)
    if re.compile("\A[\dA-Fa-f]{1,4}(:[\dA-Fa-f]{1,4})*\Z").match(addr):
        return True

    if re.compile("\A[\dA-Fa-f]{1,4}(:[\dA-Fa-f]{1,4})*::([\dA-Fa-f]{1,4}(:[\dA-Fa-f]{1,4})*)?\Z").match(addr):
        return True

    if re.compile("\A::([\dA-Fa-f]{1,4}(:[\dA-Fa-f]{1,4})*)?\Z").match(addr):
        return True
    
    # IPv6 (IPv4 compat)
    match = re.compile("\A[\dA-Fa-f]{1,4}(?:[\dA-Fa-f]{1,4})*:(.*)\Z").match(addr)
    if match and is_valid_ipv4(match.group(1)):
        return True

    match = re.compile("\A[\dA-Fa-f]{1,4}(?:[\dA-Fa-f]{1,4})*::(?:[\dA-Fa-f]{1,4}(?:[\dA-Fa-f]{1,4})*:)?(.*)\Z").match(addr)
    if match and is_valid_ipv4(match.group(1)):
        return True

    match = re.compile("\A::(?:[\dA-Fa-f]{1,4}(?:[\dA-Fa-f]{1,4})*:)?(.*)\Z").match(addr)
    if match and is_valid_ipv4(match.group(1)):
        return True

    return False

def camelize(string):
    "".join([s.capitalize() for s in string.split("_")])

def matches_tld(string):
    return re.compile("^\.(xn--)?[a-z0-9]+$").match(string)

def matches_ip(string):
    return is_valid_ipv4(string) or is_valid_ipv6(string)

def matches_email(string):
    return "@" in string

def matches_asn(string):
    return re.compile("^as\d+$", re.I).match(string)