class Aresta:
    def __init__(self, origem, destino):
        self.origem = origem
        self.destino = destino

    def getOrigem(self):
        return self.origem

    def setOrigem(self, origem):
        self.origem = origem

    def getDestino(self):
        return self.destino

    def setDestino(self, destino):
        self.destino = destino

    def getPeso(self):
        return self.peso

    def setPeso(self, peso):
        self.peso = peso
