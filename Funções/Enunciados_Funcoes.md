# Condições


## Questões

### 1. Peso Ideal do Atleta
Faça uma função que receba a altura (m), e o gênero de um(a) atleta (M ou F), e que retorne o peso ideal (Kg) para esse indivíduo. Utilize as seguintes fórmulas:
>Homens: (72.3 * h) - 58.2
>Mulheres: (62.7 * h) - 45.2


Entrada   | Saida
--------- | ------
1.85 “M”  | 75,55 Kg
1.90 ”F”  | 73.93 Kg
1.73 “M”  | 66.87 Kg

* [Gabarito](./qst01.lua)


### 2. Nota Média do Aluno
Faça uma função que calcule a média das notas de um aluno. Ela deve ter a seguinte assinatura:
    ```function mediaAluno(nota1, nota2, nota3, tipoMedia)```
onde nota1, nota2 e nota3 são as notas do aluno, já tipoMedia é uma das seguintes médias: aritmética ou ponderada com pesos 2 4 e 2.

Entrada   | Saida
--------- | ------
9.5 10.0 9.0 “aritmetica”  | 9,5
9.5 10.0 9.0 “ponderada”   | 9.65
10.0 4.5 10 “ponderada”    | 7.25

* [Gabarito](./qst02.lua)


### 3. Área do Quadrado
Faça uma função que receba as coordenadas de 4 pontos quaisquer no plano cartesiano e em qualquer ordem, e retorne a área do quadrado formado por esses pontos. Caso não seja possível formar um quadrado, imprima essa informação em tela. Desconsidere rotações do polígono (Os lados do quadrado são paralelos aos eixos X e Y). 

Entrada   | Saida
--------- | ------
0 0<br>0 4<br>9 0<br>9 4 | “Não formou um quadrado.”
2 2<br>2 5.5<br>5.5 2<br>5.5 5.5 | 12,25
8 1<br>3 6<br>8 6<br>3 1 | 25
4 3<br>3 4<br>4 6<br>3 6 | “Não formou um quadrado.”

* [Gabarito](./qst03.lua)


### 4. Subtração do Maior pelo Menor
Faça uma função que receba três inteiros A, B e C e que retorne a subtração do maior dos 3 números pelo menor.

Entrada   | Saida
--------- | ------
0 3 4    | 4
2 2 2    | 0
8 1 5    | 7

* [Gabarito](./qst04.lua)

