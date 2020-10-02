# -*- coding: utf-8 -*-
"""
Elabore um algoritmo que calcule o que deve ser pago por um produto,
considerando o preço normal de etiqueta e a escolha da condição de pagamento.
Utilize os códigos da tabela a seguir para ler qual a condição de pagamento escolhida e efetuar o cálculo adequado.  
Código Condição de pagamento: 

1 À vista em dinheiro ou cheque, recebe 10% de desconto
2 À vista no cartão de crédito, recebe 15% de desconto
3 Em duas vezes, preço normal de etiqueta sem juros
4 Em duas vezes, preço normal de etiqueta mais juros de 10%  

"""
print("Nome do produto: ")
produto = input()
print("Valor do Produto: ")
precoProduto = float(input())
print("Código de pagamento: \n1-À vista em dinheiro ou cheque, recebe 10%' de desconto\n2-À vista no cartão de crédito, recebe 15%' de desconto\n3-Em duas vezes, preço normal de etiqueta sem juros\n4-Em duas vezes, preço normal de etiqueta mais juros de 10%")
codigo = int(input())

if codigo == 1:
    precoFinalProduto = precoProduto - (precoProduto*0.1)
    print("O preço a pagar por " + produto + ": R$" + str(precoFinalProduto))
elif codigo == 2:
    precoFinalProduto = precoProduto - (precoProduto*0.15)
    print("O preço a pagar por " + produto + ": R$ " + str(precoFinalProduto))
elif codigo == 3:
    precoFinalProduto = precoProduto/2
    print("Preço a pagar por " + produto + " 2x de R$" + str(precoFinalProduto))
else:
    precoFinalProduto = (precoProduto/2) + (precoProduto*0.1)
    print("Preço a pagar por " + produto + " 2x de R$" + str(precoFinalProduto))            
