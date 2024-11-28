from ObjUsuario import objUsuario
from ObjLinha import objLinha

# Main = classe que instancia os objetos
# objUsuario = classe que representa um usuario
# classe que representa os dados da linha


class Main:
  data = [
 "Bob, bob@xyzzzzzz.com, Rua 12 de Abril, +5500000000000, 40GB",
 "Alice, alice@xyzzzzzz.com, Rua Brasil, +5500111111111, 10GB"
 ]
  formatData = []
  for element in data:
   partes = [parte.strip() for parte in element.split(',')]
   formatData = partes
   usu = objUsuario(formatData[0],formatData[1],formatData[2],formatData[3],formatData[4])
   usu.imprimir()
   lin = objLinha(formatData[3],formatData[4])
   lin.imprimir()




# È feito um for iterando sobre os dados de exemplo, gerando a criação dos objetos solicitados
# cada objeto tem o comportamento de imprimir a mensagem que foi solicitado