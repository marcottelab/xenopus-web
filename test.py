#!/usr/bin/python
import cgi
import string

form = cgi.FieldStorage()

print "Content-type: text/html\n"
print open('tmpl/header.html','r').read()

term = form.getfirst('gene_name','').upper()
print term

print open('tmpl/footer.html','r').read()


