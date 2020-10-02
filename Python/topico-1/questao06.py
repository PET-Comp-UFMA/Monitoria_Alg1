## calcular o salário de um vendedor 
'''
    considere que ele recebe um salário fixo e ganhe também pela comissão
    exemplo:
    salario = 500
    vendas = 50
    salário + comissão da venda = 507

'''

vendas = int(input())
salario = int( 500 + (0.15 * vendas) )
print(salario)