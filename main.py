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
    g.inicializaListaAdjacencia(qntdVertices)
    for i in range(len(linhas)):
        g.insereAresta(int(linhas[i][0]), int(linhas[i][1]), float(linhas[i][2]))
    g.imprimirListaAdjacencia()
    g.floydWarshall()
    g.verificaCicloNegativo() #já conferi se é ciclo negativo

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
        print("[ 10 ] | BUSCA EM PROFUNDIDADE")
        print("[ 11 ] | DISTANCIA E CAMINHO MÍNIMO")
        print("[ 12 ] | CENTRALIDADE DE PROXIMIDADE C DE UM VÉTICE X")
        print("[ 13 ] | USAR TODAS AS FUNÇÔES")
        print("\n[ 14 ] | VOLTAR PRO MENU")
        print("-------------------------------------------------------------------------")
        print("Entre com sua escolha:", end = " ")
        escolha = input()
        
        if escolha == '1':
            print("\n- Ordem do Grafo: ",g.ordemGrafo())
      
        elif escolha == '2':
            print("\n- Tamanho do Grafo: ",g.tamanhoGrafo())
     
        elif escolha == '3':
            print("\nEntre com o vértice que deseja saber seus vizinhos: ", end = " ")
            v = int(input())
            if v > g.ordemGrafo():
                print("Erro: VÉRTICE INVÁLIDO")
            else:
                print("\n- Vizinhos do Vertice",v,": ",g.encontrarVizinhos(v))
            
              
        elif escolha == '4':
            print("\nEntre com o vértice que deseja saber o grau: ", end = " ")
            v = int(input())
            if v > g.ordemGrafo():
                print("Erro: VÉRTICE INVÁLIDO")
            else:
                print("\n- Grau do Vertice",v,": ",g.grauVertice(v))
              
        elif escolha == '5':
            print("\n- Sequencia de Graus do Grafo: ",g.sequenciaGrausGrafo())
             
        elif escolha == '6':
            if (g.cicloNegativo==1):
                print("ERRO: Impossivel calcular exentricidade de um vértice pois grafo com Ciclo Negativo!") 
            else:
                print("\nEntre com o vértice que deseja saber sua excentricidade: ", end = " ")
                v = int(input())
                if v > g.ordemGrafo():
                    print("Erro: VÉRTICE INVÁLIDO")
                else:
                    print("- Exentricidade do Vertice",v,": ",g.exentricidadeVertice(v))         
        
        elif escolha == '7':
            if (g.cicloNegativo==1):
                print("ERRO: Impossivel calcular o raio do grafo pois grafo com Ciclo Negativo!") 
            else:
                print("\n- Raio do Grafo:", g.raioGrafo())

        elif escolha == '8':
            if (g.cicloNegativo==1):
                print("ERRO: Impossivel calcular o diametro do grafo pois grafo com Ciclo Negativo!") 
            else:
                print("\n- Diametro do Grafo:",g.diametroGrafo())


        elif escolha == '9':
            if (g.cicloNegativo==1):
                print("ERRO: Impossivel calcular o centro do grafo pois grafo com Ciclo Negativo!") 
            else:
                print("\n- Centro do Grafo:",g.centroGrafo())
            
        elif escolha == '10':
            print("\nEntre com o vértice que deseja começar a busca em profundidade: ", end = " ")
            v = int(input())
            if v > g.ordemGrafo():
                print("Erro: VÉRTICE INVÁLIDO")
            else:
                vizitados, retorno = g.buscaProfundidade(v)
                print("- Vértices vizitados na Busca em Profundidade: ",vizitados)
                print("- Arestas de Retorno: ", retorno )
        
        elif escolha == '11':
            if (g.cicloNegativo==1):
                print("ERRO: Impossivel calcular distancia e caminho mínimo entre vertices pois grafo com Ciclo Negativo!")  
            else:
                print("\nEntre com o vértice de origem: ", end = " ")
                origem = int(input())
                print("\nEntre com o vértice de destino: ", end = " ")
                destino = int(input())
                max = g.ordemGrafo()
                if (origem > max) or (destino > max):
                    print("Erro: VÉRTICE INVÁLIDO")
                else:
                    print("- Distancia entre {:d}  e {:d} é: {:.2f}".format(origem,destino,g.distancia(origem,destino)))
                    print("- Caminho minimo entre",origem,"e",destino,":",g.caminhoMinimo(origem,destino))

        elif escolha == '12':
            if (g.cicloNegativo==1):
                print("ERRO: Impossivel calcular centralidade de proximidade do vertice pois grafo com Ciclo Negativo!") 
            else: 
                print("\nEntre com o vértice que deseja calcular a centralidade: ", end = " ")
                v = int(input())
                if v > g.ordemGrafo():
                    print("Erro: VÉRTICE INVÁLIDO")
                else:  
                    print("- Centralidade de Proximidade do vértice {:d} é: {:.2f}".format(v,g.CentralidadeProxC(v)))
        
        elif escolha == '13':
            grau = g.ordemGrafo()
            print("-------------------------------------------------------------------------")
            print("\nCaracteristicas do Grafo:")

            print("\n- Ordem do Grafo: ",g.ordemGrafo())

            print("\n- Tamanho do Grafo: ",g.tamanhoGrafo())

            print()
            for i in range (1, grau+1):
                print("- Vizinhos do Vertice",i,": ",g.encontrarVizinhos(i))

            print()
            for i in range (1, grau+1):
                print("- Grau do Vertice",i,": ",g.grauVertice(i))
                
            print("\n- Sequencia de Graus do Vertice : ",g.sequenciaGrausGrafo())

            print("\n- Busca em Profundidade: ")
            inicio = 1
            vizitados, retorno = g.buscaProfundidade(inicio)
            print("-- Vértices vizitados na Busca em Profundidade: ",vizitados)
            print("-- Arestas de Retorno: ", retorno )

            print()
            if (g.cicloNegativo==1):
                print("ERRO: Impossivel usar restantes das funções pois grafo Ciclo Negativo!")
            else:
                print("\n- Distancia e Caminho Minimo: ")
                origem = 1
                for i in range (1,grau+1):
                    print()
                    destino = i
                    print("- Distancia entre {:d}  e {:d} é: {:.2f}".format(origem,destino,g.distancia(origem,destino)))
                    print("- Caminho minimo entre",origem,"e",destino,":",g.caminhoMinimo(origem,destino))

                for i in range (1,grau+1):
                    print("- Exentricidade do Vertice {:d}: {:.2f}".format(i,g.exentricidadeVertice(i)))
                
                print("\n- Raio do Grafo {:d}: {:.2f}".format(i, g.raioGrafo()))
                print("\n- Diametro do Grafo {:d}: {:.2f}".format(i,g.diametroGrafo()))
                print("\n- Centro do Grafo: ",g.centroGrafo())
                
                print()
                for i in range (1,grau+1):
                    print("- Centralidade de Proximidade do vértice {:d} é: {:.2f}".format(i,g.CentralidadeProxC(i)))
                    
        elif escolha == '14':
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








