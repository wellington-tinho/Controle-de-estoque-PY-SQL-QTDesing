from ..model.Estoque import *
from ..model.Funcionario import *
from ..view.menu import menu
from ..model.Pessoa import *
from ..model.Produto import *
from ..main import main 

from ..controller.Database_Pessoas import Database_Pessoas



def primeira_vez(estoque):
  print("Bem vindo aos primeiros passos \n Primeiramente é preciso cadastrar um Funcionario \n")


  #cadastro do Funcionario
  escolha=input("""  Para efetuar cadastro insira seu nome, sua ocupação e seu identificador unico - ID (separando-os por virgula ',')
                      ex: Wellington,developer,123 \n""").split(',')
  user=Database_Pessoas.cadastro_funcionario(escolha[0],escolha[2],escolha[1])
  logado = user
  print("\n Cadastro do Funcionario realizado com sucesso, agora iremos cadastrar um produto ")
  nomeProd = input("Digite o nome do produto: ")
  qtdProd = int(input("Digite a quantidade em estoque: "))


  #cadastro de Produtos
  cadastrado = estoque.cadastrarProduto(nomeProd, qtdProd)
  if cadastrado:
    print('Produto cadastrado com sucesso!')
  else:
    print('Ocorreu um erro ao cadastrar o produto, verifique se o produto ja não esta cadastrado')
  print("Muito bem agora só falta o cadastro do cliente")


  #cadastro de Clientes
  escolha=input("""\n  Para efetuar cadastro insira seu nome, sua ocupação e seu identificador unico (separando-os por virgula ',')
                      ex: Wellington,123 \n""").split(',')
  user=Database_Pessoas.cadastro_usuario(escolha[0],escolha[1])
  logado = user

  print("Cadastro do Cliente realizado com sucesso, agora ja podemos entrar no sistema")

  main(logado)