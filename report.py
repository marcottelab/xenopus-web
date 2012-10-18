#!/usr/bin/python
import cgi
import string
import os
import sys

dataset = 'Oktoberfest'

print "Content-type: text/html\n"
print open('tmpl/header.html','r').read()
mesg = ''

form = cgi.FieldStorage()
t_id = form.getfirst('t_id','')

if( t_id == '' ):
    mesg = 'No target_region is provided. Try again.'
    print string.Template(open('tmpl/init_mesg.html','r').read()).substitute(mesg=mesg)
    print open('tmpl/footer.html','r').read()
    sys.exit(1)

target_list = dict()
f = open(os.path.join('/home','taejoon',dataset,'XENLA_2012oct_names.raw'),'r')
for line in f:
    tokens = line.strip().split("\t")
    if( tokens[1] == t_id ):
        gene_name = tokens[0]
        rep_id = tokens[2]
        if( not target_list.has_key(gene_name) ):
            target_list[gene_name] = []
        target_list[gene_name].append(rep_id)
f.close()
print string.Template(open('tmpl/report_info.html','r').read()).substitute(t_id=t_id, gene_list=','.join(target_list.keys()))

filename_cdna = os.path.join('/home','taejoon',dataset,'longest_fa','%s.cdna.fa'%t_id)
if( not os.access(filename_cdna,os.R_OK) ):
    mesg = '%s is not available'%filename_cdna
cdna_txt = open(filename_cdna,'r').read()
if( len(cdna_txt) == 0 ):
    mesg = '%s is not available'%filename_cdna

filename_prot = os.path.join('/home','taejoon',dataset,'longest_fa','%s.prot.fa'%t_id)
if( not os.access(filename_prot,os.R_OK) ):
    mesg = '%s is not available'%filename_prot
prot_txt = open(filename_prot,'r').read()
if( len(prot_txt) == 0 ):
    mesg = '%s is not available'%filename_prot

print string.Template(open('tmpl/seq.html','r').read()).substitute(prot_seq=prot_txt,cdna_seq=cdna_txt,t_id=t_id)

filename_tree = os.path.join('/home','taejoon',dataset,'nw_tree','%s.tree'%t_id)
if( not os.access(filename_tree,os.R_OK) ):
    mesg = '%s is not available'%filename_tree
tree_txt = open(filename_tree,'r').read()
if( len(tree_txt) == 0 ):
    mesg = '%s is not available'%filename_tree
print string.Template(open('tmpl/tree.html','r').read()).substitute(tree_txt=tree_txt)

filename_png = os.path.join('/home','taejoon',dataset,'png.2012oct','%s.png'%t_id)
if( not os.access(filename_png,os.R_OK) ):
    mesg = '%s is not available'%filename_png
    print string.Template(open('tmpl/init_mesg.html','r').read()).substitute(mesg=mesg)
    print open('tmpl/footer.html','r').read()
    sys.exit(1)
print string.Template(open('tmpl/map_fig.html','r').read()).substitute(t_id=t_id)

if( mesg != '' ):
    print string.Template(open('tmpl/init_mesg.html','r').read()).substitute(mesg=mesg)
print open('tmpl/footer.html','r').read()
