''' Suponha todos os inteiros de 1 a 789. Imprima
o primeiro deles, depois o último, depois o
segundo, depois o penúltimo e assim por diante
até imprimir todos os 789 inteiros.

LISTA DOS EXTREMOS
1
789
2
788
3
...
394
396
395


'''

i = 1

while i < 395:
    print(i)
    print(789-i+1)
    i = i + 1

print(i)