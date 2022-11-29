import json

class Arquivo:
    
    def __init__(self):
        self.nome = " "
    
    def lerTxt(self):
        linhas = []
        arquivo = open(self.nome)
        
        aux = 0
        for linha in arquivo.readlines():
            if aux != 0:
                linhas.append(list(map(float,linha.replace("\n","").split(" "))))
            else:
                qntdVertices = (int(linha.replace("\n","")))           
            aux += 1
        
        return [qntdVertices, linhas]

    def lerJson(self,nomeArquivo):
        with open(nomeArquivo, 'r') as fileJson:
            
            grafoJson = json.load(fileJson)
            txt  = open(nomeArquivo.replace("json", "txt"), 'w')
            
            quantidadeVertices = grafoJson['data']['nodes']['length']
            txt.write(str(quantidadeVertices))

            path = grafoJson['data']['edges']['_data']
            for i in range(1,grafoJson['data']['edges']['length']+1):
                origem = path[str(i)]['from']
                destino = path[str(i)]['to']
                label = path[str(i)]['label']
                txt.write("\n"+str(origem)+" "+str(destino)+" "+ label)

    def gerarJson(self):
        arq = self.lerTxt()
        with open('base.json', 'r') as fileJson:
            grafoJson = json.load(fileJson)
            grafoJson['data']['nodes']['length'] = arq[0]
            grafoJson['data']['edges']['length'] = len(arq[1])
            
            for i in range(arq[0]):
                vertice = {"id": int(i+1), "label": str(i+1)}
                grafoJson["data"]["nodes"]["_data"][str(i+1)] = vertice

            for i in range(len(arq[1])):
                aresta = {"from": int(arq[1][i][0]), "to": int(arq[1][i][1]), "label": str(arq[1][i][2]),"id": str(i+1),"color": {}}
                grafoJson["data"]["edges"]["_data"][str(i+1)] = aresta
                
        nomeJson = self.nome.replace("txt","json") #funcao lerJson vai gerar o arquivo txt de mesmo nome
        with open(nomeJson, 'w') as outputFileJson:
            json.dump(grafoJson, outputFileJson, indent=4)
        
        print("-------------------------------------------------------------------------")
        print("ARQUIVO ",nomeJson," GERADO COM SUCESSO!")
    
    def escreverArvoreGeradoraMinima(self,arvoreGeradoraMinima, peso):
        nome = (self.nome).replace(".txt", "_AGMin.txt")
        arquivo = open(nome,'w')
        # em uma arvore geradora minima |M| = |N|-1 => |N| = |M|+1
        N = len(arvoreGeradoraMinima)+1
        arquivo.write(str(N))
        for i in arvoreGeradoraMinima:
            arquivo.write('\n'+str(i.origem)+' '+str(i.destino)+' '+str(i.peso))
        arquivo.write('\n'+str(peso))
        arquivo.close()
        
        
        

