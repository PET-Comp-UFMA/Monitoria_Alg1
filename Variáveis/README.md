# Variáveis


## Questões

### 1. Hello World
Uma prática muito bem difundida entre os programadores é que, em cada nova linguagem que eles aprendem, experimentem em seu primeiro programa a exibição de uma mensagem em tela. Em seu primeiro programa, apenas imprima a string “Hello World !”, usando a função de sistema já implementada em sua linguagem.

>OBS: Experimente guardar a string em uma variável, e tente imprimir o valor dessa variável, assim como fazer modificações em seu conteúdo, como mudar a string, inserir um valor numérico ou booleano na variável.

Entrada   | Saida
--------- | ------
   ---    | “Hello World !”
   ---    | "Good Bye ! ”
   ---    | True
   ---    | 80

* [Gabarito](./qst01.lua)


### 2. Soma e Produto dois números
Dado dois números A e B, calcular:
a) a sua soma e imprimí-la em tela, seguindo o formato: “A soma de A e B é S.”, onde S é a soma A+B.
b) o seu produto e imprimí-lo em tela, seguindo o formato: “O produto de A e B é P.”, onde P é o produto A.B.


Entrada   | Saida
--------- | ------
   2 1    | “A soma de 2 e 1 é 3.”<br>“O produto de 2 e 1 é 2.”
   0 10   | “A soma de 0 e 10 é 10.”<br>“O produto de 0 e 10 é 0.”
   6 4    | “A soma de 6 e 4 é 10.”<br>“O produto de 6 e 4 é 24.”

* [Gabarito](./qst02.lua)


### 3. Cubo de um número
Dado um número A, calcular o seu valor elevado ao cubo e imprimí-lo em tela, seguindo o formato: “O cubo de A é C.”, onde C é A^3.

Entrada   | Saida
--------- | ------
   2      | “O cubo de 2 é 8.”
   0      | “O cubo de 0 é 0.”
   4      | “O cubo de 4 é 64.”

* [Gabarito](./qst03.lua)


### 4. Inverter Número
Dado um número A, de quatro dígitos, imprimir seus dígitos em ordem invertida.
Dessa forma, está vetado receber como entrada cada dígito do teclado em variáveis distintas

Entrada   | Saida
--------- | ------
   1013   | 3101
   4321   | 1234
   1001   | 1001

* [Gabarito](./qst04.lua)


### 5. Divisão Inteira entre dois números
Dado dois números A e B, calcular a sua razão e imprimí-la em tela, seguindo o formato: “A razão entre A e B é R.”, onde R é a divisão inteira A/B. É possível que o resultado R seja apresentado como um número de ponto flutuante (número real não-inteiro, tipo, 0.2, 1.1 ou 4.5). O desafio é obter um R inteiro usando apenas a aritmética básica (usando + - * / %). Está vetado o uso de bibliotecas.

Entrada   | Saida
--------- | ------
   2 1    | "A razão entre 2 e 1 é 2.”
   0 10   | “A razão entre 0 e 10 é 0.”
   1 2    | “A razão entre 1 e 2 é 0.”
   4 3    | “A razão entre 4 e 3 é 1.”

* [Gabarito](./qst05.lua)


### 6. Tipos de variáveis
Dado uma variável A que receba qualquer informação de entrada do usuário, escreva um programa que imprima em tela o tipo de dado dessa variável, seguindo o formato: “O tipo da variável é TIPO.”, onde TIPO é um dos tipos de variáveis definidos na linguagem utilizada.
(ex: em linguagens da família C, temos int, float, double, char, etc…, já em Lua, temos string, number, boolean, nil, etc...). Não use estruturas IF. Bibliotecas nativas são permitidas.

Entrada   | Saida
--------- | ------
   2      | “O tipo da variável é number.”
   2.3    | “O tipo da variável é number.”
   True   | “O tipo da variável é boolean.”
   ‘A’    | “O tipo da variável é string”
“Exercício da Monitoria”| “O tipo da variável é string”

* [Gabarito](./qst06.lua)


### 7. Multiplos de um número
Escreva um programa que leia um número inteiro e exiba como resultado o seu dobro, e em seguida o seu triplo, concatenados.

Entrada   | Saida
--------- | ------
   2      | 46
   1      | 23
   0      | 00

* [Gabarito](./qst07.lua)


### 8. Teto de inteiros positivos
Faça um programa que receba como entrada um número real qualquer, e que imprima em tela um número inteiro maior ou igual à entrada, usando a função teto. Caso o número seja negativo, ele deve ser tratado como número positivo. Não utilize estruturas IF.

Entrada   | Saida
--------- | ------
   2      | 2
   2.3    | 3
   -1     | 1
   4      | 4
   4.001  | 5
  -4.001 | 5

* [Gabarito](./qst08.lua)


### 9. Três Reais
Escreva um programa que leia três variáveis reais A, B e C, e exiba uma linha com o resultado do seguinte cálculo: a soma do 1º número com 2º, multiplicado pela soma do 2º pelo 3º. Na linha seguinte, exibir o resultado do triplo da soma dos 3 números.

Entrada   | Saida
--------- | ------
   1 2 3  | 15<br>18
   0 1 2  | 3<br>9
   2 2 2  | 16<br>18
   1 0 1  | 1<br>6

* [Gabarito](./qst09.lua)


### 10. Permuta
Faça um programa que receba 3 entradas quaisquer A, B e C. Espera-se que o programa faça as seguintes permutações dois a dois: entre os conteúdos das variáveis A e B; B e C; em seguida B e A; e por último, A e C. Em cada permuta, o programa deve exibir o conteúdo atual de cada variável.

Entrada   | Saida
--------- | ------
   “ABC”<br>100<br>true | “A = 100 , B = “ABC”, C = true ”<br>“A = 100 , B = true, C = “ABC” ”<br>“A = true , B = 100, C = “ABC” ”<br>“A = “ABC” , B = 100, C = true ”
   10<br>4<br>2  | “A = “4 , B = 10, C = 2 ”<br>“A = 4 , B = 2, C = 10 ”<br>“A = 2 , B = 4, C = 10 ”<br>“A = 10 , B = 4, C = 2 ”
   
* [Gabarito](./qst10.lua)


### 11. Dias de Vida
Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade dessa pessoa expressa apenas em dias. Considere que um ano tem 365 dias e um mês tem 30 dias.

Entrada   | Saida
--------- | ------
 19 6 12  | 7127 dias
 40 5 10  | 14760 dias
   
* [Gabarito](./qst11.lua)


### 12. Evento da fábrica
Leia um valor inteiro, que é a duração em segundos para que um determinado evento em uma fábrica ocorra. Informe esse período de tempo, expressando-o no formato horas:minutos:segundos.

Entrada   | Saida
--------- | ------
 8546     | 2:22:26
 0        | 0:0:0
 85       | 0:1:25
   
* [Gabarito](./qst12.lua)


### 13. Contabilizar Eleitorado
Faça um algoritmo para ler o número total de eleitores, o número de votos brancos, nulos e válidos de um município. Calcular e escrever o percentual que cada um representa em relação ao total de eleitores.

Entrada   | Saida
--------- | ------
 1000<br>5000<br>2500<br>2500 | Validos: 50%<br>Brancos: 25%<br>Nulos: 25%
 650<br>500<br>100<br>50 | Validos: 76,9%<br>Brancos: 15,3%<br>Nulos: 7,8%
   
* [Gabarito](./qst13.lua)


