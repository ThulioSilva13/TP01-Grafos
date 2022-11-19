from grafo import Grafo
from aresta import Aresta

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
    
    
    # i = 0
    # arvoreGeradoraMinima.append(g.arestas[i])
    # origem = g.arestas[i].getOrigem()
    # destino = g.arestas[i].getDestino()
    # feixoTransitivoD[origem-1] += (feixoTransitivoD[destino-1])
    # feixoTransitivoD[destino-1] += (feixoTransitivoD[origem-1])
    
    i = 0
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

    
    

qntdVertices, linhas  = lerArquivo()
g = Grafo()

inicializarGrafo(qntdVertices, linhas)

for i in range(len(linhas)):
    g.insereAresta(int(linhas[i][0]), int(linhas[i][1]), float(linhas[i][2]))

print("\nGrafo:")
g.imprimirListaAdjacencia()

algoritmoKruskal()
                
            
    
    
    
    
    




