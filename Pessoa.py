
class Usuario():
  def __init__(self,nome,_id):
    self.__nome=nome
    self.__id=_id

  @property
  def nome(self):
    return self.__nome

  @nome.setter
  def nome(self,value):
    self.__nome=value

  @property
  def id(self):
    return self.__id

  @id.setter
  def id(self,value):
    self.__id=value


def person_cadastradas(lista1, lista2):
  print("\n Pessoas cadastradas no sistema")
  for i in lista1:
    print(f"{i.nome}:{i.id} ")
  for i in lista2:
    print(f"{i.nome}:{i.id} ")