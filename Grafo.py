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

    def BuscaProfundidade(self,v):
        # determinar sequencia de vertices visitados
        # informar arestas que nao fazem parte da arvore de busca em profundidade
        marcados = [] #armazenar vertices marcados
        exploradas = [] #armazenar arestas que já foram exploradas
        profundidade = []
        retorno = []
        self.ProcedimentoBP(v,exploradas, marcados, profundidade, retorno)
        print("arvore de profundidade = ",profundidade)
        print("arestas retorno = ", retorno )
    
    def ProcedimentoBP(self,v,exploradas,marcados, profundidade, retorno):
        id_v = v-1 #como lista começa no zero, vertice 1 esta na posiçao 0 da lista
        
        if not v in marcados:
            marcados.append(v) #marcar vertice da vez
        
        vizinhos = self.EncontrarVizinhos(v) #guardar vizinhos do vertice
        
        for w in vizinhos:
            aresta = []
            aresta.append(v)
            aresta.append(w)
            aresta.sort() #como grafo nao direcioando armazenar ordenado 
            if not w in marcados: #se vizinho ainda nao foi vizitado
                exploradas.append(aresta) 
                marcados.append(w) #marcar w como já vizitado
                if not aresta in profundidade:
                    profundidade.append(aresta)
                self.ProcedimentoBP(w,exploradas, marcados, profundidade, retorno)
            else:  #se vizinho ainda já foi vizitado
                if not aresta in exploradas and not aresta in retorno:
                    exploradas.append(aresta)
                    retorno.append(aresta)
    
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
