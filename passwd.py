#!/usr/bin/python
# -*- coding: utf-8 -*-

fich=open('/etc/passwd', 'r')
lista=fich.readlines()
dic_shells={}
usuario_buscar = 'pepito'

for line in lista:
    linea=line.split(':')
    user=linea[0]
    shell=linea[-1]
    dic_shells[user] = shell

try:
    print  'Usuario root: ' + dic_shells['root']
    print dic_shells[usuario_buscar]
except KeyError:
	print usuario_buscar + ': ' + ('Usuario incorrecto')
