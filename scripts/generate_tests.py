import sys
import os
import glob
import re
import fnmatch
from dateutil.parser import parse as time_parse
from nose.tools import ok_, eq_

def camelize(string):
    string = re.sub("[^\w\d_]", "_", string)
    return "".join([s.capitalize() for s in string.split("_")])

def create_dynamic_method(host, source_path):
    """just don't include `test` in the function name here, nose will try to
    run it"""
    def dynamic_test_method(self):
        """this function name doesn't matter much, it can start with `test`,
        but we're going to rename it dynamically below"""

        fixture_path = source_path.replace(".expected", ".txt")
        
        part   = yawhois.record.Part(open(fixture_path, "r").read(), host)
        record = yawhois.record.Record(None, [part])

        lines = open(source_path, "r").readlines()
        prop  = None
        value = None
        tests = {}

        for line in lines:
            line = line.rstrip()
            match = re.compile("^#([\w\d_]+)").match(line)
            if match:
                prop  = match.group(1)
                value = getattr(record, prop)
                continue

            match = re.compile("\s+(.+?) (.+)").match(line)
            if match:
                method, condition = match.group(1), match.group(2).strip()
                match = re.compile("^%CLASS\{(.+)\}$").match(condition)
                if match:
                    type_to_test = build_condition_typeof(match.group(1))
                    expression = "record.%s should be an instance of %s" % (prop, type_to_test)
                    ok_(isinstance(value, type_to_test) == True, expression)

                match = re.compile("^== (.+)$").match(condition)
                if match:
                    expression = "record.%s == %s" % (prop, match.group(1))
                    ok_(value == translate_expected_value(match.group(1)), expression)

                    #tests[prop].append(parse_assertion(k, v))

    return dynamic_test_method

def generate_tests(source_path):
    lines = open(source_path, "r").readlines()
    prop  = None
    value = None
    tests = {}

    code  = ""

    for line in lines:
        line = line.rstrip()

        match = re.compile("(^\s*$)|(^\s*\/\/.*$)").match(line)
        if match:
            continue

        match = re.compile("^#([\w\d_]+)").match(line)
        if match:
            prop  = match.group(1)
            tests[prop] = []

        match = re.compile("\s+(.+?) (.+)").match(line)
        if match:
            left_side, condition = match.group(1), match.group(2).strip()
            left_side = left_side % ("self.record." + prop)
            match = re.compile("^%CLASS\{(.+)\}$").match(condition)
            if match:
                type_to_test = build_condition_typeof(match.group(1))
                test_line    = "eq_(%s.__class__.__name__, '%s')" % (left_side, type_to_test)
                tests[prop].append(test_line)
                continue

            match = re.compile("^%ERROR\{(.+)\}$").match(condition)
            if match:
                test_line = "assert_raises(yawhois.exceptions.%s, %s)" % (match.group(1), left_side)
                tests[prop].append(test_line)
                continue

            match = re.compile("^== (.+)$").match(condition)
            if match:
                test_line = "eq_(%s, %s)" % (left_side, translate_expected_value(match.group(1)))
                tests[prop].append(test_line)
                continue

            match = re.compile("^%TIME\{(.+)\}$").match(condition)
            if match:
                test_line = "eq_(%s, time_parse('%s'))" % (left_side, match.group(1))
                tests[prop].append(test_line)
                continue

            match = re.compile("^%SIZE\{(.+)\}$").match(condition)
            if match:
                test_line = "eq_(len(%s), %s)" % (left_side, match.group(1))
                tests[prop].append(test_line)
                continue

            raise Exception("Invalid line '%s' in '%s'" % (line, source_path))

    for prop, conditions in tests.items():
        code += TPL_TESTCASE.format(**{'test_case': prop, 'test_case_code': ("\n" + " "*8).join(conditions)})

    return code

def translate_expected_value(value):
    if value == 'true':
        return 'True'

    if value == 'false':
        return 'False'

    if value == 'nil':
        return 'None'

    if value == 'Whois::Record::Contact::TYPE_ADMINISTRATIVE':
        return 'yawhois.record.Contact.TYPE_ADMINISTRATIVE'

    if value == 'Whois::Record::Contact::TYPE_REGISTRANT':
        return 'yawhois.record.Contact.TYPE_REGISTRANT'

    if value == 'Whois::Record::Contact::TYPE_TECHNICAL':
        return 'yawhois.record.Contact.TYPE_TECHNICAL'

    if value == '""':
        return 'None'

    if value.startswith(':'):
        return "'%s'" % value.strip(":")

    return value

