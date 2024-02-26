# selection-sort
estudo sobre o algoritmo de ordenação selection sort 

Algoritmo Selection Sort
O selection sort consiste em selecionar o menor item e colocar na primeira posição,
selecionar o segundo menor item e colocar na segunda posição, segue estes
passos até que reste um único elemento.
![selection-sort-animation-1](https://github.com/vinicius171/selection-sort/assets/80222322/dbc1a549-0468-4f16-8944-adfbb4d8cb5f)



Para todos os casos (melhor, médio e pior caso) possui complexidade C(n) = O(n²) e não é um algoritmo estável.
Para calcularmos o número de operações feita pelo algoritmo podemos usar uma
fórmula bem simples, n * (n — 1) / 2, onde n é o tamanho da lista.
Logo, abstraindo a fórmula acima:
n * (n — 1) / 2 = (n² — n) / 2
Para análise assintótica, podemos ignorar os valores constantes. O que importa
mesmo é o n² / 2 , pois conforme a lista crescer, este valor irá aumentar
quadraticamente. Por isso, o algoritmo selection sort possui tempo de execução
O(n²).
Resolvemos implementar o código em python e criar uma função que lê um arquivo
de texto que contém os dados. Isso pode diminuir o desempenho do algoritmo
causando um maior atraso na execução.
O arquivo de texto que iremos utilizar foi criado a partir de um código que gera
números aleatórios no intervalo de [-100, 100], cada linha tem no máximo 3
caracteres podendo haver repetições.
Conclusão:
Era de nosso conhecimento que esse algoritmo não era amplamente recomendado
em tarefas de ordenação muito grandes. Em pequenas listas o desempenho foi
muito bom, o programa conseguiu lidar rapidamente com esse tipo de lista, porém
ao aumentarmos para uma lista com 1000 linhas foram gastos 215.4198 = 4
minutos.
utilizando a fórmula para calcular o número de operações chegamos em um número
total de 499500 operações em uma lista de tamanho 1000, o programa começou a
demonstrar maior dificuldade em processar todos dados. aumentamos novamente para ver qual seria o comportamento do programa, a lista
agora tinha um tamanho de 10000 linhas, o tempo gasto foi de 2353.63sec = 40
minutos.
Com 1 milhão de linhas os nossos computadores travaram, diversos programas
fecharam incluindo o Visual Studio. Escolher o python para a implementação não foi
a melhor opção.
Com o resultado dos tempos de execução colhidos podemos estipular um número
para testes com lista de 1000000 até 2000000 caracteres,
Ao compararmos a velocidade gasta nos três algoritmos para executar a tarefa de
ordenação, o algoritmo selection sort demonstrou ser o mais lento, mesmo com uma
quantidade de dados pequena comparada às que foram utilizadas nos outros
algoritmos.

![image](https://github.com/vinicius171/selection-sort/assets/80222322/e06b6d16-b4a9-47aa-aeef-6bad35f211b3)
