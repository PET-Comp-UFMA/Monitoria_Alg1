# -*- coding: utf-8 -*-
"""
Reunindo quatro gravetos, um hominídeo fará um dos maiores avanços da história
humana: inventará um retângulo. Mas ele não sabe se os gravetos têm o tamanho certo
para isso, então ele vai pedir sua ajuda, o programador pré-histórico.
Faça um programa que peça quatro inteiros ao usuário, que são os comprimentos
em centímetros dos gravetos, e diga se com eles se pode formar um retângulo.
Exemplo de entrada:
4 4 8 8
3 5 6 5
Saída de acordo com exemplo:
Forma retângulo. Homo sapiens sapiens
Não forma retângulo. Mais oito mil anos de evolução
"""

aresta1, aresta2, aresta3, aresta4 = int(input()), int(input()), int(input()), int(input()) 

if(aresta1 == aresta2 and aresta3 == aresta4) or (aresta1 == aresta3 and aresta2 == aresta4) or(aresta1 == aresta4 and aresta3 == aresta2) or (aresta3 == aresta2 and aresta4 == aresta1) :
    print("Forma retângulo. Homo sapiens sapiens")
else: 
    print("Não forma retângulo. Mais oito mil anos de evolução")
