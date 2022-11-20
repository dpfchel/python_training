# -*- coding: utf-8 -*-
from model.group import Group
from fixture.application import Application as appl
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of block x8", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 2
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

testdata = []
for i in range(n):
    testdata = testdata + [
        Group(name=name, header=header, footer=footer)
                for name in ["", (appl.random_string("name", 10)).strip()]
                for header in ["", appl.random_string("header", 20)]
                for footer in ["", appl.random_string("footer", 20)]
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, 'w') as ff:
    jsonpickle.set_encoder_options("json", indent=2)
    ff.write(jsonpickle.encode(testdata))
    #

