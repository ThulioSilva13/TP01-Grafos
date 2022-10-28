import json
import sys
from Grafo import Grafo

g = Grafo()

def lerArquivo():
    nome_arquivo = sys.argv[1]
    linhas = []
    arquivo = open(nome_arquivo)
    aux = 0
    for linha in arquivo.readlines():
        if aux != 0:
            linhas.append(list(map(float,linha.replace("\n","").split(" "))))
        else:
            qntdVertices = (int(linha.replace("\n","")))           
        aux += 1
    
    return [ qntdVertices, linhas]

def escreverJson():
    arq = lerArquivo()
    with open('grafoExemplo.json', 'r') as fileJson:
        grafoJson = json.load(fileJson)
        grafoJson['data']['nodes']['length'] = arq[0]
        grafoJson['data']['edges']['length'] = len(arq[1])
        
        for i in range(arq[0]):
            vertice = {"id": int(i+1), "label": str(i+1)}
            grafoJson["data"]["nodes"]["_data"][str(i+1)] = vertice

        for i in range(len(arq[1])):
            aresta = {"from": int(arq[1][i][0]), "to": int(arq[1][i][1]), "label": str(arq[1][i][2]),"id": str(i+1),"color": {}}
            grafoJson["data"]["edges"]["_data"][str(i+1)] = aresta

    with open('grafoCriado.json', 'w') as outputFileJson:
        json.dump(grafoJson, outputFileJson, indent=4)
escreverJson()   
g.lerJson('grafoExemplo.json')


def inicializarGrafo(qntdVertices, linhas):
    g.inicializaListaAdjacencia(qntdVertices)
    for i in range(len(linhas)):
        g.insereAresta(int(linhas[i][0]), int(linhas[i][1]), float(linhas[i][2]))
    print("\nGrafo:")
    g.imprimirListaAdjacencia()
    g.floydWarshall()
    g.verificaCicloNegativo() #já conferir se tem ciclo negativo

arq = lerArquivo()
inicializarGrafo(arq[0], arq[1])

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
vizitados, retorno = g.buscaProfundidade(inicio)
print("-- Vértices vizitados na Busca em Profundidade: ",vizitados)
print("-- Arestas de Retorno: ", retorno )

print()
if (g.cicloNegativo==1):
    print("ERRO: Impossivel calcular distancia entre vertices pois grafo com Ciclo Negativo!")
    print("ERRO: Impossivel calcular caminho minimo entre vertices pois grafo com Ciclo Negativo!")
    print("ERRO: Impossivel calcular exentricidade de um vértice pois grafo com Ciclo Negativo!") 
    print("ERRO: Impossivel calcular o raio do grafo pois grafo com Ciclo Negativo!")
    print("ERRO: Impossivel calcular o diametro do grafo pois grafo com Ciclo Negativo!") 
    print("ERRO: Impossivel calcular o centro do grafo pois grafo com Ciclo Negativo!") 
    print("ERRO: Impossivel calcular centralidade de proximidade do vertice pois grafo com Ciclo Negativo!") 
    
else:
    print("\n- Distancia e Caminho Minimo: ")
    origem = 1
    for i in range (1,6):
        print()
        destino = i
        print("- Distancia entre ",origem,"e",destino,":",g.distancia(origem,destino))
        print("- Caminho minimo entre",origem,"e",destino,":",g.caminhoMinimo(origem,destino))

    for i in range (1,g.ordemGrafo()+1):
        print("- Exentricidade do Vertice",i,": ",g.exentricidadeVertice(i))
    
    print("\n- Raio do Grafo:", g.raioGrafo())
    print("\n- Diametro do Grafo:",g.diametroGrafo())
    print("\n- Centro do Grafo:",g.centroGrafo())
    
    print()
    for i in range (1,g.ordemGrafo()+1):
        print("- Centralidade de Proximidade do vértice",i,"é:",g.CentralidadeProxC(i))

