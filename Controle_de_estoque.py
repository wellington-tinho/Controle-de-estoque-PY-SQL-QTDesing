
class Produtos():
  flag=False
  def __init__(self,nome: str,quantidade: int):
    self.__nome=nome
    self.__quantidade=quantidade
    Produtos.flag=True


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


class Funcionario():
  def __init__(self,nome,ocupacao,_id):
    self.__nome=nome
    self.__id=_id
    self.__ocupacao=ocupacao

  @property
  def ocupacao(self):
    return self.__ocupacao

  @ocupacao.setter
  def ocupacao(self,value):
      self.__ocupacao=value
  
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

pessoas_cadastradas=[Funcionario('kj','dev','321'), Usuario('jk','123')]
produtos_cadastrados = [ Produtos('c',5)]

def venda_produtos(produto, quantidade):
  print(f"Produtos restantes: {produto.quantidade - quantidade}")
  produto.quantidade = produto.quantidade - quantidade

def Buscar_produto(nome):### possivel erro
  for i in produtos_cadastrados:
    if i.nome == nome:
      return i
    return False

def cadastro_produtos(nome, quantidade):
  produtoExiste = False
  for i in produtos_cadastrados:
    if i.nome == nome:
      return False

  if not produtoExiste:
    produto = Produtos(nome, quantidade)
    produtos_cadastrados.append(produto)
    return True
    
def cadastro_usuario(nome,Id):
  user=Usuario(nome,Id)
  pessoas_cadastradas.append(user)
  return user
  
def cadastro_funcionario(nome,Id,ocupacao):
  user=Funcionario(nome,Id,ocupacao)
  pessoas_cadastradas.append(user)
  return user


def id_existe(Id):
  for i in pessoas_cadastradas:

    if (i.id == Id):
      return i
  return False

def excluir_produto(produto):
  try:
    produtos_cadastrados.remove(produto)
    return True
  except expression as identifier:
    return False

#Regra de Negocio / Validação 
def is_funcionario(pessoa):
  return isinstance(pessoa, Funcionario)

def is_cliente(pessoa):
  return isinstance(pessoa, Usuario)

def tem_qtd_disponivel( nome, quantidade):
  for i in produtos_cadastrados:
    if i.nome == nome:
      if i.quantidade - quantidade >= 0:
        return i
  
  return False

def showProducts():
  for i in produtos_cadastrados:
    print("_______________________________________________________________________________ \n")
    print("Nome:", i.nome)
    print("Quantidade:", i.quantidade)
  
def mostra_login(user):
  if is_funcionario(user):
    return f'Logado como funcionario: {user.nome}'

  if is_cliente(user):
    return f'Logado como Cliente: {user.nome4}'

  else:
    return 'Voce não esta logado'

def person_cadastradas():
  print("\n Pessoas cadastradas no sistema")
  for i in pessoas_cadastradas:
    print(f"{i.nome}:{i.id} ")

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


