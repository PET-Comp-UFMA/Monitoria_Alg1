# -*- coding: utf-8 -*-
"""
Lao Tsung foi chamado à corte do imperador da China para participar de um desafio
mortal. Ele deve dizer um número que atenda às vontades do imperador. Se conseguir,
receberá um cargo na corte. Se o número não servir, Tsung será executado. Para sorte dele
ele tem a ti, o espírito guardião programador. Ajude-o a sair dessa vivo.
Faça um programa que exiba uma mensagem de true ou false, para um número
inserido pelo usuário. Esse número deve atender ao pedido do imperador:
- “Eu exijo um numeral que esteja de 23 a 43 e não seja divisível por 5 ou por 3, ou um cujo
último algarismo seja menor ou igual a 5 e o triplo do número está de 20 a 50, e, nesse
caso, esse triplo não pode ser divisível por 5 e 3 ao mesmo tempo.”
"""

num = int(input()) 
trip=num*3

if ((num>=23 and num<=43) and (num%5!=0 or num%3!=0) ) or ( (num%10<=5) and (trip>=20 and trip<=50) and trip%5!=0) :
    print("VERDADEIRO")
else:
	print("FAlSE")



