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


### 5. Primos menores que 10
Faça uma função que calcule se um inteiro positivo, desde que seja menor que 10, é ou não um número primo. Ele deve retornar um valor booleano.

Entrada   | Saida
--------- | ------
3         | true
6         | false
7         | true

* [Gabarito](./qst05.lua)


### 6. Conversão de Temperatura
Faça uma função que converta uma temperatura dada em Fahrenheit para Celsius ou Kelvin, dependendo da conversão sinalizada.

Entrada   | Saida
--------- | ------
212 “Celsius”    | 100 °C
8 “Kelvin”       | 303,15 K
86 “Celsius”     | 30 °C

* [Gabarito](./qst06.lua)


### 7. Melhor nem se Aposentar
Implemente uma função com a seguinte assinatura:
    ```function temAposentadoria(idade, tempoTrabalho)```
Para um trabalhador receber sua aposentadoria, ele deve ter no mínimo 65 anos de idade e ter trabalhado no mínimo 30 anos. A função deve retornar um valor booleano.

Entrada   | Saida
--------- | ------
73 30     | true
86 20     | false
64 40     | false

* [Gabarito](./qst07.lua)


### 8. Aposentadoria 2019
Usando a função acima (fazendo chamadas a ela, durante a execução do programa), implemente outra função, que deve receber o nome do trabalhador, o ano de nascimento, ano de ingresso na empresa e imprima “TRABALHADOR tem aposentadoria em 2019.” ou “TRABALHADOR não tem aposentadoria em 2019.” , onde TRABALHADOR é o nome do empregado. Informe na execução dessa função o motivo dele não ter aposentadoria.

Entrada   | Saida
--------- | ------
“João” 1954 1989    | “João tem aposentadoria em 2019.”
“Maria das Dores” 1943 1993    | “Maria das Dores não tem aposentadoria em 2019.”<br>“Trabalhe mais 4 anos.”
“Enzo” 1990 2003   | “Enzo não tem aposentadoria em 2019.”<br>“Trabalhe mais 14 anos.”<br>“Muito novo para se aposentar.”


* [Gabarito](./qst08.lua)


### 9. Eu vi na fila do pão
Faça uma função que receba a altura de N pessoas na fila de uma padaria (As próximas N entradas devem ser as alturas delas) e printa quantas podem ser vistas pelo padeiro. Use a seguinte assinatura: ```function visiveisFila (n)``` .

Entrada   | Saida
--------- | ------
4<br>1.90<br>1.65<br>1.85<br>1.84 | “1 pessoa”
3<br>1.70<br>1.65<br>1.85 | “2 pessoas”
4<br>1.65<br>1.83<br>1.85<br>1.90 | “4 pessoas”

* [Gabarito](./qst09.lua)

