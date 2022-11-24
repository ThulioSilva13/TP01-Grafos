import math
import json

class Vertice:
    def __init__(self, id, grau):
        self.id = id
        self.grau = grau

class Aresta:
    def __init__(self, origem, destino,peso):
        self.origem = origem
        self.destino = destino
        self.peso = peso
        
class Grafo:
    def __init__(self):
        self.vertices = 0
        self.arestas = []
        self.grafo = [[]] #lista de adjacencia 
        self.dt = [[]]  
        self.rot = [[]] 
        self.temCiclo = None
        self.cicloNegativo = 0
        
    def inicializar(self, qtdeVertices, linhas):
        self.vertices = qtdeVertices
        self.grafo = [[] for i in range(self.vertices)]
        for i in range(len(linhas)):
            self.insereAresta(int(linhas[i][0]), int(linhas[i][1]), float(linhas[i][2]))
            self.arestas.append(Aresta(int(linhas[i][0]), int(linhas[i][1]), float(linhas[i][2])))
        
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
            tamanho += len(self.grafo[i])
        return int(tamanho/2) #/ 2 pois como nao orientado cada aresta aparece duas vezes na lista
    
    def encontrarVizinhos(self, idVertice):
        # dois vertices são vizinhos quando existe uma aresta que os liga.
        listaVizinhos = []
        for i in range(self.vertices):
            if(i+1 == idVertice):
                for j in range(len(self.grafo[i])):
                    listaVizinhos.append(self.grafo[i][j][0])
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
        
        if (len(retorno)==0): #se nao tem aresta de retorno
            self.temCiclo = False
        else:
            self.temCiclo = True
            
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
    
    def centralidadeProximidade(self, vertice):
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
                
    def verificarCiclos(self):
        if (self.temCiclo == None):
            self.buscaProfundidade(1)
        
        return self.temCiclo
                
    # def verificarCiclos(self, vertice):
    #     verticesVisitados = set()
    #     verticesRestantes = [vertice]

    #     while verticesRestantes:
    #         verticeAtual = verticesRestantes.pop()
    #         verticesVisitados.add(verticeAtual)

    #         for vizinho in self.encontrarVizinhos(verticeAtual):
    #             if vizinho in verticesVisitados:
    #                 return True

    #             verticesRestantes.append(vizinho)

    #     return False  
    
    def algoritmoKruskal(self):
    
        self.arestas.sort(key=lambda arestas: arestas.peso) #vetor com as arestas do grafo em ordem crescente de peso
        
        arvoreGeradoraMinima = []
        peso = 0
        
        feixoTransitivoD = [[] for i in range (self.vertices)] #verifica se tem ciclo
        
        # um vertice faz parte do seu proprio feixo
        for i in range (self.vertices):
            feixoTransitivoD[i].append(i+1)
        
        
        # i = 0
        # arvoreGeradoraMinima.append(self.arestas[i])
        # origem = self.arestas[i].getOrigem()
        # destino = self.arestas[i].getDestino()
        # feixoTransitivoD[origem-1] += (feixoTransitivoD[destino-1])
        # feixoTransitivoD[destino-1] += (feixoTransitivoD[origem-1])
        
        i = 0
        while (True):
            
            # encerra quando qtd arestas da arvore gerador minima = |N|-1
            if (len(arvoreGeradoraMinima) == self.vertices - 1):
                break

            origem = self.arestas[i].origem
            destino = self.arestas[i].destino
            
            '''
            
            se o vertice de destino faz parte do feixo tarnsitivo direto do vertice de origem
            OU
            se o vertice de origem faz parte do feixo transitivo direto do vertice de destino
            entao a aresta (origem,destino) forma um ciclo no grafo
            
            entao para conferir se NÂO forma ciclo
            o vertice de origem não pode fazer parte do feixo transitivo direto do vertice de destino
            E
            o vertice de destino não pode estar parte do  feixo transitico direto do vertice de origem
            
            '''

            if ((origem not in feixoTransitivoD[destino-1]) 
                and (destino not in feixoTransitivoD[origem-1])): #conferi se nao forma ciclo
                
                arvoreGeradoraMinima.append(self.arestas[i])
                peso += self.arestas[i].peso
                feixoTransitivoD[origem-1] += (feixoTransitivoD[destino-1])
                feixoTransitivoD[destino-1] += feixoTransitivoD[origem-1]
                
            i += 1 # olha pra proxima aresta
        
        return [arvoreGeradoraMinima, peso]   
    
    def coberturaVertices(self):
        
        cobertura = []
        numCobertura = 0
        
        vertices = []    
        for i in range (1,self.vertices+1):
            vertices.append(Vertice(i, self.grauVertice(i)))
        
        #ordenar os vertices em ordem decrescente de graus
        
        vertices.sort(key=lambda vertices: vertices.grau, reverse=True)
        # for i in vertices:
        #      print(i.id,"=",i.grau)
        
        # print("vertices = ",end=" ")
        # for i in vertices:
        #     print(i.id,end=" ")
        
        arestas = self.arestas
        
        while len(arestas)>0:
            #print("\narestas = ",len(arestas))
            K = vertices.pop(0) #retira vertice com maior grau 
            cobertura.append(K.id) #e coloca no conjunto do vertices da cobertura
            #print("cobertura =",cobertura)
            
            vizinhosK = self.encontrarVizinhos(K.id)
            #print("vizinhos =",vizinhosK)
            
            # remove as arestas adjacentes ao vertice K
            for v in vizinhosK:
                for a in arestas:
                    if (a.origem == K.id and a.destino == v):
                        #print(a.origem,"->",a.destino)
                        arestas.remove(a)
                    if (a.destino == K.id and a.origem == v):
                        #print(a.origem,"->",a.destino)
                        arestas.remove(a)
            
            numCobertura += 1
        
        return cobertura  
            
    def lerJson(self, nomeArquivo):
        with open(nomeArquivo, 'r') as fileJson:
            grafoJson = json.load(fileJson)

        arquivo = open(nomeArquivo.replace("json", "txt"), 'w')
        quantidadeVertices = grafoJson['data']['nodes']['length']

        arquivo.write(str(quantidadeVertices))


        grafoJson['data']['nodes']['length'] = quantidadeVertices
        origem = grafoJson['data']['edges']['_data']
        path = grafoJson['data']['edges']['_data']
        for i in range(1,grafoJson['data']['edges']['length']+1):
            origem = path[str(i)]['from']
            destino = path[str(i)]['to']
            label = path[str(i)]['label']
            arquivo.write("\n"+str(origem)+" "+str(destino)+" "+ label)
        
