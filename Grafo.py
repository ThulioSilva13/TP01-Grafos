import Vertice


class Grafo:
    def __init__(grafo):
        grafo.listaVertices = []
        grafo.listaArestas = []

    def InsereVertice(self, identificador):
        self.listaVertices.append(Vertice(identificador))

    def InsereAresta(self, origem, destino, peso):
        verticeOrigem = self.__getattribute__()