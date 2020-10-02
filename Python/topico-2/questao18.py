#python 2.7.15
#coding: utf-8

#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = raw_input('Informe uma letra: ')
 
if ('AEIOU'.find(letra.upper()) >= 0):
    print 'VOGAL'
else:
    print 'CONSOANTE'
 