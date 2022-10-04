class Vertice:
    def __init__(vertice, identificador):
        vertice.visitado = False
        vertice.identificador = identificador

    def getVisitado(self):
        return self.visitado

    def setVisitado(self, visitado):
        self.visitado = visitado

    def getIdentificador(self):
        return self.identificador

    def setIdentificador(self, identificador):
        self.identificador = identificador
