#!/usr/bin/python
import cgi
import string
import os

dataset = 'Oktoberfest'

print "Content-type: text/html\n"
print open('tmpl/header.html','r').read()
#print string.Template( open('tmpl/header.html','r').readlines() ).substitute()
print open('tmpl/init.html','r').read()

mesg = ''

form = cgi.FieldStorage()
gene_name = form.getfirst('gene_name','').upper()

target_list = dict()
if( gene_name != '' ):
    f = open(os.path.join('/home','taejoon',dataset,'XENLA_2012oct_names.raw'),'r')
    for line in f:
        tokens = line.strip().split("\t")
        if( tokens[0] == gene_name ):
            t_id = tokens[1]
            rep_id = tokens[2]
            if( not target_list.has_key(t_id) ):
                target_list[t_id] = []
            target_list[t_id].append(rep_id)
    f.close()

targets = sorted(target_list.keys())
#print "Gene name:",gene_name
#print "TARGETS:",targets

if( gene_name == '' ):
    mesg = 'No gene name is provided. Try again.'
elif( len(targets) == 0 ):
    mesg = 'No target region for %s. Try again.'%gene_name
else:
    mesg = 'List of genome hits for %s.'%gene_name

if( mesg != '' ):
    print string.Template(open('tmpl/init_mesg.html','r').read()).substitute(mesg=mesg)

tmpl_list = string.Template(open('tmpl/list.html','r').read())
if( len(targets) > 0 ):
    print "<ul>"
    for t_id in targets:
        print tmpl_list.substitute(t_id=t_id,rep_list=','.join(sorted([x.replace(t_id,'') for x in target_list[t_id]])))
    print "</ul>"
print open('tmpl/footer.html','r').read()
