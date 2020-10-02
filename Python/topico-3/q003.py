# Imprima os múltiplos de 2 de 1 a 20, depois os múltiplos de 3 de 1 a 20, depois os múltiplos de 4 de 1 a 20 e assim por diante até imprimir
# os múlitplos de 10 de 1 a 20
# Saída: 2,4,6 ... 10,20.



for i in range(2,10 + 1):
    for j in range(1,20 + 1):
        if j % i == 0 :
            print(j)
        