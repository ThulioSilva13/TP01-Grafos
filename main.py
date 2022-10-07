import json
from Grafo import Grafo

with open('grafoConvertido.json', 'r') as fileJson:
    data = json.load(fileJson)

g = Grafo(5) 
g.InsereAresta(1, 2, 1.2)
g.InsereAresta(1, 5, 0.1)
g.InsereAresta(2, 5, 2.3)
g.InsereAresta(3, 5, -8.4)
g.InsereAresta(3, 4, 0.3)
g.InsereAresta(4, 5, 4.6)

print("\nGrafo:")
g.PrintList()

print("\nCaracteristicas do Grafo:")
print("- Ordem do Grafo = ",g.OrdemGrafo())
print("- Tamanho do Grafo = ",g.TamanhoGrafo())
print("- Grau do Vertice 1 = ",g.GrauVertice(1))
print("- Grau do Vertice 2 = ",g.GrauVertice(2))
print("- Grau do Vertice 3 = ",g.GrauVertice(3))
print("- Grau do Vertice 4 = ",g.GrauVertice(4))
print("- Grau do Vertice 5 = ",g.GrauVertice(5))
print("- Vizinhos do Vertice 1 = ",g.EncontrarVizinhos(1))
print("- Vizinhos do Vertice 2 = ",g.EncontrarVizinhos(2))
print("- Vizinhos do Vertice 3 = ",g.EncontrarVizinhos(3))
print("- Vizinhos do Vertice 4 = ",g.EncontrarVizinhos(4))
print("- Vizinhos do Vertice 5 = ",g.EncontrarVizinhos(5))
print("- Sequencia de Graus do Vertice = [",end=' ')
g.SequenciaGrausGrafo()