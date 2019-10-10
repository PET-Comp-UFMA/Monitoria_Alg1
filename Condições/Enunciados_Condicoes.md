# Condições


## Questões

### 1.  Índice de Massa Corporal
Faça um algoritmo que receba a altura (m), seguido do peso (kg) de um indivíduo. Ao final, exiba o IMC dessa pessoa. Além disso, deve-se exibir uma mensagem, em forma de string, de acordo com o seu resultado: Caso o IMC  seja menor ou igual a 18, imprima “Abaixo do Peso”. Senão, caso seja entre 18 e 25, imprima “Peso Normal”. A partir do IMC 25, desde que seja menor que 30, imprima “Sobrepeso”, senão, imprima “Obeso Moderado” (desde que que não chegue a 40). Caso o IMC seja maior ou igual a 40, exiba em tela a mensagem “Obeso Mórbido”.

>OBS: Cuidado com o uso do ponto e da vírgula! Geralmente em linguagens de programação, o ponto separa a parte inteira da parte decimal de um número.

Entrada   | Saida
--------- | ------
1.90 56   | 15.512<br>“Abaixo do Peso”
1.65 96   | 35,261<br>“Obeso Moderado”
1.70 67   | 23,183<br>“Peso Normal”

* [Gabarito](./qst01.lua)


### 2. Saldo Bancário
A partir do saldo bancário inicial, um cliente teve débitos e créditos ao longo do mês. Faça um algoritmo para ler o saldo inicial, o total de débitos e o total de créditos, em reais (R$). Assim, você deve imprimir o saldo final do cliente, através da mensagem “Saldo positivo em SALDO”, ou “Saldo negativo em SALDO”, onde SALDO é o resultado do processamento, o saldo final em R$. Caso o Saldo seja de R$0,0, imprima “Saldo zero”.

Entrada   | Saida
--------- | ------
   1500.00 300.00 600.00  | “Saldo positivo em R$ 1800,00”
   3300.00 4000.00 100    | “Saldo negativo em R$600,00”
   2200 3000 800   | “Saldo zero”

* [Gabarito](./qst02.lua)


### 3.  Máquina f
Uma máquina, que tem um comportamento de uma função matemática f, recebe um valor numérico inteiro x e exibe um respectivo resultado. Essa função é dada por:
 
>f(x) = x^2 , para todo x tal que ( |x| mod 2 = 0),<br>= x^3 , para todo x tal que ( |x| mod 2 = 1 OU x < 0).   

Em outras palavras, essa máquina imprime o quadrado desse número, caso ele seja par, caso contrário, ele exibe o cubo desse mesmo número se ele for ímpar ou negativo. Escreva um algoritmo que tenha o mesmo comportamento da função f.
Considere o ZERO um número PAR, e para números menores que zero, o seu valor absoluto (módulo de X, ou |x|) para definir se é par ou ímpar. MOD é a operação matemática de resto da divisão.

Entrada   | Saida
--------- | ------
10        | 100
3         | 27
-3        | -27
2         | 4
-2        | 4

* [Gabarito](./qst01.lua)

