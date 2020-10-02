# -*- coding: utf-8 -*-
""" O bondinho que leva número N de alunos e 4 monitores, mas bonde só comporta 50
pessoas. Dizer se vai caber
	Hernán Cortez assassinou o imperador asteca, Montezuma, e agora tem que fugir
da cidade flutuante Tenochtitlán com seus homens. Os astecas destruíram as pontes,
porém Hernã viu que em um pequeno porto há balsas que poderiam carregar os soldados
até a margem do lago. Sem pensar duas vezes, deixa muito equipamento para trás e
manda todos subirem nas balsas.
	Há 5 balsas. Cada uma aguenta 50 soldados. Cada balsa irá carregar 4 cavalos,
cada um pesando por dois soldados. Faça um programa que, dados naturais S1, S2, S3, S4
e S5, representando a quantidade de soldados em cada balsa, exiba quais balsas foram
capazes de chegar sem afundar, por meio de mensagens de True ou False.
EXEMPLO:
		entrada: 
50 30 45 20 44
		saída:
False True False True False """
#dicas: utilizar flag (variável contendo valor booleano True ou False)

s1,s2,s3,s4,s5 = int(input()),int(input()),int(input()),int(input()),int(input())
cavalo = 4*2 #há 4 cavalos em cada balsa, cada cavalo vale por 2 soldados
if s1<=(50-cavalo) :
	print(True)
else: print(False) 

if s2<=(50-cavalo) :
	print(True)
else: 
    print(False) 

if s3<=(50-cavalo) :
	print(True)
else: 
    print(False) 

if s4<=(50-cavalo) :
	print(True)
else: 
    print(False) 

if s5<=(50-cavalo) :
	print(True)
else: 
    print(False) 
