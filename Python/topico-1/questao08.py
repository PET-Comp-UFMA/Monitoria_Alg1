'''
O agente D da Organização Multicultural Intergaláctica Brasileira, OMIB, fez o primeiro contato com uma forma de vida alienígena que está visitando a Terra. É parte
importante do processo de diplomacia perguntar a idade do alienígena. Cientistas calcularam que o planeta do alienígena se comporta de forma idêntica à Terra, porém o ET
disse que sua raça tem uma outra medição para meses e anos. Portanto, o agente D precisa perguntar a idade dele em dias. Você é do time de programação da OMIB, então
deve ajudar.
Faça um programa que dado um número D de dias, exibe quantos anos, meses e
dias o alienígena tem. Tome sempre um ano com 365 dias e um mês com 30 dias.
'''

# ENTRADA: 400
# SAIDA: 1 ano(s), 1 mês(es) e 5 dia(s)

print("Entre com um valor:")
nDias = int(input()) # entra com um valor

ano = int(nDias/365)
meses = int((nDias-(ano*365))/30)
dias = nDias - (ano*365) - (meses*30)

print(ano ,  " ano(s) e " , meses , " mes(es) e " , dias , " dia(s)")

'''
  encontre primeiro os anos e depois os meses
  nDias = nDias/365
  subtrai 

'''