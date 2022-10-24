import json
import sys
from Grafo import Grafo

# with open('grafoConvertido.json', 'r') as fileJson:
#     data = json.load(fileJson)

g = Grafo()
   
def escolherArquivo():
    print("-------------------------------------------------------------------------")
    print("ESCOLHER ARQUIVO")
    print("-------------------------------------------------------------------------")
    print("[ 1 ] .json")
    print("[ 2 ] .txt")
    print("-------------------------------------------------------------------------")
    print("Entre com o número referente ao formato do arquivo de entrada:", end = " ")
    formato = int(input())
    if (formato==1 or formato==2):
        nomeArquivo(formato)
    else:
        print("Erro: FORMATO INVÁLIDO!")
        escolherArquivo()

def nomeArquivo(formato):
    if formato == 1:
        print("Entre com o nome do arquivo .json:", end = " ")
        nomeArquivo = input()
        lerJson(nomeArquivo)
        nomeArquivo = nomeArquivo.replace("json","txt") #funcao lerJson vai gerar o arquivo txt de mesmo nome
    else: #se nao é 1 é 2
        print("Entre com o nome do arquivo .txt:", end = " ")
        nomeArquivo = input()
    
    lerTxt(nomeArquivo)


def lerJson(nomeArquivo):
    print("implementar função que lê arquivo .json e gera arquivo .txt")

def gerarJson():
    print("!!! implementar função que gera arquivo .json !!!")

def lerTxt(nome_arquivo):
    #nome_arquivo = sys.argv[1]
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
    
    inicializarGrafo(qntdVertices, linhas)

def inicializarGrafo(qntdVertices, linhas):
    g.inicializaListaAdjacencia(qntdVertices)
    for i in range(len(linhas)):
        g.insereAresta(int(linhas[i][0]), int(linhas[i][1]), float(linhas[i][2]))

    print("\nGrafo:")
    g.imprimirListaAdjacencia()
    g.floydWarshall()

def menuFuncoes():
    while True:
        print("-------------------------------------------------------------------------")
        print("FUNÇÕES DA BIBLIOTECA")
        print("-------------------------------------------------------------------------")
        print("[  1 ] | ORDEM DO GRAFO")
        print("[  2 ] | TAMANHO DO GRAFO")
        print("[  3 ] | VIZINHOS DE UM VÉRTICE")
        print("[  4 ] | GRAU DE UM VÉRTICE")
        print("[  5 ] | SEQUÊNCIA DE GRAUS DO GRAFO")
        print("[  6 ] | EXCENTRICIDADE DE UM VÉRTICE")
        print("[  7 ] | RAIO DO GRAFO")
        print("[  8 ] | DIÂMETRO DO GRAFO")
        print("[  9 ] | CENTRO DO GRAFO")
        print("[ 10 ] | VÉRTICES VIZITADOS NA BUSCA EM PROFUNDIDADE E ARESTAS DE RETORNO")
        print("[ 11 ] | DISTANCIA E CAMINHO MÍNIMO")
        print("[ 12 ] | CENTRALIDADE DE PROXIMIDADE C DE UM VÉTICE X")
        print("[ 13 ] | ENCERRAR")
        print("-------------------------------------------------------------------------")
        print("Entre com sua escolha:", end = " ")
        escolha = int(input())
        
        #conferir se grafo foi inicializado
        
        if g == None: 
            print("Erro: PRIMEIRO ESCOLHA O ARQUIVO")
         
        elif escolha == 1:
            print("\n- Ordem do Grafo: ",g.ordemGrafo())
      
        elif escolha == 2:
            print("\n- Tamanho do Grafo: ",g.tamanhoGrafo())
     
        elif escolha == 3:
            print("\nEntre com o vértice que deseja saber seus vizinhos: ", end = " ")
            v = int(input())
            print("\n- Vizinhos do Vertice",v,": ",g.encontrarVizinhos(v))
            
              
        elif escolha == 4:
            print("\nEntre com o vértice que deseja saber o grau: ", end = " ")
            v = int(input())
            print("\n- Grau do Vertice",v,": ",g.grauVertice(v))
              
        elif escolha == 5:
            print("\n- Sequencia de Graus do Grafo: ",g.sequenciaGrausGrafo())
             
        elif escolha == 6:
            print("\nEntre com o vértice que deseja saber sua excentricidade: ", end = " ")
            v = int(input())
            print("- Exentricidade do Vertice",v,": ",g.exentricidadeVertice(v))         
        
        elif escolha == 7:
            print("\n- Raio do Grafo:", g.raioGrafo())

        elif escolha == 8:
           print("\n- Diametro do Grafo:",g.diametroGrafo())


        elif escolha == 9:
            print("\n- Centro do Grafo:",g.centroGrafo())
            
        elif escolha == 10:
            print("\nEntre com o vértice que deseja começar a busca em profundidade: ", end = " ")
            v = int(input())
            # corrigir para vertices vizitados e nao arestas de profundidade
            profundidade, retorno = g.buscaProfundidade(v)
            print("- Vértices vizitados na Busca em Profundidade: ",profundidade)
            print("- Arestas de Retorno: ", retorno )
        
        elif escolha == 11:
            flag = g.verificaCicloNegativo()
            if (flag==1):
                print("ERRO: Impossivel calcular distancia e caminho mínimo entre vertices pois grafo com Ciclo Negativo!")  
            else:
                print("\nEntre com o vértice de origem: ", end = " ")
                origem = int(input())
                print("\nEntre com o vértice de destino: ", end = " ")
                destino = int(input())
                #conferir se vertices existem no grafico
                print("- Distancia entre ",origem,"e",destino,":",g.distancia(origem,destino))
                print("- Caminho minimo entre",origem,"e",destino,":",g.caminhoMinimo(origem,destino))

        elif escolha == 12:
            print("!!! implementar funcao para calcular !!!")
        
        elif escolha == 13:
            break
            
        else:
            print("Erro: ESCOLHA INVÁLIDA")
    
    
while True:
    print("-------------------------------------------------------------------------")
    print("MENU")
    print("-------------------------------------------------------------------------")
    print("[ 1 ] | ESCOLHER ARQUIVO")
    print("[ 2 ] | USAR FUNÇÕES DA BIBLIOTECA")
    print("[ 3 ] | GERAR ARQUIVO .json")
    print("[ 4 ] | ENCERRAR")
    print("-------------------------------------------------------------------------")
    print("Entre com sua escolha:", end = " ")
    escolha = int(input())
    
    if escolha == 1:
        escolherArquivo()
        
    elif escolha == 2:
        if g == None: 
            print("Erro: PRIMEIRO ESCOLHA O ARQUIVO")
        else:
            menuFuncoes()
        
    elif escolha == 3:
        if g == None: 
            print("Erro: PRIMEIRO ESCOLHA O ARQUIVO")
        else:
            gerarJson()
    
    elif escolha == 4:
        break
    
    else:
        print("Erro: ESCOLHA INVÁLIDA!")