def build_condition_typeof(described_class):
    if described_class == "array":
        return 'list'
    elif described_class == "time":
        return 'datetime'
    elif described_class == "contact":
        return 'Contact'
    elif described_class == "nameserver":
        return 'Nameserver'
    elif described_class == "registrar":
        return 'Registrar'
    else:
        raise Exception("Unknown class '%s'" % described_class)

# def build_condition_typecast(described_class, value):
#     if described_class == "time"
#         parse(value)
#     else:
#         raise Exception("Unknown class '%s'" % described_class)

# def parse_assertion(method, condition):
#     m = method
#     c = condition.strip()

#     match = re.compile("^%CLASS\{(.+)\}$").match(c)
#     if match:
#         c = "be_a(%s)" % build_condition_typeof(match.group(1))


#     match = re.compile("^%CLASS\{(.+)\}$").match(c)
#     if match:
#         c = "be_a(%s)" % build_condition_typeof(match.group(1))
#         return [m, c]

#     match = re.compile("^%SIZE\{(.+)\}$").match(c)
#     if match:
#         c = "have(%s).items" % match.group(1)
#         return [m, c]


# for k, pair in enumerate(xrange(12)):
#     dynamic_method = create_dynamic_method(pair)
#     dynamic_method.__name__ = 'test_{0}'.format(k)
#     dynamic_method.__doc__ = 'my super great name {0}'.format(k)
#     setattr(TestMyGoods, dynamic_method.__name__, dynamic_method)
#     # remove the last test name from the current namespace, 
#     # so nose doesn't run it
#     del dynamic_method

project_root_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
source_dir       = os.path.join(project_root_dir, "spec", "fixtures", "responses")
target_dir       = os.path.join(project_root_dir, "test", "record", "parser")

TPL_FILE = """
# This file is autogenerated. Do not edit it manually.
# If you want change the content of this file, edit
#
#   {sfile}
#
# and regenerate the tests with the following script
#
#   $ scripts/generate_tests.py
#

from nose.tools import *
from dateutil.parser import parse as time_parse
import yawhois

class Test{test_class}(object):

    def setUp(self):
        {tear_up_code}
{test_cases}"""

TPL_TESTCASE = """
    def test_{test_case}(self):
        {test_case_code}
"""

matches = []
for root, dirnames, filenames in os.walk(source_dir):
    for filename in fnmatch.filter(filenames, '*.expected'):
        source_path = os.path.join(root, filename)
        parts       = os.path.relpath(source_path, source_dir).replace(".expected", "")
        target_file = "test_response_%s.py" % re.sub("[^\w\d_]", "_", parts)
        target_path = os.path.join(target_dir, target_file)

        source_file = os.path.join("spec", "fixtures", "responses", parts)

        khost        = parts.split("/")[0]
        fixture_path = source_file + ".txt"

        tear_up_code = """fixture_path = "%s"
        host         = "%s"
        part         = yawhois.record.Part(open(fixture_path, "r").read(), host)
        self.record  = yawhois.record.Record(None, [part])""" % (fixture_path, khost)

        code = TPL_FILE.format(**{
                                    "sfile"       : source_file, 
                                    "test_class"  : camelize(parts.replace(".expected", "")),
                                    "tear_up_code": tear_up_code, 
                                    "test_cases"  : generate_tests(source_path)
                                })

        f = open(target_path, "w")
        f.write(code)
        f.close()

      # matches.append(os.path.join(root, filename))

# for source_path in glob.glob("%s/**/*.expected" % source_dir)[:5]:
#     parts = os.path.relpath(source_path, source_dir)
#     khost, kfile = parts.split("/")

#     described_class  = yawhois.parser.factory.ParserFactory.parser_class(khost)
#     target_file_name = "test_response_%s_%s.py" % (khost, kfile.replace(".expected", ""))
#     target_file_path = os.path.join(target_dir, target_file_name)
