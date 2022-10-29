import math

class Grafo:
    def __init__(self):
        self.vertices = 0
        self.grafo = [[]] #lista de adjacencia 
        self.dt = [[]]  
        self.rot = [[]] 
        self.cicloNegativo = 0
        
    def inicializaListaAdjacencia(self, qtdeVertices):
        self.vertices = qtdeVertices
        self.grafo = [[] for i in range(self.vertices)]
        
    def insereAresta(self, origem, destino, peso):
        #acessar primeira posicao da lista(posicao 0), por isso origin-1
        self.grafo[origem -1].append([destino, peso])
        self.grafo[destino -1].append([origem, peso])
    
    def imprimirListaAdjacencia(self):
        for i in range(self.vertices):
            print(f"  [ {i+1} ] ->",end=" ")
            tam = len(self.grafo[i])
            for j in range (tam):
                if j == tam-1:
                    print(self.grafo[i][j])
                else:
                    print(self.grafo[i][j]," ->", end=' ')
    
    def ordemGrafo(self):
        # quantidade de vertices do grafo
        return self.vertices
        
    def tamanhoGrafo(self):
        # quantidade de arestas do grafo
        tamanho = 0
        for i in range(self.vertices):
            #for j in self.grafo[i]:
            #    tamanho+=1
            tamanho += len(self.grafo[i])
        return int(tamanho/2) #/ 2 pois como nao orientado cada aresta aparece duas vezes na lista
    
    def encontrarVizinhos(self, idVertice):
        # dois vertices são vizinhos quando existe uma aresta que os liga.
        listaVizinhos = []
        for i in range(self.vertices):
            if(i+1 == idVertice):
                for j in range(len(self.grafo[i])):
                    listaVizinhos.append(self.grafo[i][j][0])
        listaVizinhos.sort()
        return listaVizinhos
    
    def encontrarPesoVizinhos(self, idVertice):
        #funcao auxiliar para armazenar peso das arestas no mesma ordem que os vizinhos foram armazenados
        pesos = []
        for i in range(self.vertices):
            if(i+1 == idVertice):
                for j in range(len(self.grafo[i])):
                    pesos.append(self.grafo[i][j][1])
        return pesos

    def grauVertice(self, id):
        # grau de um vértice em um grafo não direcionado é o número de arestas incidentes no vértice
        return len(self.grafo[id-1])
        
    def sequenciaGrausGrafo(self):
        # sequencia de graus é uma sequência monotônica não crescente dos graus dos vértices, ou seja, é o grau dos vérticem em ordem decrescente
        sequenciaGraus = []
        for i in range(self.vertices):
            grau = self.grauVertice(i)
            sequenciaGraus.append(grau)
        sequenciaGraus.sort(reverse=True) #ordenar graus em ordem decrescente
        
        return(sequenciaGraus)
    
    def exentricidadeVertice(self, id):
        # maior distância entre ele e outro vértice do grafo
        exe = max(self.dt[id-1]) #-1 pois vertice 1 esta no indece 0 da matriz
        return(exe)
    
    def raioGrafo(self):
        # menor valor de excentricidade para to vértice pertencente ao conjunto de vértices do grafo, ou seja, calcula-se a exentricidade de todos os vértices do grafo e pega o menor valor.       
        excentricidades = []
        for i in range(self.vertices):
            excentricidades.append(self.exentricidadeVertice(i+1))
        return(min(excentricidades))
        
    def diametroGrafo(self):
        # maior valor de excentricidade para to vértice pertencente ao conjunto de vértices do grafo, ou seja, calcula-se a exentricidade de todos os vértices do grafo e pega o maior valor.    
        excentricidades = []
        for i in range(self.vertices):
            excentricidades.append(self.exentricidadeVertice(i+1))
        return(max(excentricidades))
        
    def centroGrafo(self):
        # subconjunto dos vértices de exentricidade mínima.
        centro=[]
        raio = self.raioGrafo()
        for i in range(1,self.vertices+1): #+1 pois no inde 0 esta o vertice 1
            if (self.exentricidadeVertice(i) == raio): 
                centro.append(i) #
        return(centro)

    def buscaProfundidade(self,v):
        # determinar sequencia de vertices visitados
        # informar arestas que nao fazem parte da arvore de busca em profundidade
        marcados = [] #armazenar vertices marcados
        exploradas = [] #armazenar arestas que já foram exploradas
        profundidade = []
        retorno = []
        self.procedimentoBP(v,exploradas, marcados, profundidade, retorno)

        return marcados, retorno
    
    def procedimentoBP(self,v,exploradas,marcados, profundidade, retorno):        
        if not v in marcados:
            marcados.append(v) #marcar vertice da vez
        
        vizinhos = self.encontrarVizinhos(v) #guardar vizinhos do vertice
        
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
                self.procedimentoBP(w,exploradas, marcados, profundidade, retorno)
            else:  #se vizinho ainda já foi vizitado
                if not aresta in exploradas and not aresta in retorno:
                    exploradas.append(aresta)
                    retorno.append(aresta)
    
    def distancia(self,origem,destino):
        return(self.dt[origem-1][destino-1]) #-1 pois vertice 1 esta no indice 0
    
    def caminhoMinimo(self,origem,destino):      
        caminho = []
        caminho.append(destino)
        i = self.rot[origem-1][destino-1]
        while(True):
            caminho.append(i)
            if i == origem:
                break
            else:
                i = self.rot[origem-1][i-1]
        
        caminho.reverse()
        return(caminho)
    
    def CentralidadeProxC(self, vertice):
        N = (self.vertices)
        somatorio = 0
        for i in range (N):
            somatorio += self.dt[vertice-1][i] #somar a distancia do vertice a todos os outros do grafo
        c = (N-1)/somatorio
        return(c)
       
    def floydWarshall(self):
        
        v = self.vertices
        self.dt = [[0 for i in range (self.vertices)] for j in range (v)] 
        self.rot = [[0 for i in range (self.vertices)] for j in range (v)] 
        
        '''
        como a matriz vai de 0 a v-1
        vertice 1 está no indece 0
        '''

        #inicializar matriz dt(L) e a matriz rot(R) 
        for i in range (v):
            vizinhos = self.encontrarVizinhos(i+1) 
            pesos = self.encontrarPesoVizinhos(i+1)
 
            for j in range (v):
                if i==j:
                    self.dt[i][j] = 0
                    self.rot[i][j] = i+1 #em vez do indice vai receber o indice 
                else:
                    if (j+1) in vizinhos: #j+1 pois quando j=0 quero olhar se vertice 1 é vizinho
                        self.dt[i][j] = pesos[vizinhos.index(j+1)]
                        self.rot[i][j] = i+1 #lembrar que i=0 indica vertice 1
                    else:
                        self.dt[i][j] = math.inf
                        self.rot[i][j] =  0
        '''              
        # inicialização da matrizes
        print("\n - MATRIZ DT:")
        for i in range (v):
            print("   [",end = "")
            for j in range (v):
                if j == v-1:
                    print("{:.2f}]".format(self.dt[i][j]))
                else:
                    print("{:.2f},".format(self.dt[i][j]), end = " ")
                    
        print("\n - MATRIZ ROT:")
        for i in range (v):
            print("  ",end = " ")
            print(self.rot[i])
        '''       
        #tentar caminho intermediario
        for k in range(v):
            for i in range(v):
                for j in range(v):
                    if self.dt[i][j] > (self.dt[i][k] + self.dt[k][j]):
                        self.dt[i][j] = (self.dt[i][k] + self.dt[k][j])
                        self.rot[i][j] = self.rot[k][j]
        
    def imprimirMatrizesFloydWarshall(self):
        v = self.vertices
        print("\n-- MATRIZ DT:")
        for i in range (v):
            print("   [",end = "")
            for j in range (v):
                if j == v-1:
                    print("{:.2f}]".format(self.dt[i][j]))
                else:
                    print("{:.2f},".format(self.dt[i][j]), end = " ")
                
        print("\n-- MATRIZ ROT:")
        for i in range (v):
            print("  ",end = " ")
            print(self.rot[i])

            
    def verificaCicloNegativo(self):
        self.cicloNegativo = 0
        for i in range (self.vertices):
            for j in range (self.vertices):
                if (i==j and self.dt[i][j]<0):
                    self.cicloNegativo = 1
                    break
          
    
