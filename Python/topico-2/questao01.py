# -*- coding: utf-8 -*-
""" Sabendo que IMC é o Índice da Massa Corporal e se calcula dividindo o peso da pessoa pela altura, faça um algoritmo que receba a altura em metros, seguido do peso em quilogramas de um indivíduo. Ao final, exiba o IMC dessa pessoa. Além disso, deve-se exibir uma 
mensagem, em forma de string, de acordo com o seu resultado: 
- Caso o IMC seja menor ou igual a 18, imprima "Abaixo do Peso";
- Caso o IMC esteja entre 18 e 25, imprima "Peso Normal";
- Caso o IMC esteja entre 25 e 30, imprima "Obeso Moderado";
- Caso o IMC seja maior ou igual a 40, imprima "Obeso Mórbido"

EXEMPLO:
		entrada: 
1.90
56
		saída: 
15.512	
Abaixo do Peso """


print('Insira a altura do paciente: ')
altura = float(input())
print('Insira o peso do paciente')
peso = float(input())
imc=peso/(altura**2) # **2 significa ao quadrado (a²)
print('IMC: ' + str(round(imc, 3))) # a função str() converte imc de float para string / round() arredonda, no caso em 3 casas após a vírgula
if imc<=18 :
	print('Abaixo do Peso')
elif imc>=18 and imc<=25 : # os sinais de <> devem sempre vir antes do = para indicar maior ou igual e menor ou igual
	print('Peso Normal')
elif imc>=25 and imc<=30 :
	print('Obeso Moderado')
elif imc>=40 :
	print('Obeso Mórbido')
