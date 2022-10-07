import Vertice


class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[] for i in range(self.vertices)]    

    def InsereAresta(self, origin, destiny, weight):
        #acessar primeira posicao da lista(posicao 0), por isso origin-1
        self.grafo[origin -1].append([destiny, weight])
        self.grafo[destiny -1].append([origin, weight])


    def PrintList(self):
        for i in range(self.vertices):
            print(f'{i+1}:', end='  ')
            for j in self.grafo[i]:
                print(f'{j}  ->', end='  ')
            print('')

    def EncontrarVizinhos(self, idVertice):
        listVizinhos = []
        for i in range(self.vertices):
            if(i+1 == idVertice):
                for j in range(len(self.grafo[i])):
                    listVizinhos.append(self.grafo[i][j][0])
        print(listVizinhos)