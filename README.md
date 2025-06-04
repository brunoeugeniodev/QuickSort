🚀 Comparação de Implementações do QuickSort
📖 Introdução
Este projeto explora diferentes abordagens do algoritmo QuickSort, incluindo versões recursiva e iterativa, além de análises sobre sua separação e comportamento em diferentes entradas. A finalidade é identificar vantagens, desvantagens e possíveis melhorias na lógica de ordenação.

⚙️ Estruturas Abordadas
QuickSort Recursivo e Iterativo

Comparação de desempenho e análise de tempo de execução.

Implementações em Python.

Lógica de Separação no QuickSort

Discussão sobre uma abordagem incorreta e sugestão de correção.

Análise de Chamadas Recursivas

Observação da sequência de invocações em diferentes vetores de entrada.

🔍 Implementação e Testes
📌 QuickSort Recursivo
O QuickSort na forma recursiva utiliza chamadas sucessivas para ordenar subvetores menores. Embora seja intuitivo e elegante, pode sofrer com limitações em vetores grandes devido ao consumo de memória na pilha de execução.

📌 QuickSort Iterativo
A versão iterativa do algoritmo evita problemas de profundidade de recursão ao utilizar uma pilha explícita para armazenar os índices dos subvetores a serem ordenados.

Os testes foram realizados com vetores de diferentes tamanhos, e os tempos de execução foram registrados para comparação.

📊 Comparação de Tempo de Execução
Os resultados dos testes demonstram diferenças significativas no desempenho das abordagens:

Tamanho do Vetor	Tempo Recursivo (s)	Tempo Iterativo (s)
1000 elementos	X.XXX	X.XXX
5000 elementos	X.XXX	X.XXX
10000 elementos	X.XXX	X.XXX
50000 elementos	X.XXX	X.XXX
Ajuste os valores conforme seus experimentos.

🛠️ Análise de Erros e Melhorias
Problemas na Função de Separação
Uma tentativa incorreta de particionar o vetor compromete a ordenação correta. A análise revelou que a movimentação do pivô era inadequada, levando a um estado inconsistente na separação dos elementos.

Comportamento do QuickSort em Diferentes Vetores
Testes realizados com vetores pequenos mostraram problemas nas chamadas recursivas erradas, que podem causar loops desnecessários ou falhas de ordenação.

Sugestões de Correção
A implementação correta da função de separação deve garantir:

Troca adequada entre elementos menores e maiores que o pivô.

Posicionamento correto do pivô antes da recursão.

Condições de parada bem definidas para evitar recursões redundantes.

📌 Conclusão
A análise comparativa do QuickSort permitiu entender os desafios de diferentes abordagens e como pequenas mudanças na implementação podem impactar o desempenho e a correção do algoritmo. A versão iterativa pode ser mais eficiente para vetores grandes, enquanto a versão recursiva é mais intuitiva para implementações menores.
