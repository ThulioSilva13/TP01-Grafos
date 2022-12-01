from grafo import Grafo
from arquivo import Arquivo

import os.path
import os

os.system('clear') 
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
        os.system('clear')
        print("Erro: ESCOLHA INVÁLIDA!")
        escolherArquivo()

def receberArquivo(formato):
    flag = 1
    
    if flag == 1:

        if formato == 1:
            print("Entre com o nome do arquivo com a extensão .json:", end = " ")
            nomeArquivo = input()
            os.system('clear')
            if ".json" not in nomeArquivo:
                nomeArquivo = nomeArquivo + ".json"
            #else:
            if(os.path.isfile(nomeArquivo)): #coneferir se existe o aquivo
                a.lerJson(nomeArquivo)
                a.nome = nomeArquivo.replace("json","txt") #funcao lerJson vai gerar o arquivo txt de mesmo nome
                flag = 0
                print("ARQUIVO ESCOLHIDO COM SUCESSO")
            else:
                print("Erro: ARQUIVO NÃO ENCONTRADO")
                escolherArquivo()
            
        else: #se nao é 1 é 2
            print("Entre com o nome do arquivo com a extensão .txt:", end = " ")
            nomeArquivo = input()
            os.system('clear')
            if ".txt" not in nomeArquivo:
                nomeArquivo = nomeArquivo + ".txt"
            
            if(os.path.isfile(nomeArquivo)): #coneferir se existe o aquivo 
                a.nome = nomeArquivo
                flag = 0
                print("ARQUIVO ESCOLHIDO COM SUCESSO")
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
        print("----------------------------------------------------------")
        print("[ 13 ] | VERIFICAR SE O GRAFO POSSUI CICLO")
        print("[ 14 ] | ÁRVORE GERADORA MÍNIMA")
        print("[ 15 ] | COBERTURA MÍNIMA DE VÉRTICES")
        print("[ 16 ] | EMPARELHAMENTO MÁXIMO")
        print("----------------------------------------------------------")
        print("[ 17 ] | REPRESENTAÇAO DO GRAFO EM LISTA DE ADJACENCIA")
        print("[ 18 ] | MATRIZES RESULTANTES FLOYD-WARSHALL")
        print("[ 19 ] | USAR TODAS AS FUNÇOES")
        print("\n[ 20 ] | VOLTAR PRO MENU")
        print("-------------------------------------------------------------------------")
        print("Entre com sua escolha:", end = " ")
        escolha = input()
        os.system('clear')
        
        if escolha == '1': # ordem do grafo
            print("\n- ORDEM DO GRAFO:",g.ordemGrafo())
      
        elif escolha == '2': # tamanho do grafo
            print("\n- TAMANHO DO GRAFO:",g.tamanhoGrafo())
     
        elif escolha == '3': # vizinhos de um vértice
            print("Entre com o vertice que deseja saber seus vizinhos:", end = " ")
            v = int(input())
            if (v < 1) or (v > g.ordemGrafo()):
                print("\nErro: VERTICE INVALIDO")
            else:
                vizinhos = g.encontrarVizinhos(v)
                vizinhos.sort()
                print("\n- VIZINHOS DO VERTICE",v,":",vizinhos)
            
              
        elif escolha == '4': # sequencia de graus do grafo
            print("Entre com o vertice que deseja saber o grau:", end = " ")
            v = int(input())
            if (v < 1) or (v > g.ordemGrafo()):
                print("\nErro: VERTICE INVALIDO")
            else:
                print("\n- GRAU DO VERTICE",v,":",g.grauVertice(v))
              
        elif escolha == '5':
            print("\n- SEQUENCIA DE GRAUS DO GRAFO:",g.sequenciaGrausGrafo())
             
        elif escolha == '6': # excentricidade de um vértice
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
            if (g.cicloNegativo==1): # raio do grafo
                print("\nErro: GRAFO COM CICLO NAGATIVO! Impossivel calcular o raio do grafo.") 
            else:
                print("\n- RAIO DO GRAFO:", g.raioGrafo())

        elif escolha == '8': # diamentro do grafo
            if (g.cicloNegativo==1):
                print("\nErro: GRAFO COM CICLO NAGATIVO! Impossivel calcular o diametro do grafo.") 
            else:
                print("\n- DIAMETRO DO GRAFO:",g.diametroGrafo())


        elif escolha == '9': # centro do grafo
            if (g.cicloNegativo==1):
                print("\nErro: GRAFO COM CICLO NAGATIVO! Impossivel calcular o centro do grafo.") 
            else:
                print("\n- CENTRO DO GRAFO:",g.centroGrafo())
            
        elif escolha == '10': # busca em profunidade
            print("Entre com o vertice que deseja começar a busca em profundidade:", end = " ")
            v = int(input())
            if (v < 1) or (v > g.ordemGrafo()):
                print("\nErro: VERTICE INVALIDO")
            else:
                vizitados, retorno = g.buscaProfundidade(v)
                print("\n- BUSCA EM PROFUNDIDADE COMEÇANDO DO VERTICE",v,":")
                print("-- SEQUENCIA DE VERTICES VISITADOS:",vizitados)
                print("-- ARESTAS DE RETORNO:", retorno )
                
        elif escolha == '11': # distancia e caminho minimo
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

        elif escolha == '12': # centralidade de proximidade de um vértice
            if (g.cicloNegativo==1):
                print("\nErro: GRAFO COM CICLO NAGATIVO! Impossivel calcular centralidade de proximidade de um vertice.") 
            else: 
                print("Entre com o vertice que deseja calcular a centralidade de proximidade:", end = " ")
                v = int(input())
                if (v < 1) or (v > g.ordemGrafo()):
                    print("\nErro: VÉRTICE INVÁLIDO")
                else:  
                    print("- CENTRALIDADE DE PROXIMIDADE DO VERTICE {:d} : {:.2f}".format(v,g.centralidadeProximidade(v)))
        
        elif escolha == '13': # verificar se grafo possui ciclos
            if (g.verificarCiclos()):
                print("\n- O GRAFO TEM CICLO")
            else:
                print("\n- O GRAFO NÃO TEM CICLO")
            
        elif escolha == '14': 
            print("- ÁRVORE GERADORA MÍNIMA")
            arvoreGeradoraMinima, peso = g.algoritmoKruskal()

            for i in arvoreGeradoraMinima:
                print(" ",i.origem,"->",i.destino)
            
            print("\n-- PESO TOTAL =",peso)
            
            #ecrever arvore geradora minima em um arquivo (no mesmo formato de entrada)
            a.escreverArvoreGeradoraMinima(arvoreGeradoraMinima, peso)
            
        elif escolha == '15': 
            print("- UMA COBERTURA MÍNIMA DE VÉRTICES:", g.coberturaVertices())
            
        elif escolha == '16': 
            matching = g.emparelhamentoMaximo()
            
            print("- EMPARELHAMENTO MÁXIMO:", end=" ")
            for i in range (len(matching)):
                if (i == len(matching)-1):
                    print("({:d},{:d})".format(matching[i].origem,matching[i].destino))
                else:
                    print("({:d},{:d}) - ".format(matching[i].origem,matching[i].destino), end="")
        
        elif escolha == '17': # representação do grafo porlista de adjacência
            print("\n- REPRESENTAÇAO POR LISTA DE ADJACENCIA:\n")
            g.imprimirListaAdjacencia()
        
        elif escolha == '18': # matrizes dt e rot resultantes do Floyd-Warshall
            print("\n- MATRIZES FLOYD-WARSHALL")
            g.imprimirMatrizesFloydWarshall()
            
            
        elif escolha == '19': # usar todas as funções
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
                print("-- SEQUENCIA VERTICES VISITADOS:",vizitados)
                print("-- ARESTAS DE RETORNO:", retorno )
            
            # verificar ciclos
            if (g.verificarCiclos()):
                print("\n- O GRAFO TEM CICLO")
            else:
                print("\n- O GRAFO NÃO TEM CICLO")
            
            
            print("\n- ÁRVORE GERADORA MÍNIMA") 
            arvoreGeradoraMinima, peso = g.algoritmoKruskal()

            for i in arvoreGeradoraMinima:
                print(" ",i.origem,"->",i.destino)
            
            print("\n-- PESO TOTAL =",peso)
            
            #ecrever arvore geradora minima em um arquivo (no mesmo formato de entrada)
            a.escreverArvoreGeradoraMinima(arvoreGeradoraMinima, peso)
            
            print("\n- UMA COBERTURA MÍNIMA DE VÉRTICES:", g.coberturaVertices())
            
            print("\n- EMPARELHAMENTO MÁXIMO:", end=" ")
                      
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
                    print("- CENTRALIDADE DE PROXIMIDADE DO VERTICE {:d}: {:.2f}".format(v,g.centralidadeProximidade(v)))
                    
        elif escolha == '20': # voltar para o menu
            break
        
        else:
            print("Erro: ESCOLHA INVÁLIDA")
        
        print("\n\n-------------------------------------------------------------------------")
        print("[ 1 ] | CONTINUAR UTILIZANDO FUNÇÕES DA BIBLIOTECA \n[ 2 ] | VOLTAR MENU")
        print("-------------------------------------------------------------------------")
        print("Entre com sua escolha:", end = " ")
        escolha = input()
        os.system('clear')
        if (escolha != '1'):
            break
        
    
    
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
    os.system('clear')
    
    if escolha == '1':
        g = Grafo()
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








