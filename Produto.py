class Produtos():
  flag=False
  def __init__(self,nome: str,quantidade: int):
    self.__nome=nome
    self.__quantidade=quantidade
    Produtos.flag=True #talvez essa verificação fique no estoque agora.

  @property
  def quantidade(self):
    return self.__quantidade

  @quantidade.setter
  def quantidade(self,value: int):
    self.__quantidade=value

  @property
  def nome(self):
    return self.__nome

  @nome.setter
  def nome(self,value):
    self.__nome=value

def venda_produtos(produto: Produtos): 
  quantidade = int(input("Informe a quantidade desejada: "))
  if produto.quantidade - quantidade >= 0:
    produto.quantidade = produto.quantidade - quantidade
    return True
  
  return False

