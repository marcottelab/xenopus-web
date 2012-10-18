#!/usr/bin/python
import os
import cgi
import json

form = cgi.FieldStorage()

print "Content-type: text/html\n"

dataset = 'Oktoberfest'
term = form.getfirst('term','').upper()

rv = dict()
f = open(os.path.join('/home','taejoon',dataset,'XENLA_2012oct_names.single'),'r')
for line in f:
    tokens = line.strip().split("\t")
    if( tokens[0].find(term) >= 0 ):
        rv[tokens[0]] = tokens[0]
f.close()

print json.dumps(rv, sort_keys=True)
