class objLinha:
    def __init__(self,plano,linhaTelefone):
        self.plano = plano
        self.linhaTelefone = linhaTelefone

    def imprimir(self):
     print( self.linhaTelefone + " com plano contratado de " + self.plano)