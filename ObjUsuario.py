class objUsuario:
 def __init__(self,nome, email,endereco, linha,plano):
    self.nome = nome
    self.email = email
    self.endereco = endereco
    self.plano = plano
    self.linha = linha

 def imprimir(self):
  print( "O cliente, " + self.nome  + "com email " +  self.email +", "
         + "morador do endereço," +  self.endereco + "," + " Dono da linha, " )