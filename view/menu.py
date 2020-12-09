
def menu():
  home_menu="""
  Bem Vindo ao gerenciador de estoque WK, escolha uma opção.
  
  1 - Login | Cadastro
  2 - Realizar Compra | Venda 
  3 - Primeira vez no Estoque siga esses passos.
  4 - Administracao
  0 - Sair
  _______________________________________________________________________________

  """

  menu_escolha_user="""
  1 - Cliente
  2 - Funcionario
  3 - Voltar
  0 - Sair
  """

  menu_entrar_cliente="""
  Para entrar insira seu e ID 
  123
  Para efetuar cadastro insira seu nome e seu identificador unico (separando-os por virgula ',')
  ex: Wellington,123
  Para sair digite:  0
  """

  menu_entrar_Funcionario="""
   Para entrar insira seu nome cadastrado e ID (separando-os por virgula ',')
    Wellington,1234
  Para efetuar cadastro insira seu nome, sua ocupação e seu identificador unico (separando-os por virgula ',')
  ex: Wellington,developer,1234
  Para sair digite: 0
  """

  compra_step1="""
  Identificamos que voce esta logado como Cliente logo assim irá realizar uma compra
  Para logar como Funcionario 
  digite:  0
  E faça o Login novamente
  Caso Contrario informe o ID valido do Funcionario para iniciar a validaçao da compra
  """

  venda_step1="""
  Identificamos que voce esta logado como Funcionario logo assim irá realizar uma venda
  Para logar como Cliente 
  digite:  0
  E faça o Login novamente
  Caso Contrario informe o ID valido do Cliente para iniciar a Venda
  """

  compra_venda_step2="""
  Informe a quantidade desejada
 
  """
  return home_menu,menu_escolha_user,menu_entrar_cliente,menu_entrar_Funcionario,compra_step1,venda_step1,compra_venda_step2
