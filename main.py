import json
from Aresta import Aresta

from Vertice import Vertice

with open('grafoConvertido.json', 'r') as fileJson:
    data = json.load(fileJson)

origem = data['data']['edges']['_data']['1']['from']
destino = data['data']['edges']['_data']['1']['to']
peso = 0
aresta = Aresta(origem, destino, peso)
print("a primeira aresta começa no vetice",aresta.origem,"e vai até o vértice", aresta.destino)