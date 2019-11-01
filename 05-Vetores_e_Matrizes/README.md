# Vetores e Matrizes


## Questões

### 1. Operações no vetor
Escreva um programa que altere todos os valores de um vetor de tamanho N preenchido com números aleatórios de 1 a 20, se o valor for ímpar deve se multiplicar por 3, se for par deve-se subtrair 1 e multiplicar por 2. no final imprima o vetor antes e depois das alterações serem feitas.



Entrada   | Saida
--------- | ------
3  | 17 8 16<br>51 14 30
5  | 17 8 16 16 19<br>51 14 30 30 57
1  | 17<br>51

* [Gabarito](./qst01.lua)

### 2. Maior e menor
Faça um programa que imprima o menor e o maior valor de um vetor com 100 números aleatórios.

* [Gabarito](./qst02.lua)
### 3. Número em vetor
Faça um algoritmo para ler um vetor de 30 números. Após isto, ler amis um número qualquer, calcular quantas vezes esse número aparece no vetor.
* [Gabarito](./qst03.lua)

### 4. Determinante
Faça um programa que receba os 9 números de uma matriz 3x3 e calcule e imprima o seu determinante.

Entrada   | Saida
--------- |------
1 0 1<br>0 1 0<br>0 0 1| 1
1 2 3<br>1 2 3<br>1 2 3|0
4 0 2<br>1 3 4<br>5 -1 3|20

* [Gabarito](./qst04.lua)

### 5. Eu vi na fila do pão
Faça uma função que receba a altura de N pessoas na fila de uma padaria (As próximas N entradas devem ser as alturas delas) e mostra na tela quantas podem ser vistas pelo padeiro. Use a seguinte assinatura: function visiveisFila(n) .

Entrada|Saida
-|-
4<br>1.90<br>1.65<br>1.85<br>1.84<br>|1 pessoa
3<br>1.70<br>1.65<br>1.85|2 pessoas
4<br>1.65<br>1.83<br>1.85<br>1.90|4 pessoas
* [Gabarito](./qst05.lua)
### 6. Soma de pares
Fça um programa que receba do usurário 10 números. O programa deverá calcular a quantidade de elementos pares e imprimir cada elemento. Deverá também calcular e exibir a soma de todos esses elementos. Caso nenhum dos elementos sejam pares, exiba a seguinte mensagem: "Não há elementos pares".

Entrada|Saida
-|-
2<br>7<br>9<br>6<br>4<br>2<br>10<br>11<br>24<br>14|"Existem 7 elementos pares"<br>"2,6,4,2,10,24,14"<br>"Soma de pares = 62"
9<br>5<br>7<br>33<br>11<br>15<br>19<br>1<br>147<br>23|"Existem 0 elementos pares"<br>"Não há elementos"
0<br>165<br>183<br>185<br>91<br>17<br>29<br>3<br>7<br>9|"Existem 1 elementos pares"<br>"0"<br>"Soma de pares = 0"
* [Gabarito](./qst06.lua) 


### 7. Ordenar Vetor
Escreva uma função ```function ordenaVetor(v)``` que recebe um  vetor de inteiros de tamanho 10, a função deve ordenar vetor de forma crescente



Entrada   | Saida
--------- | ------
3 8 7 1 10 1 -7 3 1 17  | -7 1 1 1 3 3 7 8 10 17
10 9 8 7 6 5 4 3 2 1    | 1 2 3 4 5 6 7 8 9 10
8 7 1 3 19 18 2 15 20 10  | 1 2 3 7 8 10 15 18 19 20

* [Gabarito](./qst07.lua)

### 8. Operando uma matriz
Faça um programa que receba do usuário a quantidade de linhas e colunas de uma matriz e que preencha essa matriz com números aleatórios menores 10. Imprima a matriz gerada, a transposta da matriz, a diagonal principal e o triângulo superior.
>Tente usar a função io.write() para imprimir a linha da matriz.

Entrada   | Saida
------ | ------
3<br>3 | "Matriz gerada:"<br>2 &nbsp;4 &nbsp;5<br>3 &nbsp;6 &nbsp;8<br>7 &nbsp;1 &nbsp;2<br>"Matriz transposta:"<br>2 &nbsp;3 &nbsp;7<br>4 &nbsp;6 &nbsp;1<br>5 &nbsp;8 &nbsp;2<br>"Diagonal principal:"<br>2<br> &nbsp;  &nbsp;6<br> &nbsp;  &nbsp; &nbsp; &nbsp;2<br>"Triângulo superior:"<br> &nbsp;4 &nbsp;5<br> &nbsp; &nbsp; &nbsp;8

* [Gabarito](./qst08.lua)
