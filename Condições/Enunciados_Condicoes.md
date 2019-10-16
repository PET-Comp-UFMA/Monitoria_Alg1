# Condições


## Questões

### 1. Índice de Massa Corporal
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


### 3. Máquina f
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

* [Gabarito](./qst03.lua)

### 4. Consumo de um carro
Um modelo novo do carro Xport não é considerado um automóvel econômico, já que percorre 9 Km/Litro. O senhor Antônio Silva tem um carro da concorrente AutoCars, e após uma viagem de férias com a família, ele registrou a distância percorrida (Km) e a quantidade de combustível consumido (L). Faça um algoritmo que ajude esse paizão a decidir se ele deve trocar seu carro, lendo a partir da entrada do programa, as respectivas informações de consumo, que imprima o consumo médio do AutoCars. 
Além disso, se a média de consumo for no mínimo 15 Km/L, seu programa deve imprimir a mensagem “É econômico”, senão, imprima “Não é econômico”. Caso o consumo do carro do Antônio seja pior que um carro da marca rival, escreva a mensagem “Sr. Antônio, melhor trocar de carro”

Entrada   | Saida
--------- | ------
300 20    | 15 Km/L<br>“É econômico”
300 33    | 10 Km/L<br>“Não é econômico”
180 30    | 6 Km/L<br>“Não é econômico”<br>“Sr. Antônio, melhor trocar de carro”

* [Gabarito](./qst04.lua)


### 5. Divisível ou não?
Faça um programa que indique se um número inteiro A é divisível por outro inteiro B (tal que 0 <= (A,B) <= 10). A é a entrada do usuário, e B é um número aleatório, gerado aleatoriamente pela execução do programa. Caso A não seja divisível por B, imprima também o seu resto.

>OBS: Use as funções built-in ou de bibliotecas da linguagem para gerar números aleatórios.

Entrada   | Saida
--------- | ------
4         | “4 é divisível por 2”
6         | “6 não é divisível por 5”<br>“Resto = 1”
6         | “6 é divisível por 3” 

* [Gabarito](./qst05.lua)


### 6. Divisível ou não? V2.0
Assim como na questão anterior, faça um programa que indique se um número inteiro A é divisível por outro inteiro B. A é a entrada do usuário, e B é um número aleatório entre 2 e 10, gerado pela execução do programa. Dessa vez, utilize uma única variável booleana, imprimindo o seu valor na tela.

Entrada   | Saida
--------- | ------
4         | true
6         | false
6         | true 

* [Gabarito](./qst06.lua)


### 7. Inteiro qualquer
Faça um programa que recebe um número inteiro qualquer, caso ele seja negativo imprima o valor positivo, caso ele seja entre 1 e 10  exiba o número elevado ao quadrado, e caso seja maior que dez retorna a raiz do número.

Entrada   | Saida
--------- | ------
4         | 16
11        | 3.316624...
-8        | 8 
-11       | 11

* [Gabarito](./qst07.lua)


### 8. Melhor de Três
Dois jogadores de Street Fighter V competem um melhor de 3 rounds. Não basta saber o Hadouken, o jogador que nocautear o oponente em no mínimo 2 rodadas, vence a disputa. Faça um programa que recebe um fluxo de três booleanos, indicando em quais rounds o Honda foi melhor que o Blanka. 
Antes de cada entrada, imprima uma mensagem indicando o Round atual (Round 1, 2 e Final Round), já ao final de cada round, exceto o último, imprima o nome do vencedor., abortando a entrada quando necessário .
Por fim, Imprima “O vencedor da luta é LUTADOR!”, onde LUTADOR é o nome do Honda ou do Blanka. 

Entrada   | Saida
--------- | ------
True True         | “Round 1”<br>“Honda”<br>“Round 2”<br>“O vencedor da luta é Honda!”
True False True        |“Round 1”<br>“Honda”<br>“Round 2”<br>“Blanka”<br>“Final Round”<br>“O vencedor da luta é Honda!”
False False        | “Round 1”<br>“Blanka”<br>“Round 2”<br>O vencedor da luta é Blanka!”

* [Gabarito](./qst08.lua)


### 9. Melhor de Três
Dessa vez, os fãs de Street Fighter decidem competir um melhor de 5 rounds no Mortal Kombat. Só pra zoar, modifique o programa anterior e adicione um easter egg (“Toasty!!!”), caso alguma das entradas seja um valor inválido, interrompendo o fluxo de entradas. Os lutadores agora são Scorpion e SubZero. 

Entrada   | Saida
--------- | ------
True True False False True         | “Round 1”<br>“Scorpion”<br>“Round 2”<br>“Scorpion”<br>“Round 3”<br>“SubZero”<br>“Round 4”<br>“SubZero”<br>“Final Round”<br>“O vencedor da luta é Scorpion!”
True Nil         | “Round 1”<br>“Scorpion”<br>“Toasty!!!”.
False True True True        | “Round 1”<br>“SubZero”<br>“Round 2”<br>“Scorpion”<br>“Round 3”<br>“Scorpion”<br>“Round 4”<br>“O vencedor da luta é Scorpion!”

* [Gabarito](./qst09.lua)


### 10. Triângulos
Dado os três lados de um triângulo, faça um programa que indique se esse triângulo é equilátero, isósceles ou escaleno.
>OBS: Observe que os lados só formam um triângulo se o comprimento de cada lado for sempre menor que a soma dos outros dois lados.(Exiba uma mensagem de erro, caso o critério não seja satisfeito).

Entrada   | Saida
--------- | ------
5 5 5 | “Equilátero”
7 6 7 | “Isósceles”
3 4 5 | “Escaleno”

* [Gabarito](./qst10.lua)


### 11. Sou de maior
Faça um algoritmo que leia a idade de uma pessoa e imprima a seguinte mensagem, caso ela tenha ao menos 18 anos: “Você é maior de idade”. Se a pessoa for menor de idade, imprima “Você é menor de idade”.

Entrada   | Saida
--------- | ------
14 | “Você é menor de idade”
45 | “Você é maior de idade”

* [Gabarito](./qst11.lua)


### 12. Maior de 3
Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “é o maior”. 

Entrada   | Saida
--------- | ------
4 5 7 | 7 é o maior
-5 19 0 | 19 é o maior

* [Gabarito](./qst12.lua)


### 13. Números restantes
Escreva um programa que receba como entrada 3 números diferentes de 1 a 5, e imprima os 2 números restantes

Entrada   | Saida
--------- | ------
1 2 3 | 4 5
5 1 2 | 3 4

* [Gabarito](./qst13.lua)

