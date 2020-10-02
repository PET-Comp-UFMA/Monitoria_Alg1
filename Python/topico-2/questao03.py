# -*- coding: utf-8 -*-
"""
. Pelas regras da UFMA, toda disciplina é composta de 3 avaliações obrigatórias. Se um aluno
tem média superior ou igual a 7 (sete) nas três avaliações, ele é considerado “Aprovado por
média.”. Se tiver média inferior a 7 (sete), tem direito a uma quarta prova, chamada de
reposição, que substituiu a menor nota das três provas anteriores (se a nota da reposição for
maior que ela). Após a reposição, se as três maiores notas formarem uma média igual ou
superior a 7 (sete), o aluno é considerado “Aprovado na reposição.”. Finalmente, apenas se tiver
a média com a reposição inferior a 7 (sete), ele faz uma quinta prova, chamada de final, em que
é considerado “Aprovado na final.” se a soma da média com a reposição e a nota da prova final
for igual ou maior que 12 (doze). Nesse último caso, caso a soma da média com reposição e
prova final for inferior a 12 (doze), o aluno é dito como “Reprovado.”. Faça um programa que
lê as três notas obrigatórias de uma disciplina e depois, apenas se necessário, lê as notas da
reposição e final. O programa deve dar como saída as frases “Aprovado por média.”, “Aprovado
na reposição”. “Aprovado na final.” ou “Reprovado.” respectivamente em cada uma dessas
situações conforme a descrição anterior.
"""
print('insira as 3 notas respectivamente:')
nota1,nota2,nota3 = int(input()),int(input()),int(input())
media = (nota1+nota2+nota3)/3
soma2 = 0
print('media inicial: ' + str(round(media,2)))
if media<7 :
	print('insira a nota da reposição:')
	if nota1<nota3 and nota1<nota2 :
		rep = int(input())
		soma2 = nota2+nota3
	elif nota2<nota1 and nota2<nota3 :
		rep = int(input())
		soma2 = nota1+nota3
	elif nota3<nota1 and nota3<nota2 :
		rep = int(input())
		soma2=nota2+nota1
	
	if rep>=nota1 or rep>=nota2 or rep>=nota3 :
		media=(soma2+rep)/3
		print('media com a reposição: ' + str(round(media,2)))
	
	if media<7 :
		print('insira a nota da final: ')
		final=int(input())
		media=(media+final)/2
		print('media com a final: ' + str(round(media,2)))
		if media<6 :
			print('Reprovado')
		else: print('Aprovado na final')
		
	else: 
		print('Aprovado na reposição')
	
else:
	print('Aprovado por média')



