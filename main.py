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
    g.InsereAresta(int(linhas[i][0]), int(linhas[i][1]), float(linhas[i][2]))

print("\nGrafo:")
g.PrintList()
g.floydWarshall()

print("\nCaracteristicas do Grafo:")
print("- Ordem do Grafo =",g.OrdemGrafo())
print("- Tamanho do Grafo =",g.TamanhoGrafo())
for i in range (1, g.OrdemGrafo()+1):
    print("- Grau do Vertice",i,"=",g.GrauVertice(i))
for i in range (1, g.OrdemGrafo()+1):
    print("- Vizinhos do Vertice",i,"=",g.EncontrarVizinhos(i))
print("- Sequencia de Graus do Vertice =",end=' ')
g.SequenciaGrausGrafo()
print("- Busca em Profundidade:")
g.BuscaProfundidade(1)

g.CaminhoMinimo(1,1)
g.CaminhoMinimo(1,2)
g.CaminhoMinimo(1,3)
g.CaminhoMinimo(1,4)
g.CaminhoMinimo(1,5)
print("Exentricidade: ",g.ExentricidadeVertice(1))
print("Raio:", g.RaioGrafo())
print("Diametro:")
g.DiametroGrafo()
print("Cntro:")
g.CentroGrafo()

