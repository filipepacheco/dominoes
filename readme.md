# Somando Dominós

#### Filipe Pacheco e Jayme Riegel - UNISINOS, 2022 | Análise e Projeto de Algoritmos

#### Profa. Andriele Busatto do Carmo

### Como executar o programa

Para executar o programa, você deve ter o Python instalado na máquina.

Depois de instalado, apenas rode o comando no console:

```
python main.py <nome_do_arquivo>
```

Onde "main.py" é o algoritmo principal a ser executado e "nome do arquivo" referencia um dos arquivos existentes na
pasta `/test_cases`.

Caso deseje rodar um caso de teste que não está incluso na pasta `/test_cases`, então deve-se adicioná-lo a essa pasta e
passar como parâmetro na linha de comando.

Caso o nome do arquivo seja omitido da linha de comando, ele irá executar por default o arquivo `/test_cases/in3`.

### Solução do problema

Para solucionar o problema de forma eficiente, criamos um algoritmo que mapeia os dominós e faz vários cálculos nos
dominós individualmente e também no conjunto de dominós, como por exemplo a diferença entre os valores de cima e de
baixo, se a diferença é par ou ímpar e qual o valor associado ao swap de um dominó específico.

Esses cálculos são utilizados na hora de decidir qual dominó será escolhido para swap, se é necessário remover um dominó
e qual dominó será escolhido para ser retirado do conjunto.

Esses cálculos são feitos na propriedade `metadata` dos dominós e dos conjuntos de dominós.

### Descrição do problema

O jogo inicia com um jogador recebendo um pequeno conjunto de dominós.
Esses dominós devem ser escolhidos aleatoriamente de um outro conjunto de
peças, esse último grande e variado.

Usando o conjunto de dominós recebido, o
jogador deve encontrar uma combinação na qual os dominós colocados lado a lado
na mesa, devem apresentar a mesma soma tanto para a parte de cima quanto para
a parte de baixo dos dominós. Por exemplo, para o conjunto de dominós `[2, 1], [6,
3], [3, 1]`, uma combinação correta seria:

```
1 6 1
2 3 3
```

Se não for possível encontrar uma combinação usando todos os dominós
escolhidos, o jogador pode descartar um deles, mas o valor da soma na
combinação deve ser a maior possível.
Além disso, se existir mais de um dominó que possa ser descartado mantendo a mesma soma (para a parte de baixo e para a
parte de cima), o jogador deve descartar o dominó `[a, b]` de modo que `a ≤ b` e `a` é o
menor valor possível considerando todos os dominós que podem ser descartados.

Você deve escrever um programa que, dado um conjunto de dominós, tenta
encontrar uma combinação que satisfaz as condições do desafio, descartando um
dominó se necessário. Note que um dominó `[a, b]` também pode ser escrito como
`[b, a]`.