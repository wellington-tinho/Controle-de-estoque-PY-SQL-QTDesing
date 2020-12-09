from ..model.Estoque import *
from ..model.Funcionario import *
from ..model.Pessoa import *
from ..model.Produto import *
from ..main import main 

from ..controller.Database_Pessoas import Database_Pessoas


def administracao(logado,estoque):
  print("Area adm")
  if Database_Pessoas.is_funcionario(logado):
    produto_menu = input("""Digite
    1 - Cadastrar
    2 - Buscar
    3 - Alterar
    4 - Excluir
    5 - Listar Produtos
    6 - Voltar
    0 - Sair
    """)
    if produto_menu == '1':
      nomeProd = input("Digite o nome do produto: ")
      qtdProd = int(input("Digite a quantidade em estoque: "))

      cadastrado = estoque.cadastrarProduto(nomeProd, qtdProd)
      if cadastrado:
        print('Produto cadastrado com sucesso!')
      else:
        print('Ocorreu um erro ao cadastrar o produto, verifique se o produto ja não esta cadastrado')
        
    elif produto_menu == '2':
      nome = input('Digite o nome do produto: ')
      produto = estoque.buscarProduto(nome)
      if produto: 
        print("Nome: ", produto.nome)
        print("Quantidade: ", produto.quantidade)
      else:
        print('Não possivel encontrar esse produto!')

    elif produto_menu == '3':
      nome = input('Digite o nome do produto: ')
      produto = estoque.buscarProduto(nome)
      if produto:
        produto.quantidade = int(input('Dige a nova quantidade em estoque: '))
        print('As alterações foram salvas com sucesso!')
      else:
        print('Não possivel encontrar esse produto!')

    elif produto_menu == '4':
      nome = input('Digite o nome do produto: ')
      produto = estoque.buscarProduto(nome)
      if produto:
        estoque.exluirProduto(produto)
        print('O produto foi excluido com sucesso!')
        # Produtos.flag=False
      else:
        print('Não possivel encontrar esse produto!')
    elif produto_menu == '5':
      estoque.listarProdutos()
    elif produto_menu == '0':
      exit()
  else:
    print("Voce não tem autorização para entrar aqui, Logue novamente como Funcionario")

  main(logado)
  