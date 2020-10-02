# -*- coding: utf-8 -*-
"""
  Escreva	 um	 programa	 para	 ler	 3	 valores	 inteiros	 (considere	 que não
  serão	lidos	valores	iguais)	e	escrevê-los	em	ordem	crescente.
"""

print("Insira três numeroa de qualquer valor")
n1,n2,n3 = int(input()), int(input()), int(input())

if(n1 > n2) :
  n1,n2 = n2,n1

if (n2 > n3) :
  n2,n3 = n3,n2

if (n1 > n2) :
  n1,n2 = n2,n1


print("deu certo?")
print(n1,n2,n3)

