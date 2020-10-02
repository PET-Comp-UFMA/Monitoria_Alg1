# um programa que calcule a media de um aluno
'''
serão dadas tres notas que serão somadas e divididas por tres
'''

print("Quais foram as notas do aluno? ")
n1,n2,n3 = int(input()),int(input()),int(input())
media = (n1+n2+n3)/3 #observe que a média se torna uma variável de ponto flutuante
print("A media do aluno é: ",media)