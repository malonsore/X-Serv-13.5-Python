#!/usr/bin/python
# -*- coding: utf-8 -*-

fich=open('/etc/passwd', 'r')
list_lines=fich.readlines()
dic_shells={}
usuario_buscar = 'pepito'

for line in list_lines:
    list_split=line.split(':')
    user_=list_split[0]
    shell=list_split[-1]
    dic_shells[user] = shell

try:
    print  'Usuario root: ' + dic_shells['root']
    print dic_shells[usuario_buscar]
except KeyError:
	print usuario_buscar + ': ' + ('Usuario incorrecto')
