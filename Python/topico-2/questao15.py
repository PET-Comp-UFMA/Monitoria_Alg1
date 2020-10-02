# -*- coding: utf-8 -*-
"""
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
receberá ainda um desconto de 10% sobre este total.
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
"""

print("Quantidade de maçãs em Kg: ")
qntdMacas = float(input())
print("Quantidade de morangos em Kg: ")
qntdMorangos = float(input())
precoMacas = 0
precoMorangos = 0 
precoTotal = 0
qntdTotal = qntdMacas + qntdMorangos
if qntdMorangos <= 5:
    precoMorangos = qntdMorangos * 2.5
else: 
    precoMorangos = qntdMorangos * 2.2

if qntdMorangos <= 5:
    precoMacas = qntdMacas * 1.8
else: 
    precoMorangos = qntdMorangos * 1.5

precoTotal = precoMacas + precoMorangos

if precoTotal > 25 or qntdTotal > 8:
    precoTotal =  precoTotal - (precoTotal*0.1)
    print("Preço: " + str((precoTotal)))
else: 
    print("Preço: " + str((precoTotal)))


