'''
  Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.

  1. HOT DOG-4,00
  2. X-salada-5,00
  3. X-bacon 5,00
  4. Torrada simples 2,00
  5. Refri 1,50
'''

print("1. HOT DOG-4,00 \n 2. X-salada-5,00 \n 3. X-bacon 5,00 \n 4. Torrada simples 2,00 \n 5. Refri 1,50")

print("Qual o seu pedido: ")
pedido = int(input())
print("Quantas porções deseja: ")
qntd = int(input())

if(pedido == 1):
    print("valor: ",qntd*4)
elif(pedido == 2):
    print("valor: ",qntd*5)
elif(pedido == 3):
    print("valor: ",qntd*5)
elif(pedido == 4):
    print("valor: ",qntd*2)
elif(pedido == 5):
    print("valor: ",qntd*1.5)