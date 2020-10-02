# -*- coding: utf-8 -*-
"""
Nas profundezas de uma mina abandonada mora Zya’mta, o bruxo. Ele está
preparando uma poção para um ritual, mas precisa acertar a quantidade de ingredientes
primordiais: rasgo de saia de assombração, cabelo de desiludido e dente de lesma. A
proporção de quantidades é de duas pares para dois múltiplos de três. Como a matemática
na era das trevas estava devagar, ele invoca o poder da programação.Faça um programa que, dado a entrada dos inteiros Q1, Q2 e Q3, as quantidades de
cada ingrediente e, se há exatamente dois números pares e dois múltiplos de três, se a
poção dará certo.
Faça um programa que, dado a entrada dos inteiros Q1, Q2 e Q3, as quantidades de
cada ingrediente e, se há exatamente dois números pares e dois múltiplos de três, se a
poção dará certo.
Exemplo de entrada:
4 6 9
8 14 3
Saída de acordo com exemplo:
Sim. Pronto para o ritual
Não. O caldeirão explodiu
"""

print("ENTRE COM OS VALORES 1,2 E 3: ")
q1, q2, q3 = int(input()), int(input()), int(input())

if((q1%2 == 0 and q2%2 == 0) or (q1%2 == 0 and q3%2 == 0) or (q2%2 == 0 and q3%2 == 0) and (q1%3 == 0 and q2%3 == 0) or (q1%3 == 0 and q3%3 == 0) or (q2%3 == 0 and q3%3 == 0)) :
    print("Sim, pronto para o ritual")
else:
    print("NAAAO O CALDEIRAO EXPLODIU")

