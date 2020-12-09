from .Produto import Produtos

class Estoque: 
  def __init__(self):
    self.__produtos = [
      Produtos("Cafe", 20),
      Produtos("Feijao", 10),
      Produtos("Carne de Boi", 10),
      Produtos("Carne de Frango", 10),
      Produtos("Suco", 15),
      Produtos("Vinho", 12),
      Produtos("Refrigerante", 9),
      Produtos("Arroz", 3),
      Produtos("Sal", 5),
      Produtos("Açucar", 7),
      Produtos("Oleo", 8)
    ]
  
  def cadastrarProduto(self,nome, quantidade):
    produtoExiste = False
    for i in self.__produtos:
      if i.nome == nome:
        return False

    if not produtoExiste:
      produto = Produtos(nome, quantidade)
      self.__produtos.append(produto)
      return True

  def listarProdutos(self):
    print("_______________________________________________________________________________")
    print("Listagem de Produtos")
    print("_______________________________________________________________________________")
    for i in self.__produtos:
      print("Nome:", i.nome)
      print("Quantidade:", i.quantidade)
      print("_______________________________________________________________________________")

  def buscarProduto(self, nome):
    for i in self.__produtos:
      if i.nome == nome:
        return i
    return False

  def exluirProduto(self, produto: Produtos):
    if isinstance(produto, Produtos):
      self.__produtos.remove(produto)
      return True
    else:
      return False

  def produtoExiste(self, nome):
    for i in self.__produtos:
      if i.nome == nome:
        return i

    return False

  def tem_qtd_disponivel(self, nome, quantidade):
    produto = self.produtoExiste(nome)
    if produto:
      if(produto.quantidade - quantidade >= 0):
        return True

    return False