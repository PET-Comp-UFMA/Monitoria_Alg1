# -*- coding: utf-8 -*-
"""
Clark e Nickelson são dois paraquedistas americanos que pousaram separados de
seu esquadrão, mais para dentro da linha inimiga. Estão escondidos dentro de uma casa
em ruínas e podem ouvir um SdKfz, carro armado alemão, patrulhando do lado de fora. Eles
precisam detonar a ameaça se quiserem se mexer, mas um deles precisa se arriscar em
levar explosivos até próximo do veículo. Para serem justos, vão decidir no cara ou coroa.
Faça um programa que, dado a entrada “cara” ou “coroa”, diga qual dos dois vai ter
que sair do esconderijo. Clark escolheu cara e Nickelson escolheu coroa.
Exemplo de entrada:
cara
coroa
Saída de acordo com exemplo:
Vai lá, Clark
Boa sorte, Nickelson
"""

print("cara ou coroa?")
valor = input()
if (valor == "cara") :
  print("Vai lá Clark")
else:
  print("Boa sorte Nickelson")
