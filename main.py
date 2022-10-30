from grafo import Grafo
from arquivo import Arquivo

import os.path

g = Grafo()
a = Arquivo()
  
def escolherArquivo():
    print("-------------------------------------------------------------------------")
    print("ESCOLHER ARQUIVO")
    print("-------------------------------------------------------------------------")
    print("[ 1 ] | FORMATO .json")
    print("[ 2 ] | FORMATO .txt")
    print("\n[ 3 ] | VOLTAR MENU")
    print("-------------------------------------------------------------------------")
    print("Entre com sua escolha:", end = " ")
    formato = input()
    if (formato=='1' or formato=='2'):
        receberArquivo(int(formato))
    elif (formato=='3'):
        return
    else:
        print("Erro: ESCOLHA INVÁLIDA!")
        escolherArquivo()

def receberArquivo(formato):
    flag = 1
    
    if flag == 1:

        if formato == 1:
            print("Entre com o nome do arquivo com a extensão .json:", end = " ")
            nomeArquivo = input()
            if ".json" not in nomeArquivo:
                print("Erro: NOME SEM EXTENSÃO .JSON")
                escolherArquivo()
            else:
                if(os.path.isfile(nomeArquivo)): #coneferir se existe o aquivo
                    a.lerJson(nomeArquivo)
                    a.nome = nomeArquivo.replace("json","txt") #funcao lerJson vai gerar o arquivo txt de mesmo nome
                    flag = 0
                else:
                    print("Erro: ARQUIVO NÃO ENCONTRADO")
                    escolherArquivo()
            
        else: #se nao é 1 é 2
            print("Entre com o nome do arquivo com a extensão .txt:", end = " ")
            nomeArquivo = input()
            if ".txt" not in nomeArquivo:
                print("Erro: NOME SEM EXTENSÃO .TXT")
                escolherArquivo()
            else:
                if(os.path.isfile(nomeArquivo)): #coneferir se existe o aquivo 
                    a.nome = nomeArquivo
                    flag = 0
                else:
                    print("Erro: ARQUIVO NÃO ENCONTRADO")
                    escolherArquivo()
    
    if flag==0:
        #ler arquivo txt
        arq = a.lerTxt()
        #inicializar grafo com informações lidas do arquivo txt
        inicializarGrafo(arq[0], arq[1])

def inicializarGrafo(qntdVertices, linhas):
    g.inicializar(qntdVertices, linhas)
    g.floydWarshall()
    g.verificaCicloNegativo() #já conferi se é ciclo negativo

