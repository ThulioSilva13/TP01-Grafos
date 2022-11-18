# Biblioteca para manipular grafos

**Trabalho Prático da disciplina de Teoria e Modelo de Grafos** 

 O trabalho consiste na implementação de uma biblioteca para manipular grafos não direcionados ponderados. 

 Os grafos são representados utilizando lista de adjacência. E a biblioteca conta com funções para:

* Retornar a ordem do grafo
> A ordem de um grafo é a cardinalidade (quantidade de elementos) de seu conjunto de vértices.

* Retornar o tamanho do grafo
> O tamanho de um grafo é a cardinalidade (quantidade de elementos) de seu conjunto de arestas.

* Retornar os vizinhos de um vértice fornecido
> Dois vertices i e j são vizinhos quando existe uma aresta que liga i a j ou vice-versa.

* Determinar o grau de um vértice fornecido
> O grau de um vértice em um grafo não direcionado é igual ao número de arestas incidentes no vértice.

* Retornar a sequência de graus do grafo
> A sequencia de graus é uma sequência monotônica não crescente dos graus dos vértices, ou seja, é o grau dos vértices em ordem decrescente.

* Determinar a excentricidade de um vértice
> A excenticidade de um vértice é a maior distância entre ele e outro vértice do grafo. (E a distancia entre um par de vértices corresponde ao caminho(passeio sem repetição de vértices) de menor comprimento capaz de ligá-los).

* Determinar o raio do grafo
> Raio de um grafo é o menor valor de excentricidade para todo vértice pertencente ao conjunto de vértices do grafo, ou seja, calcula-se a exentricidade de todos os vértices do grafo e pega o menor valor.

* Determinar o diâmetro do grafo
> Diâmetro de um grafo é o maior valor de excentricidade para todo vértice pertencente ao conjunto de vértices do grafo, ou seja, calcula-se a exentricidade de todos os vértices do grafo e pega o maior valor.

* Determinar o centro do grafo
> O centro de um grafo é o subconjunto dos vértices de exentricidade mínima.

* Determinar a sequência de vértices visitados na busca em profundidade e
informar a(s) aresta(s) que não faz(em) parte da árvore de busca em profundidade.

* Determinar distância e caminho mínimo

* Determinar a centralidade de proximidade C de um vértice x

### Funções adicionais 
* Verificar se um grafo possui ciclo

* Determinar a árvore geradora mínima e escreve-lâ em um arquivo juntamente com seu peso

* Determinar uma cobertura mínima de vértices de um grafo por meio de uma heurística

* Determinar o emparelhamento máximo de um grafo

## Autores

* **Emily Lopes** - [Emily-Lopes](https://github.com/Emily-Lopes)
* **Letícia Silva** - [lleticiasilvaa](https://github.com/lleticiasilvaa)
* **Tassia** - [tatamartinsg](https://github.com/tatamartinsg)
* **Thulio Silva** - [ThulioSilva13](https://github.com/ThulioSilva13)
