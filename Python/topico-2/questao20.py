#python 2.7.15
#coding: utf-8
"""
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

Para atender a todos os clientes,
cada cliente poderá levar apenas um dos tipos de carne da promoção,
porém não há limites para a quantidade de carne por cliente.
Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra.
Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal,
contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento,
valor do desconto e valor a pagar.
"""
# Escolha do tipo da carne
print '1 - File Duplo'
print '2 - Alcatra'
print '3 - Picanha'
tipoCarne = raw_input('Informe o tipo da carne escolhida: ').upper()
 
# Escolha da quantidade
quantidade = float(raw_input('Informe a quantidade comprada: '))
 
# Verifica cartao
cartaoTabajara = raw_input('Usara cartao Tabajara (S/N): ').upper()
 
print 'CUPOM FISCAL'
 
# Verifica o tipo da carne e calcula o valor bruto
if (tipoCarne == '1'):
    print 'Carne Escolhida: File Duplo'
    if (quantidade <= 5):
        valorBruto = quantidade * 4.9
    else:
        valorBruto = quantidade * 5.8
elif (tipoCarne == '2'):
    print 'Carne Escolhida: Alcatra'
    if (quantidade <= 5):
        valorBruto = quantidade * 5.9
    else:
        valorBruto = quantidade * 6.8
else:
    print 'Carne Escolhida: Picanha'
    if (quantidade <= 5):
        valorBruto = quantidade * 6.9
    else:
        valorBruto = quantidade * 7.8
print 'Valor Bruto', valorBruto
 
# Verifica se possui desconto
desconto = 0.0
if (cartaoTabajara == 'S'):
    print 'Pagamento com cartao Tabajara'
    desconto = valorBruto * 0.05
else:
    print 'Pagamento nao sera com o cartao Tabajara'
print 'Desconto: ', desconto
print 'Valor a Pagar: ', (valorBruto - desconto)
 