def menuFuncoes():
    while True:
        print("\n-------------------------------------------------------------------------")
        print("FUNÇÕES DA BIBLIOTECA")
        print("-------------------------------------------------------------------------")
        print("[  1 ] | ORDEM DO GRAFO")
        print("[  2 ] | TAMANHO DO GRAFO")
        print("[  3 ] | VIZINHOS DE UM VERTICE")
        print("[  4 ] | GRAU DE UM VÉRTICE")
        print("[  5 ] | SEQUENCIA DE GRAUS DO GRAFO")
        print("[  6 ] | EXCENTRICIDADE DE UM VERTICE")
        print("[  7 ] | RAIO DO GRAFO")
        print("[  8 ] | DIAMETRO DO GRAFO")
        print("[  9 ] | CENTRO DO GRAFO")
        print("[ 10 ] | BUSCA EM PROFUNDIDADE")
        print("[ 11 ] | DISTANCIA E CAMINHO MINIMO")
        print("[ 12 ] | CENTRALIDADE DE PROXIMIDADE C DE UM VERTICE X")
        print("[ 13 ] | REPRESENTAÇAO DO GRAFO EM LISTA DE ADJACENCIA")
        print("[ 14 ] | MATRIZES RESULTANTES FLOYD-WARSHALL")
        print("[ 15 ] | USAR TODAS AS FUNÇOES")
        print("\n[ 16 ] | VOLTAR PRO MENU")
        print("-------------------------------------------------------------------------")
        print("Entre com sua escolha:", end = " ")
        escolha = input()
        
        if escolha == '1':
            print("\n- ORDEM DO GRAFO:",g.ordemGrafo())
      
        elif escolha == '2':
            print("\n- TAMANHO DO GRAFO:",g.tamanhoGrafo())
     
        elif escolha == '3':
            print("Entre com o vertice que deseja saber seus vizinhos:", end = " ")
            v = int(input())
            if (v < 1) or (v > g.ordemGrafo()):
                print("\nErro: VERTICE INVALIDO")
            else:
                vizinhos = g.encontrarVizinhos(v)
                vizinhos.sort()
                print("\n- VIZINHOS DO VERTICE",v,":",vizinhos)
            
              
        elif escolha == '4':
            print("Entre com o vertice que deseja saber o grau:", end = " ")
            v = int(input())
            if (v < 1) or (v > g.ordemGrafo()):
                print("\nErro: VERTICE INVALIDO")
            else:
                print("\n- GRAU DO VERTICE",v,":",g.grauVertice(v))
              
        elif escolha == '5':
            print("\n- SEQUENCIA DE GRAUS DO GRAFO:",g.sequenciaGrausGrafo())
             
        elif escolha == '6':
            if (g.cicloNegativo==1):
                print("\nErro: GRAFO COM CICLO NAGATIVO! Impossivel calcular exentricidade de um vertice.") 
            else:
                print("Entre com o vertice que deseja saber sua excentricidade: ", end = " ")
                v = int(input())
                if (v < 1) or (v > g.ordemGrafo()):
                    print("\nErro: VERTICE INVALIDO")
                else:
                    print("\n- EXCENTRICIDADE DO VERTICE",v,": ",g.exentricidadeVertice(v))         
        
        elif escolha == '7':
            if (g.cicloNegativo==1):
                print("\nErro: GRAFO COM CICLO NAGATIVO! Impossivel calcular o raio do grafo.") 
            else:
                print("\n- RAIO DO GRAFO:", g.raioGrafo())

        elif escolha == '8':
            if (g.cicloNegativo==1):
                print("\nErro: GRAFO COM CICLO NAGATIVO! Impossivel calcular o diametro do grafo.") 
            else:
                print("\n- DIAMETRO DO GRAFO:",g.diametroGrafo())


        elif escolha == '9':
            if (g.cicloNegativo==1):
                print("\nErro: GRAFO COM CICLO NAGATIVO! Impossivel calcular o centro do grafo.") 
            else:
                print("\n- CENTRO DO GRAFO:",g.centroGrafo())
            
        elif escolha == '10':
            print("Entre com o vertice que deseja começar a busca em profundidade:", end = " ")
            v = int(input())
            if (v < 1) or (v > g.ordemGrafo()):
                print("\nErro: VERTICE INVALIDO")
            else:
                vizitados, retorno = g.buscaProfundidade(v)
                print("\n- BUSCA EM PROFUNDIDADE COMEÇANDO DO VERTICE",v,":")
                print("-- VERTICES VISITADOS:",vizitados)
                print("-- ARESTAS DE RETORNO:", retorno )
                
        elif escolha == '11':
            if (g.cicloNegativo==1):
                print("\nErro: GRAFO COM CICLO NAGATIVO! Impossível calcular distancia e caminho minimo entre vertices.")  
            else:
                print("Entre com o vertice de origem:", end = " ")
                origem = int(input())
                print("Entre com o vertice de destino:", end = " ")
                destino = int(input())
                max = g.ordemGrafo()
                if (origem < 1) or (origem > max) or (destino < 1) or (destino > max):
                    print("\nErro: VERTICE INVALIDO")
                else:
                    print("\n- DISTANCIA ENTRE {:d}  E {:d} : {:.2f}".format(origem,destino,g.distancia(origem,destino)))
                    print("- CAMINHO MINIMO ENTRE",origem,"E",destino,":",g.caminhoMinimo(origem,destino))

        elif escolha == '12':
            if (g.cicloNegativo==1):
                print("\nErro: GRAFO COM CICLO NAGATIVO! Impossivel calcular centralidade de proximidade de um vertice.") 
            else: 
                print("Entre com o vertice que deseja calcular a centralidade de proximidade:", end = " ")
                v = int(input())
                if (v < 1) or (v > g.ordemGrafo()):
                    print("\nErro: VÉRTICE INVÁLIDO")
                else:  
                    print("- CENTRALIDADE DE PROXIMIDADE DO VERTICE {:d} : {:.2f}".format(v,g.CentralidadeProxC(v)))
        
        elif escolha == '13':
            print("\n- REPRESENTAÇAO POR LISTA DE ADJACENCIA:\n")
            g.imprimirListaAdjacencia()
        
        elif escolha == '14':
            print("\n- MATRIZES FLOYD-WARSHALL")
            g.imprimirMatrizesFloydWarshall()
            
            
        elif escolha == '15':
            grau = g.ordemGrafo()
            print("-------------------------------------------------------------------------")
            
            print("\n- REPRESENTAÇAO POR LISTA DE ADJACENCIA:\n")
            g.imprimirListaAdjacencia()
        
            print("\n- MATRIZES FLOYD-WARSHALL")
            g.imprimirMatrizesFloydWarshall()

            print("\n- ORDEM DO GRAFO:",g.ordemGrafo())

            print("\n- TAMANHO DO GRAFO:",g.tamanhoGrafo())

            print()
            for v in range (1, grau+1):
                vizinhos = g.encontrarVizinhos(v)
                vizinhos.sort()
                print("- VIZINHOS DO VERTICE ",v,":",vizinhos)

            print()
            for v in range (1, grau+1):
                print("- GRAU DO VERTICE",v,":",g.grauVertice(v))
                
            print("\n- SEQUENCIA DE GRAUS DO GRAFO:",g.sequenciaGrausGrafo())
            
            print("\n- BUSCA EM PROFUNDIDADE: ")
            for v in range (1, grau+1):
                print("\n- BUSCA EM PROFUNDIDADE COMEÇANDO DO VERTICE",v,":")
                vizitados, retorno = g.buscaProfundidade(v)
                print("-- VERTICES VISITADOS:",vizitados)
                print("-- ARESTAS DE RETORNO:", retorno )

            print()
            if (g.cicloNegativo==1):
                print("Erro: GRAFO COM CICLO NAGATIVO! Impossivel usar o restante das funcoes.")
            else:
                print("\n- DISTANCIA E CAMINHO MINIMO:")
                origem = 1
                for d in range (1,grau+1):
                    print()
                    destino = d
                    print("- DISTANCIA ENTRE {:d}  E {:d}: {:.2f}".format(origem,destino,g.distancia(origem,destino)))
                    print("- CAMINHO MINIMO ENTRE",origem,"E",destino,":",g.caminhoMinimo(origem,destino))
                
                print()
                for v in range (1,grau+1):
                    print("- EXENTRICIDADE DO VERTICE {:d}: {:.2f}".format(v,g.exentricidadeVertice(v)))
                
                print("\n- RAIO DO GRAFO:", g.raioGrafo())
                print("\n- DIAMETRO DO GRAFO:",g.diametroGrafo())
                print("\n- CENTRO DO GRAFO:",g.centroGrafo())
                
                print()
                for v in range (1,grau+1):
                    print("- CENTRALIDADE DE PROXIMIDADE DO VERTICE {:d}: {:.2f}".format(v,g.CentralidadeProxC(v)))
                    
        elif escolha == '16':
            break
        
        else:
            print("Erro: ESCOLHA INVÁLIDA")
    
    
while True:
    print("\n-------------------------------------------------------------------------")
    print("MENU")
    print("-------------------------------------------------------------------------")
    print("[ 1 ] | ESCOLHER ARQUIVO")
    print("[ 2 ] | USAR FUNÇÕES DA BIBLIOTECA")
    print("[ 3 ] | GERAR ARQUIVO .json")
    print("[ 4 ] | ENCERRAR")
    print("-------------------------------------------------------------------------")
    print("Entre com sua escolha:", end = " ")
    escolha = input()
    
    if escolha == '1':
        escolherArquivo()
        
    elif escolha == '2':
        if g.vertices == 0: 
            print("Erro: PRIMEIRO ESCOLHA O ARQUIVO")
        else:
            menuFuncoes()
        
    elif escolha == '3':
        if g.vertices == 0: 
            print("Erro: PRIMEIRO ESCOLHA O ARQUIVO")
        else:
            a.gerarJson()
    
    elif escolha == '4':
        break
        
    else:
        print("Erro: ESCOLHA INVÁLIDA!")








