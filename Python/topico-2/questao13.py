# -*- coding: utf-8 -*-
""" Faça um algoritmo que leia uma variável e some 5 caso seja par
   ou some 8 caso seja ímpar, imprimir o resultado desta operação.  
"""
num = int(input())
operacao = 0
if num%2 == 0:
    operacao = num + 5
else:
    operacao = num + 8

print("Resultado da operação: " + str(operacao))        