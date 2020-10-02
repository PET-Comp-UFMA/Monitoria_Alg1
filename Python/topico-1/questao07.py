''' 
    Jimmy O’Neil é um espião irlandês, infiltrado na Inglaterra para conseguir
 informações confidenciais sobre o governo, mas só pra garantir que está tudo tranquilo no
 país, sem segundas intenções por trás... Claro que não, né? Ele precisa se comunicar com
 sua central de inteligência, mas só pode fazê-lo com um código engenhoso de números de
 três dígitos. O primeiro e último dígito são só para enganar. O que importa é o dígito do
 meio.
 Faça um programa que, dado um número de três dígitos, possa exibir apenas o
 dígito do meio, facilitando a decodificação da mensagem.
 Exemplo de entrada:
 375
 Saída de acordo com exemplo:
 7
'''
n = int(input()) # entra com um valor
n = int((n%100) /10) 
print(n)

# primeiro você pega o resto da divisão desse numero por 100 e depois divide esse numero por 10, arredondando para baixo