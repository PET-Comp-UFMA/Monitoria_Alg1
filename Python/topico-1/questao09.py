'''
     Construa um algoritmo que, tendo como dados de entrada dois pontos quaisquer no plano, P(x1,y1) e P(x2,y2), escreva a distância entre eles.
    A fórmula que efetua tal cálculo é: d = sqrt((x2-x1)² + (y2 - y1)²)
'''
from math import sqrt

print("Entre com os valores x1,x2,y1 e y2 respectivamente")
x1,x2,y1,y2 = int(input()),int(input()),int(input()),int(input())

d = sqrt(((x2-x1)*(x2-x1)) + ((y2 - y1)*(y2 - y1)))
print(d)