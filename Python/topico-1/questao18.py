''' programa que leia tres numeros nas variaveis A,B e C, faça a troca dos valores para A->C, B->A,C=->B
    e imprima as variaveis A,B e C respectivamente.
'''
a,b,c = int(input()),int(input()),int(input())

aux = a
a= c
c=b
b=aux

##a,b,c=c,a,b
## forma mais simplificada
print(a,b,c)