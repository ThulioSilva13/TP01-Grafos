import json
from Aresta import Aresta

from Vertice import Vertice

with open('grafoConvertido.json', 'r') as fileJson:
    data = json.load(fileJson)

listOrigin = []
listDestiny = []
origem = data['data']['edges']['_data']['1']['from']
destino = data['data']['edges']['_data']['1']['to']
peso = 0
for chave, valor in data['data']['edges']['_data'].items():
    listOrigin.append(data['data']['edges']['_data'][str(chave)]['from'])
    listDestiny.append(data['data']['edges']['_data'][str(chave)]['to'])
    #print("a chave é: ",chave)
    #print("o valor é: ",valor)
print(listOrigin)
print(listDestiny)
#aresta = Aresta(origem, destino, peso)
#print("a primeira aresta começa no vetice",aresta.origem,"e vai até o vértice", aresta.destino)