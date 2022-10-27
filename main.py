import json
import sys
from Grafo import Grafo

# with open('grafoConvertido.json', 'r') as fileJson:
#     data = json.load(fileJson)

def lerArquivo():
    nome_arquivo = sys.argv[1]
    linhas = []
    #nome_arquivo = "Grafo.txt"
    arquivo = open(nome_arquivo)
    aux = 0
    for linha in arquivo.readlines():
        if aux != 0:
            linhas.append(list(map(float,linha.replace("\n","").split(" "))))
        else:
            qntdVertices = (int(linha.replace("\n","")))           
        aux += 1
    return [ qntdVertices, linhas]

qntdVertices, linhas  = lerArquivo()

g = Grafo(qntdVertices)

for i in range(len(linhas)):
    g.insereAresta(int(linhas[i][0]), int(linhas[i][1]), float(linhas[i][2]))

print("\nGrafo:")
g.imprimirListaAdjacencia()
g.floydWarshall()
g.verificaCicloNegativo() #já conferir se tem ciclo negativo

print("-------------------------------------------------------------------------")
print("\nCaracteristicas do Grafo:")

print("\n- Ordem do Grafo: ",g.ordemGrafo())

print("\n- Tamanho do Grafo: ",g.tamanhoGrafo())

print()
for i in range (1, g.ordemGrafo()+1):
    print("- Vizinhos do Vertice",i,": ",g.encontrarVizinhos(i))

print()
for i in range (1, g.ordemGrafo()+1):
    print("- Grau do Vertice",i,": ",g.grauVertice(i))
    
print("\n- Sequencia de Graus do Vertice : ",g.sequenciaGrausGrafo())

print("\n- Busca em Profundidade: ")
inicio = 1
profundidade, retorno = g.buscaProfundidade(inicio)
print("-- Arvore de Profundidade: ",profundidade)
print("-- Arestas de Retorno: ", retorno )

print()
if (g.cicloNegativo==1):
    print("ERRO: Impossivel calcular distancia entre vertices pois grafo com Ciclo Negativo!")
    print("ERRO: Impossivel calcular caminho minimo entre vertices pois grafo com Ciclo Negativo!")
    print("ERRO: Impossivel calcular exentricidade de um vértice pois grafo com Ciclo Negativo!") 
    print("ERRO: Impossivel calcular o raio do grafo pois grafo com Ciclo Negativo!")
    print("ERRO: Impossivel calcular o diametro do grafo pois grafo com Ciclo Negativo!") 
    print("ERRO: Impossivel calcular o centro do grafo pois grafo com Ciclo Negativo!") 
    
else:
    print("\n- Distancia e Caminho Minimo: ")
    origem = 1
    for i in range (1,6):
        print()
        destino = i
        print("- Distancia entre ",origem,"e",destino,":",g.distancia(origem,destino))
        print("- Caminho minimo entre",origem,"e",destino,":",g.caminhoMinimo(origem,destino))

    for i in range (g.ordemGrafo()):
        print("- Exentricidade do Vertice",i,": ",g.exentricidadeVertice(i+1))
    
    print("\n- Raio do Grafo:", g.raioGrafo())
    print("\n- Diametro do Grafo:",g.diametroGrafo())
    print("\n- Centro do Grafo:",g.centroGrafo())

