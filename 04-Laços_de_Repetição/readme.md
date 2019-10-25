# Laços de Repetição


## Questões

### 1. Sequencia de quadrados
Dado um inteiro positivo N, faça um programa que gere os N primeiros números da seguinte sequência: 1², 2², 3², …, N².

Entrada   | Saida
--------- | ------
2| 1, 4
5| 1,4,9,16,25
6|1,4,9,16,25,36


* [Gabarito](./qst01.lua)

### 2.Sequência Enésimo
Dado um inteiro positivo N, faça um programa que gere os próximos N números da seguinte sequência: 1², 2², 3², …, N², a partir do N-ésimo termo.

Entrada   | Saida
--------- | ------
1| 1
2| 4, 9
4| 16, 25, 36, 49


* [Gabarito](./qst02.lua)
### 3.Valores em um intervalo

Faça um programa que leia um valor inteiro positivo N. Este valor será as próximas N linhas de entrada, onde valores inteiros serão lidos em seguida.
Mostre quantos destes valores X estão dentro do intervalo [10,20] e quantos estão fora do intervalo, mostrando essas informações.

Entrada   | Saida
--------- | ------
2<br>5<br>7| "0 valor(es) dentro do intervalo [10,20]"<br>"2 valor(es) fora do intervalo [10,20]"
3<br>13<br>18<br>1| "2 valor(es) dentro do intervalo [10,20]"<br>"1 valor(es) fora do intervalo [10,20]"
3<br>5<br>3<br>8| "0 valor(es) dentro do intervalo [10,20]"<br>"3 valor(es) fora do intervalo [10,20]"
3<br>10<br>12<br>20|"3 valor(es) dentro do intervalo [10,20]"<br>"0 valor(es) fora do intervalo [10,20]"



* [Gabarito](./qst03.lua)
### 4. Números em um intervalo

Faça um programa que leia os números os inteiros positivos recebidos a partir da entrada padrão, até que um número negativo seja lido. Ao término do programa, ele deve exibir o maior número dado, e em seguida, exibir o menor número não-negativo não-nulo fornecido, além da quantidade de ocorrências desses números. 


Entrada   | Saida
--------- | ------
1<br>3<br>6<br>12<br>10<br>-1| “O maior número é 12, e ocorreu 1 vez(es).” <br>“O menor número é 1, e ocorreu 1 vez(es).”
3<br>4<br>3<br>2<br>0<br>4<br>-100| “O maior número é 4, e ocorreu 2 vez(es).”<br>“O menor número é 2, e ocorreu 1 vez(es).”
180<br>-2|“O maior número é 180, e ocorreu 1 vez(es).”<br>“O menor número é 180, e ocorreu 1 vez(es).”

* [Gabarito](./qst04.lua)


### 5. Soma dos divisores
Escreva um programa que leia um número inteiro e calcule a soma de todos os divisores desse número, com exceção dele próprio. Ex: a soma dos divisores do número 30 é 1 + 2 + 3 + 5 + 6 + 10 + 15 = 32, já para o número 66 é 1 + 2 + 3 + 6 + 11 + 22 + 33 = 78.

Entrada   | Saida
--------- | ------
4| 3
6|6 
30|42
66|78
49|8


* [Gabarito](./qst05.lua)

### 6. Valores Negativos
Ler 10 valores e escrever quantos desses valores lidos são NEGATIVOS.

Entrada   | Saida
--------- | ------
-5 -4 -3 -2 -1 0 1 2 3 4| 5 numeros negativos
-6 9 8 56 -8 5 -1 -56 0 10|4 numeros negativos
-6 9 8 56 -8 5 -1 -56 0 10|4 numeros negativos
6 8 2 57 41 9 32 2 74 55|0 numeros negativos


* [Gabarito](./qst06.lua)