def main(logado=False):
  home_menu,menu_escolha_user,menu_entrar_cliente,menu_entrar_Funcionario,compra_step1,venda_step1,compra_venda_step2 = menu()

  logado=logado
  print("_______________________________________________________________________________ \n", mostra_login(logado))
  escolha=input(home_menu)

  #thead_escolha_1
  if(escolha == '1'):
    
    #escolha se é cliente ou Funcionario 1,2
    escolha=input(menu_escolha_user)

    #login_Cliente
    if(escolha == '1'):
        escolha=input(menu_entrar_cliente).split(',')

        if (len(escolha) == 1):
            user=id_existe(escolha[0])
            if(is_cliente(user)):
              logado = user
              print("Logado com Sucesso")
            else:
               print("ID not Found")
        
        if (len(escolha) == 2): 
          user=cadastro_usuario(escolha[0],escolha[1])
          logado = user
          print("Cadastro com Sucesso")
        else:
          print("voce escolheu sair")
        
        main(logado)

    #login_funcionario
    if(escolha == '2'):
      escolha=input(menu_entrar_Funcionario).split(',')
     

      if(len(escolha) == 2):
        user=id_existe(escolha[1])
        if(is_funcionario(user)):
          logado = user
          print("Logado com Sucesso")
        else:
            print("ID not Found")

      if(len(escolha) == 3): 
        user=cadastro_funcionario(escolha[0],escolha[2],escolha[1])
        logado = user
        print("Cadastro com Sucesso")
      else:
        print("voce escolheu sair")
     
      main(logado)

    if(escolha == '3'):
      main()

  if(escolha == '2'):

    #saber se existe produto
    if(Produtos.flag):
      showProducts()
      #saber se é cliente
      if is_cliente(logado):
        escolha=input(compra_step1)
        user = id_existe(escolha)
        if(user and escolha != 0 and is_funcionario(user)):
           
          nome_prod=input("Infome o nome do produto: ")
          qtd=int(input(compra_venda_step2))
          produto = tem_qtd_disponivel(nome_prod,qtd)
          if(produto):
            venda_produtos(produto,qtd)
          else:
            print("Quantidade maior do que cadastrada")

      if is_funcionario(logado):
        escolha=input(venda_step1)
        #recebe id
        user = id_existe(escolha)
        if(user and escolha != 0 and is_cliente(user)):
          nome_prod=input("Infome o nome do produto: ")
          qtd=int(input(compra_venda_step2))
          produto = tem_qtd_disponivel(nome_prod,qtd)
          if(produto):
            venda_produtos(produto,qtd)
          else:
            print("Quantidade maior do que cadastrada")
      main(logado)
    else:
      print("Não ha produtos cadastrados, é recomendado ir para Administração")
      main(logado)

  if(escolha == '3'):
  
    print("Bem vindo aos primeiros passos \n Primeiramente é preciso cadastrar um Funcionario \n")


    #cadastro do Funcionario
    escolha=input("""  Para efetuar cadastro insira seu nome, sua ocupação e seu identificador unico - ID (separando-os por virgula ',')
                        ex: Wellington,developer,123 \n""").split(',')
    user=cadastro_funcionario(escolha[0],escolha[1],escolha[2])
    logado = user
    print("\n Cadastro do Funcionario realizado com sucesso, agora iremos cadastrar um produto ")
    nomeProd = input("Digite o nome do produto: ")
    qtdProd = int(input("Digite a quantidade em estoque: "))


    #cadastro de Produtos
    cadastrado = cadastro_produtos(nomeProd, qtdProd)
    if cadastrado:
      print('Produto cadastrado com sucesso!')
    else:
      print('Ocorreu um erro ao cadastrar o produto, verifique se o produto ja não esta cadastrado')
    print("Muito bem agora só falta o cadastro do cliente")


    #cadastro de Clientes
    escolha=input("""\n  Para efetuar cadastro insira seu nome, sua ocupação e seu identificador unico (separando-os por virgula ',')
                        ex: Wellington,123 \n""").split(',')
    user=cadastro_usuario(escolha[0],escolha[1])
    logado = user
  
    print("Cadastro do Cliente realizado com sucesso, agora ja podemos entrar no sistema")
 
    main(logado)

  if(escolha == '4'):
    print("Area adm")
    if is_funcionario(logado):
      produto_menu = input("""Digite
      1 - Cadastrar
      2 - Buscar
      3 - Alterar
      4 - Excluir
      5 - Listar Produtos
      0 - Voltar
      """)
      if produto_menu == '1':
        nomeProd = input("Digite o nome do produto: ")
        qtdProd = int(input("Digite a quantidade em estoque: "))

        cadastrado = cadastro_produtos(nomeProd, qtdProd)
        if cadastrado:
          print('Produto cadastrado com sucesso!')
        else:
          print('Ocorreu um erro ao cadastrar o produto, verifique se o produto ja não esta cadastrado')
          
      elif produto_menu == '2':
        nome = input('Digite o nome do produto: ')
        produto = Buscar_produto(nome)
        if produto: 
          print("Nome: ", produto.nome)
          print("Quantidade: ", produto.quantidade)
        else:
          print('Não possivel encontrar esse produto!')

      elif produto_menu == '3':
        nome = input('Digite o nome do produto: ')
        produto = Buscar_produto(nome)
        if produto:
          produto.quantidade = int(input('Dige a nova quantidade em estoque: '))
          print('As alterações foram salvas com sucesso!')
        else:
          print('Não possivel encontrar esse produto!')

      elif produto_menu == '4':
        nome = input('Digite o nome do produto: ')
        produto = Buscar_produto(nome)
        if produto:
          excluir_produto(produto)
          print('O produto foi excluido com sucesso!')
          Produtos.flag=False
        else:
          print('Não possivel encontrar esse produto!')
      elif produto_menu == '5':
        showProducts()
    else:
      print("Voce não tem autorização para entrar aqui, Logue nomentere como Funcionario")
    main(logado)
    #confere se logar é instancia de funcionario: se sim
    #CRUD de produtos

        
main()
