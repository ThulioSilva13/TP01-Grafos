from grafo import Grafo
from grafo import Vertice
from grafo import Aresta


import sys

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

def inicializarGrafo(qntdVertices, linhas):
    g.inicializar(qntdVertices, linhas)
    g.floydWarshall()
    g.verificaCicloNegativo() #já conferi se é ciclo negativo

def algoritmoKruskal():
    
    g.arestas.sort(key=lambda arestas: arestas.peso) #vetor com as arestas do grafo em ordem crescente de peso
    
    arvoreGeradoraMinima = []
    peso = 0
     
    feixoTransitivoD = [[] for i in range (g.vertices)] #verifica se tem ciclo
    
    # um vertice faz parte do seu proprio feixo
    for i in range (g.vertices):
        feixoTransitivoD[i].append(i+1)
    
    
    i = 0
    arvoreGeradoraMinima.append(g.arestas[i])
    origem = g.arestas[i].getOrigem()
    destino = g.arestas[i].getDestino()
    feixoTransitivoD[origem-1] += (feixoTransitivoD[destino-1])
    feixoTransitivoD[destino-1] += (feixoTransitivoD[origem-1])
    
    i = 1
    while (True):
        
        # encerra quando qtd arestas da arvore gerador minima = |N|-1
        if (len(arvoreGeradoraMinima) == g.vertices - 1):
            break

        origem = g.arestas[i].origem
        destino = g.arestas[i].destino
        
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
            
            arvoreGeradoraMinima.append(g.arestas[i])
            peso += g.arestas[i].peso
            feixoTransitivoD[origem-1] += (feixoTransitivoD[destino-1])
            feixoTransitivoD[destino-1] += feixoTransitivoD[origem-1]
            
        i += 1 # olha pra proxima aresta
    
    print("\nArvore Geradora Mínima (Peso = ",peso,")")
    for i in arvoreGeradoraMinima:
        print (i.origem,"->",i.destino)

def coberturaVertices():
    
    print("\nCobertura Vértices")
    
    cobertura = []
    numCobertura = 0
    
    vertices = []    
    for i in range (1,g.vertices+1):
        vertices.append(Vertice(i, g.grauVertice(i)))
    
    #ordenar os vertices em ordem decrescente de graus
    
    vertices.sort(key=lambda vertices: vertices.grau, reverse=True)
    # for i in vertices:
    #      print(i.id,"=",i.grau)
    
    # print("vertices = ",end=" ")
    # for i in vertices:
    #     print(i.id,end=" ")
    
    arestas = g.arestas
    
    while len(arestas)>0:
        #print("\narestas = ",len(arestas))
        K = vertices.pop(0) #retira vertice com maior grau 
        cobertura.append(K.id) #e coloca no conjunto do vertices da cobertura
        #print("cobertura =",cobertura)
        
        vizinhosK = g.encontrarVizinhos(K.id)
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
    
    print(cobertura)
    print(numCobertura)

def escreverArvoreGeradoraMinima(arvoreGeradoraMinima, peso):
    nome = "profundidade.txt"
    nome = nome.replace(".txt", "_AGMin.txt")
    arquivo = open(nome,'w')
    # em uma arvore geradora minima |M| = |N|-1 => |N| = |M|+1
    N = len(arvoreGeradoraMinima)+1
    arquivo.write(str(N))
    for i in arvoreGeradoraMinima:
        arquivo.write('\n'+str(i.origem)+' '+str(i.destino)+' '+str(i.peso))
    arquivo.close()
            
    
qntdVertices, linhas  = lerArquivo()
g = Grafo()

inicializarGrafo(qntdVertices, linhas)

print("\nGrafo:")
g.imprimirListaAdjacencia()

arvoreGeradoraMinima, peso = g.algoritmoKruskal()

for i in arvoreGeradoraMinima:
    print(" ",i.origem,"->",i.destino)

print("\n-- PESO TOTAL =",peso)

#ecrever arvore geradora minima em um arquivo (no mesmo formato de entrada)
escreverArvoreGeradoraMinima(arvoreGeradoraMinima, peso)
                
            
    
    
    
    
    




