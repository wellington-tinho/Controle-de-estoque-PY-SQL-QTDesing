from Pessoa import Usuario

class Funcionario(Usuario):
  def __init__(self,nome,ocupacao,_id):
    super().__init__(nome,_id)
    self.__ocupacao=ocupacao

  @property
  def ocupacao(self):
    return self.__ocupacao

  @ocupacao.setter
  def ocupacao(self,value):
    self.__ocupacao=value
  
  # @property
  # def nome(self):1
  #   return self.nome

  # @nome.setter
  # def nome(self,value):
  #   self.nome=value

  # @property
  # def id(self):
  #   return self.id

  # @id.setter
  # def id(self,value):
  #   self.id=value