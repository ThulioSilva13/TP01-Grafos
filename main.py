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
print("- Ordem do Grafo =",g.OrdemGrafo())
print("- Tamanho do Grafo =",g.TamanhoGrafo())
for i in range (1, g.OrdemGrafo()+1):
    print("- Grau do Vertice",i,"=",g.GrauVertice(i))
for i in range (1, g.OrdemGrafo()+1):
    print("- Vizinhos do Vertice",i,"=",g.EncontrarVizinhos(i))
print("- Sequencia de Graus do Vertice =",end=' ')
g.SequenciaGrausGrafo()