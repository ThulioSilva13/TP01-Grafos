import Vertice

class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[] for i in range(self.vertices)] #lista de adjacencia    

    def InsereAresta(self, origin, destiny, weight):
        #acessar primeira posicao da lista(posicao 0), por isso origin-1
        self.grafo[origin -1].append([destiny, weight])
        self.grafo[destiny -1].append([origin, weight])
    
    def OrdemGrafo(self):
        # quantidade de vertices do grafo
        return self.vertices
        
    def TamanhoGrafo(self):
        # quantidade de arestas do grafo
        tamanho = 0
        for i in range(self.vertices):
            for j in self.grafo[i]:
                tamanho+=1
        return int(tamanho/2)
    
    #def VizinhosVertice(self, id):
        # dois vertices são vizinhos quando existe uma aresta que liga.

    def GrauVertice(self, id):
        grau = 0
        for i in self.grafo[id-1]:
            grau+=1
        return grau
        
    def SequenciaGrausGrafo(self):
        seqGraus =[]
        for i in range(self.vertices):
            grau = self.GrauVertice(i)
            seqGraus.append(grau)
        seqGraus.sort(reverse=True) #ordenar graus em ordem decrescente
        
        print(seqGraus)
    
    #def ExentricidadeVertice(self, id):
        # maior distância entre ele e outro vértice do grafo
    
    #def RaioVertice(self,id):
        # menor valor de excentricidade para to vértice pertencente ao conjunto de vértices do grafo, ou seja, calcula-se a exentricidade de todos os vértices do grafo e pega o menor valor.       

    #def DiametroVertice(self,id):
        # maior valor de excentricidade para to vértice pertencente ao conjunto de vértices do grafo, ou seja, calcula-se a exentricidade de todos os vértices do grafo e pega o maior valor.    

    #def CentroGrafo(self)
        # subconjunto dos vértices de exentricidade mínima.

    #def BuscaProfundidade(self)
        # determinar sequencia de vertices visitados
        # informar arestas que nao fazem parte da arvore de busca em profundidade

    #def DistCaminhoMinimo(self)
    
    #def CentralidadeProxC(self)
    
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
        listVizinhos.sort()
        return listVizinhos
