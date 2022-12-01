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
                  
    def algoritmoKruskal(self):
    
        self.arestas.sort(key=lambda arestas: arestas.peso) #vetor com as arestas do grafo em ordem crescente de peso
        
        arvoreGeradoraMinima = []
        peso = 0
        
        feixoTransitivoD = [[] for i in range (self.vertices)] #verifica se tem ciclo
        
        # um vertice faz parte do seu proprio feixo
        for i in range (self.vertices):
            feixoTransitivoD[i].append(i+1)
        
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
    
    def vizinhos(self, idVertice):
        # dois vertices são vizinhos quando existe uma aresta que os liga.
        vizinhos = []
        for i in range(self.vertices):
            if(i+1 == idVertice):
                for j in range(len(self.grafo[i])):
                    vizinho = self.grafo[i][j][0]
                    vizinhos.append(Vertice(vizinho,self.grauVertice(vizinho)))
                    
        vizinhos.sort(key=lambda vertices: vertices.grau)
        return vizinhos
    
    def emparelhamentoMaximo(self):
        # Emparelhamento = conjunto E de arestas tal que nenhum vertice incide em mais de uma aresta
        # Emarelhamento Máximo = possui o maior número de arestas possível
        
        matching = [] # arestas emparelhadas = aresta do conjunto E
        saturados = [] # vertices saturados = vertice terminal de alguma aresta do cjto E
        
        arestas = self.arestas
                    
        # pegar os vertices do grafo e colocar em um vetor juntamente com seu grau
        vertices = []    
        for i in range (1,self.vertices+1):
            vertices.append(Vertice(i, self.grauVertice(i))) # cada vertice tem seu id e seu grau
        
        #ordenar os vertices em ordem crescente de graus
        #já que queremos o máximo de arestas podemos começar com os vertices de menor grau
        vertices.sort(key=lambda vertices: vertices.grau)
        
        # for i in range (len(vertices)):
        #     print(vertices[i].id,",",end=" ")
         
        indice_vertices = []
        for i in vertices:
            indice_vertices.append(i.id)
        
        vizinhos = []
        qtdVizinhos = []
        for i in vertices:
            vizinhos.append(self.vizinhos(i.id))
            qtdVizinhos.append(len(self.vizinhos(i.id)))
        
        
        # for i in range (len(vizinhos)):
        #     print("\nvizinhos",vertices[i].id,":",end="")
        #     for j in range (len(vizinhos[i])):
        #         print(vizinhos[i][j].id,",",end="")
        

        # Determinar um emparelhamento E = detreminar um conjunto independente de arestas
        while sum(qtdVizinhos)!=0 and len(vertices)>0: # se ainda tem vertice com vizinhos e ainda tem vertices sem ter sido olhado
            
            # for i in range (len(vertices)):
            #     print(vertices[i].id,",",end=" ")
            
            # print("\nqtd vizinhos = ", qtdVizinhos)
                
            o = vertices.pop(0) #pega o vertice com menor grau
            indice_o = indice_vertices.index(o.id)
            # print("\nvizinhos do",o.id,":",end=" ")
            # for i in range (len(vizinhos[indice_o])):
            #     print(vizinhos[indice_o][i].id,",",end=" ")
            
            if qtdVizinhos[indice_o]!=0 and o.id not in saturados: #se esse vertice tiver vizinhos que nao estao no matching
        
                while((qtdVizinhos[indice_o])>0):
                    if ((len(vizinhos[indice_o]))==0):
                        break
                    d = vizinhos[indice_o].pop(0) #pega o vizinho de menor grau
                    #print("vizinho da vez:",d.id)
                    indice_d = indice_vertices.index(d.id)
                    if d.id in vertices: #se o vertice vizinho estiver disponivel ele é o escolhido
                        break
                
                if qtdVizinhos[indice_d]==0:
                    break
                
                else:
                    #pegar a aresta entre o vertice de menor garu disponivel e seu vizinho de menor grau disponivel
                    for a in arestas:
                        if ((a.origem == o.id and a.destino == d.id) or (a.origem == d.id and a.destino == o.id)):
                            #print('\n',a.origem,'->',a.destino)
                            matching.append(a)             
                    
                    #remover o vertice destino dos verices disponiveis
                    for i in vertices:
                        if (i.id == d.id):
                            vertices.remove(i)
                    
                    #pegar os vertices de origem e de destino
                    saturados.append(o.id)
                    saturados.append(d.id)
                    
                    qtdVizinhos[indice_o] = 0
                    qtdVizinhos[indice_vertices.index(d.id)] = 0
        
        
        #Encontrar um caminho aumentante P em G em relação a E
        # ideia, conferir se a origem e o destino de uma aresta emparelhada tem vizinhos que não são saturados
        # se tiver, inverter:
        
        vizinhos = []
        for i in saturados:
            vizinhos.append(self.vizinhos(i))
        
        indice_saturados = []
        for i in saturados:
            indice_saturados.append(i)

 
        for i in range(len(matching)): #para cada aresta
            # print("\nprocura caminho aumentante")
            # print("\nSaturados:",saturado)
            a = matching[i] #pega a aresta da vez
            indice_origem = indice_saturados.index(a.origem)
            indice_destino = indice_saturados.index(a.destino)
            # print(a.origem,"[",indice_origem,"]->", a.destino,"[",indice_destino,"]")
            
            # print("len",len(vizinhos[indice_origem]))
            # print("\nvizinhos",a.origem,"[",indice_origem,"]:",end="")
            # for i in range (len(vizinhos[indice_origem])):
            #     print(vizinhos[indice_origem][i].id,",",end="")
                
            o_vizinhos_nao = None
            for i in vizinhos[indice_origem]:
                if i.id not in saturados:
                    o_vizinhos_nao = i.id
                    break
            
            # print("\nvizinhos",a.destino,":",end="")
            # for j in range (len(vizinhos[indice_destino])):
            #     print(vizinhos[indice_destino][j].id,",",end="")
                
            d_vizinhos_nao = None
            for i in vizinhos[indice_destino]:
                if i.id not in saturados:
                    d_vizinhos_nao = i.id
                    break
            
            # se tem caminho aumentante
            if (o_vizinhos_nao != None and d_vizinhos_nao != None):
                
                #novas arestas
                for a in arestas:
                    #nova aresta: o -> o_vizinhos_nao
                    if ((a.origem == o.id and a.destino == o_vizinhos_nao) or (a.origem == o_vizinhos_nao and a.destino == o.id)):
                            #print('\nadiciona:',a.origem,'->',a.destino)
                            matching.append(a) 
                            saturados.append(o_vizinhos_nao)
                            saturados.append(d_vizinhos_nao)
                            
                    #nova aresta: d -> d_vizinhos_n
                    if ((a.origem == o.id and a.destino == d_vizinhos_nao) or (a.origem == d_vizinhos_nao and a.destino == o.id)):
                            #print('\nadiciona: ',a.origem,'->',a.destino)
                            matching.append(a)
                            saturados.append(o_vizinhos_nao)
                            saturados.append(d_vizinhos_nao)  
                    
                #revome: o->d
                for a in matching:
                    if ((a.origem == o.id and a.destino == d.id) or (a.origem == d.id and a.destino == o.id)):
                            #print('\nremove: ',a.origem,'->',a.destino)
                            matching.remove(a)
                            
        return matching       
             
        # ALGORITMO DE EDMONDS

        # - caminho alternante = caminho cujas arestas são alternadamente emparelhadas e nao emparelhadas
        # - caminho aumentante = caminho alternate em que o vertice inicial e o final sao nao saturados
        #
        # 1) Ler G = (N,M)
        # 2) Determinar um emparelhamento E //detreminar um conjunto independente de arestas
        # 3) Encontrar um caminho aumentante P em G em relação a E
        # 4) Se um caminho aumentante P foi encontrado Então
        #    4.1) Para cada aresta a de P    //invreter arestas emparlhadas e não emparelhadas
        #         Se a pertence a E Então
        #             Retirar a de E.
        #         Se a nao pertence a E Então
        #             Acrescentar a em E.
        #   4.2) Voltar ao passo 3.
        # 5) Senão
        #   5.1) Emparelhamento máximo encontrado, fim.
    
            
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
        
