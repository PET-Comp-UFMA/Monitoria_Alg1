#python 2.7.15
#coding: utf-8
"""
Faça um Programa que leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2- Segunda, etc.),
se digitar outro valor deve aparecer valor inválido.
"""
numero_dia = int(input('Informe um numero para saber o dia da semana: '))
 
if (numero_dia == 1):
    print 'Domingo'
elif (numero_dia == 2):
    print 'Segunda'
elif (numero_dia == 3):
    print 'Terca'
elif (numero_dia == 4):
    print 'Quarta'
elif (numero_dia == 5):
    print 'Quinta'
elif (numero_dia == 6):
    print 'Sexta'
elif (numero_dia == 7):
    print 'Sabado'
else:
    print 'Valor invalido'
