from ..model.Estoque import *
from ..model.Funcionario import *
from ..view.menu import menu
from ..model.Pessoa import *
from ..model.Produto import Produtos, venda_produtos
from ..main import main 

from ..controller.Database_Pessoas import Database_Pessoas



def compra_venda(logado,estoque):
  _,_,_,_,compra_step1,venda_step1,_ = menu()
   #saber se existe produto
  if(Produtos.flag):
    estoque.listarProdutos()
    #saber se é cliente
    if Database_Pessoas.is_cliente(logado):
      escolha=input(compra_step1)
      user = Database_Pessoas.id_existe(escolha,Database_Pessoas.funcionarios)
      if(user and escolha != 0):
        nome_prod=input("Infome o nome do produto: ")
        produto = estoque.produtoExiste(nome_prod)
        if produto:
          vendido = venda_produtos(produto)
          if vendido:
            print("Compra realizada com sucesso")
          else:
            print("Falha ao realizar a compra")
        else:
          print("Não existe esse produto no estoque")

    elif Database_Pessoas.is_funcionario(logado):
      escolha=input(venda_step1)
      #recebe id
      user = Database_Pessoas.id_existe(escolha,Database_Pessoas.clientes)
      if(user and escolha != 0):
        nome_prod=input("Infome o nome do produto: ")
        produto = estoque.produtoExiste(nome_prod)
        if produto:
          vendido = venda_produtos(produto)
          if vendido:
            print("Venda realizada com sucesso")
          else:
            print("Falha ao realizar a venda")
        else:
          print("Não existe esse produto no estoque")
    main(logado)
  else:
    print("Não ha produtos cadastrados, é recomendado ir para Administração")
    main(logado) 