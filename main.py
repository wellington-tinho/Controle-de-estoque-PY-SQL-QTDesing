# import threading # biblioteca para threads

# from testes import conec

# thread = threading.Thread(target=conec.__init__(), args=())
# thread.start()
from Estoque import *
from Funcionario import *
from Pessoa import *
from Produto import *

import sys
import socket
#ip = input('Digite i ip de conexão')
ip = 'localhost'
port = 8000
addr = ((ip,port)) # define a tupla de endereço
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(addr) #realiza conexao
mensagem = ''

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication, QFileDialog
from PyQt5.QtCore import QCoreApplication

# from teste_1 import exemplo
from sign_up import Sign_Up
from login import Login
from home import Home
from comprar import Comprar
from vender import Vender
from adm import Adm
from adm_adicionar import Adm_adicionar
from adm_exibir import Adm_exibir
from adm_remover import Adm_remover


estoque = Estoque()

# clientes = [
#   Usuario("Joao", "1"), 
# ]

# funcionarios = [
#   Funcionario("Ricardo","Vendendor", "1"), 
# ]



def is_funcionario(pessoa):
    """
      Função que verifica se objeto enviado como parametro é um objeto instaciado da classe funcionario

      Parametros
      ___________
      pessoa : valor do type <class '__main__.Funcionario'>

      
      Retornos
      __________
      returna um valor booleano. 

      Exeções
      __________
      Sem exeções

      Exemplo
      __________
      return isinstance(pessoa, Funcionario)

      """   
    return isinstance(pessoa, Funcionario)

def is_cliente(pessoa):
  """
    Função que verifica se objeto enviado como parametro é um objeto instaciado da classe Cliente

    Parametros
    ___________
    pessoa : valor do type <class '__main__.Cliente'>
    
    Retornos
    __________
    returna um valor booleano. 

    Exeções
    __________
    Sem exeções

    Exemplo
    __________
    return (isinstance(pessoa, Usuario) and not(is_funcionario(pessoa)))
  """   
  return (isinstance(pessoa, Usuario) and not(is_funcionario(pessoa)))

def cadastro_usuario(nome,ocupacao,cpf,senha):

    """
    Função que cadastra um Usuario no sistema 

    Parametros
    ___________
    nome : valor do type String
    ocupacao : valor do type String
    cpf : valor do type String
    senha : valor do type String

    Retornos
    __________
    returna um valor objeto da classe usuario 

    Exeções
    __________
    Sem exeções

    Exemplo
    __________
    user=Usuario(nome,cpf)
    clientes.append(user)
    return user
    """   
    mensagem = f"IU{cpf},{nome},{ocupacao},{senha}"
    client_socket.send(mensagem.encode()) #envia mensagem
    print(client_socket.recv(1024).decode())
    # user=Usuario(nome,cpf)
    # clientes.append(user)
    # return user
    
def cadastro_funcionario(nome,ocupacao,cpf,senha):
  """
    Função que cadastra um Funcionario no sistema 

    Parametros
    ___________
    nome : valor do type String
    ocupacao : valor do type String
    cpf : valor do type String
    senha : valor do type String

    Retornos
    __________
    returna um valor objeto da classe Funcionario 

    Exeções
    __________
    Sem exeções

    Exemplo
    __________
    user=Funcionario(nome,ocupacao,cpf)
    funcionarios.append(user)
    return user
    """   
  mensagem = f"IU{cpf},{nome},{ocupacao},{senha}"
  client_socket.send(mensagem.encode()) #envia mensagem
  print(client_socket.recv(1024).decode())
  # user=Funcionario(nome,ocupacao,cpf)
  # funcionarios.append(user)
  # return user

# def id_existe(Id,lista):
  #   """
  #     Função que verifica se um valor enviado existe na lista enviada tambem.

  #     Parametros
  #     ___________
  #     Id : valor do type String
  #     lista : valor do type list

  #     Retornos
  #     __________
  #     returna um valor objeto instanciado na lista ou um boolean False caso não houver item na lista

  #     Exeções
  #     __________
  #     Sem exeções

  #     Exemplo
  #     __________
  #     for i in lista:
  #     if (i.id == Id):
  #       return i
  #     return False
  #     """   
    
  #   for i in lista:
  #     if (i.id == Id):
  #       return i
  #   return False

  # def mostra_login(user):
  #   """
  #   Função que verifica se um valor enviado existe na lista enviada tambem.

  #   Parametros
  #   ___________
  #   Id : valor do type String
  #   lista : valor do type list

  #   Retornos
  #   __________
  #   returna uma string exibindo se o usuario esta logado ou não

  #   Exeções
  #   __________
  #   Sem exeções

  #   Exemplo
  #   __________
  #   if is_funcionario(user):
  #     return f'Logado como funcionario: {user.nome}'
  #   if is_cliente(user): 
  #     return f'Logado como Cliente: {user.nome}'
  #   else:
  #     return 'Voce não esta logado'

  #   """   
  #   if is_funcionario(user):
  #     return f'Logado como funcionario: {user.nome}'
  #   if is_cliente(user): 
  #     return f'Logado como Cliente: {user.nome}'
  #   else:
  #     return 'Voce não esta logado'


class Ui_Main(QtWidgets.QWidget):
    """
  Class responsavel por herdar propriedades para executar telas do QTdesing

    ...
    
    Atributos
    ___________
     Não há


    Metodos
    ____________
    setupUi(self, Main)

  """   
    def setupUi(self, Main):
      """
      Função responsavel por executar telas da aplicação.
      ...

        Parametros
        ___________
        QtStack: QtWidgets.QStackedLayout()

        stack1: QtWidgets.QMainWindow() 
        stack2: QtWidgets.QMainWindow()
        stack0: QtWidgets.QMainWindow() 
        stack3: QtWidgets.QMainWindow() 
        stack4: QtWidgets.QMainWindow() 
        tela_home: Obj( Home() )
        tela_cadastro: Obj( Sign_Up() )
        tela_login: Obj( Login() )
        tela_compra: Obj( Comprar() )
        tela_vender: Obj( Vender() )

        Retornos
        __________
        Não há

        Exeções
        __________
        Sem exeções

        Exemplo
        __________
        Main.setObjectName('main')
        Main.resize(640,480)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow() 
        self.stack1 = QtWidgets.QMainWindow() 
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow() 
        self.stack4 = QtWidgets.QMainWindow() 

        self.tela_home = Home()
        self.tela_home.setupUi(self.stack0)
        
        self.tela_cadastro = Sign_Up()
        self.tela_cadastro.setupUi(self.stack1)

        self.tela_login = Login()
        self.tela_login.setupUi(self.stack2)

        self.tela_compra = Comprar()
        self.tela_compra.setupUi(self.stack3)

        self.tela_vender = Vender()
        self.tela_vender.setupUi(self.stack4)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)


        """
      Main.setObjectName('main')
      Main.resize(640,480)

      self.QtStack = QtWidgets.QStackedLayout()

      self.stack0 = QtWidgets.QMainWindow()  #home
      self.stack1 = QtWidgets.QMainWindow()  #login
      self.stack2 = QtWidgets.QMainWindow()  #sigin
      self.stack3 = QtWidgets.QMainWindow()  #compra
      self.stack4 = QtWidgets.QMainWindow()  #venda
      self.stack5 = QtWidgets.QMainWindow()  #adm
      self.stack6 = QtWidgets.QMainWindow()  #adm-add
      self.stack7 = QtWidgets.QMainWindow()  #adm-exclui
      self.stack8 = QtWidgets.QMainWindow()  #exibe


      self.tela_home = Home()
      self.tela_home.setupUi(self.stack0)
      
      self.tela_cadastro = Sign_Up()
      self.tela_cadastro.setupUi(self.stack1)

      self.tela_login = Login()
      self.tela_login.setupUi(self.stack2)

      self.tela_compra = Comprar()
      self.tela_compra.setupUi(self.stack3)

      self.tela_vender = Vender()
      self.tela_vender.setupUi(self.stack4)

      self.tela_adm = Adm()
      self.tela_adm.setupUi(self.stack5)  #ad

      self.tela_adm_add = Adm_adicionar()
      self.tela_adm_add.setupUi(self.stack6)

      self.tela_adm_exclui = Adm_remover()
      self.tela_adm_exclui.setupUi(self.stack7)

      self.tela_adm_exibir = Adm_exibir()
      self.tela_adm_exibir.setupUi(self.stack8)
        
      self.QtStack.addWidget(self.stack0)
      self.QtStack.addWidget(self.stack1)
      self.QtStack.addWidget(self.stack2)
      self.QtStack.addWidget(self.stack3)
      self.QtStack.addWidget(self.stack4)
      self.QtStack.addWidget(self.stack5)
      self.QtStack.addWidget(self.stack6)
      self.QtStack.addWidget(self.stack7)
      self.QtStack.addWidget(self.stack8)




class gambiarra():
  def __init__(self,name):
    self.nome = name
logado =gambiarra("Não logado")

# logado = 'Não logado'
def logadocom():
  return logado

def setlogado(value):
  global logado
  logado = value
class Main(QMainWindow,Ui_Main):
  """
    Classe responsavel por todo o fluxo de execução do programa 

    ...

    Atributos
    ____________
    estoque: list
      lista de produtos que terá no sistema
  

    Metodos
    ______________
    __init__
      construtor da classe main
    
    abrirTelaCadastro
      Função responsavel pelo botao que direciona para tela de cadastro

    abrirTelaLogin
      Função responsavel pelo botao que direciona para tela de login

    botaoLogar
      Função responsavel por confirmar dados do login do usuario

    botaoCadastra
      Função responsavel pelo botao que finaliza a etapa do cadastro de cliente ou funcionario

    botaoVoltar
      Função responsavel pelo botao que direciona o programa para tela home

    abrirTelaCompra
      Função da tela home responsavel por abrir tela de compra

    abrirTelaVenda
      Função da tela home responsavel pelo botao que direciona para a tela de vendas

    botaoCompra
      Função responsavel pelo botao que confirma a compra na tela de compras

    botaoVender
      Função responsavel pelo botao que confirma a venda na tela de vendas
  """

  def __init__(self):
    """
    Contrutor da classe
    ...
    """
    super(Main,self).__init__()
    self.setupUi(self)
    
    estoque.AttLista()



    #TELA HOME
    self.tela_home.pushButton_2.clicked.connect(self.abrirTelaCadastro)
    self.tela_home.pushButton_3.clicked.connect(self.abrirTelaCompra)
    self.tela_home.pushButton_4.clicked.connect(self.abrirTelaVenda)
    self.tela_home.pushButton_5.clicked.connect(self.abrirTelaADM)
    self.tela_home.label_2.setText(logadocom().nome)

    
    #TELA LOGIN
    self.tela_login.pushButton_8.clicked.connect(self.botaoLogar)
    self.tela_login.pushButton_5.clicked.connect(self.botaoVoltar)
    self.tela_login.label_9.setText(logadocom().nome)

    

    #TELA CADASTRO
    self.tela_cadastro.pushButton.clicked.connect(self.abrirTelaLogin)
    self.tela_cadastro.pushButton_8.clicked.connect(self.botaoCadastra)
    self.tela_cadastro.pushButton_5.clicked.connect(self.botaoVoltar)
    self.tela_cadastro.label_9.setText(logadocom().nome)


    #COMPRAR
    self.tela_compra.comboBox.addItems(estoque.allprodutos())
    self.tela_compra.pushButton_8.clicked.connect(self.botaoCompra)
    self.tela_compra.pushButton_5.clicked.connect(self.botaoVoltar)

    #VENDER
    self.tela_vender.comboBox.addItems(estoque.allprodutos())
    self.tela_vender.pushButton_8.clicked.connect(self.botaoVender)
    self.tela_vender.pushButton_5.clicked.connect(self.botaoVoltar)   
      
    #TELA_ADM
    self.tela_adm.pushButton_3.clicked.connect(self.abrirTelaADM_adicionar)
    self.tela_adm.pushButton_4.clicked.connect(self.abrirTelaADM_remover)
    self.tela_adm.pushButton_6.clicked.connect(self.abrirTelaADM_exibir)
    self.tela_adm.pushButton_7.clicked.connect(self.botaoVoltar)
 
    #TELA_ADM_ADICIONA
    self.tela_adm_add.pushButton_8.clicked.connect(self.abrirTelaADM)
    self.tela_adm_add.pushButton_5.clicked.connect(self.botaoVoltar)
    self.tela_adm_add.pushButton_9.clicked.connect(self.botao_adc_item)
    

    #TELA_ADM_REMOVE
    self.tela_adm_exclui.pushButton_8.clicked.connect(self.botao_remover)
    self.tela_adm_exclui.pushButton_5.clicked.connect(self.botaoVoltar)
    self.tela_adm_exclui.pushButton_9.clicked.connect(self.abrirTelaADM)

    #TELA_ADM_EXIBI
    self.tela_adm_exibir.pushButton_5.clicked.connect(self.botaoVoltar)
    self.tela_adm_exibir.pushButton_8.clicked.connect(self.abrirTelaADM)
    self.tela_adm_exibir.listWidget.addItems(estoque.allprodutos_com_quantidade())

  def abrirTelaCadastro(self):
    """
         Função responsavel pelo botao que direciona para tela de cadastro
    ...
    """
    self.QtStack.setCurrentIndex(1)

  def abrirTelaLogin(self):
    """
    Função responsavel pelo botao que direciona para tela de login

    ...
    
    Retornos
    __________
    Não possui um retorno

    Exeções
    __________
    Sem exeções

    """
    self.QtStack.setCurrentIndex(2)

  def botaoCadastra(self):
    """
    Função responsavel pelo botao que finaliza a etapa do cadastro de cliente ou funcionario
    ...
  
    Retornos
    __________
    Não possui um retorno

    Exeções
    __________
    Sem exeções

    """
  
    nome =      self.tela_cadastro.lineEdit_8.text()
    ocupacao =  self.tela_cadastro.lineEdit_6.text()
    cpf =       self.tela_cadastro.lineEdit_5.text()
    senha =     self.tela_cadastro.lineEdit_7.text()

    if (self.tela_cadastro.radioButton.isChecked()):
      if not(nome == '' or ocupacao == '' or cpf == '' or senha == ''):
          # cadastro_usuario(nome,ocupacao,cpf,senha)
          mensagem = f"IU{cpf},{nome},{'Cliente'},{senha}"
          client_socket.send(mensagem.encode()) #envia mensagem


          QMessageBox.information(None,'StorageControl','Cadastro realizado')
          self.QtStack.setCurrentIndex(2)
          self.tela_cadastro.lineEdit_5.setText('')
          self.tela_cadastro.lineEdit_6.setText('')
          self.tela_cadastro.lineEdit_7.setText('')
          self.tela_cadastro.lineEdit_8.setText('')
      else:
          QMessageBox.information(None,'POOII','Todos os valores devem ser preenchidos')


    if (self.tela_cadastro.radioButton_2.isChecked()):
      if not(nome == '' or ocupacao == '' or cpf == '' or senha == ''):
          # cadastro_funcionario(nome,ocupacao,cpf,senha)
          mensagem = f"IU{cpf},{nome},{'Funcionario'},{senha}"
          client_socket.send(mensagem.encode()) #envia mensagem

          QMessageBox.information(None,'StorageControl','Cadastro realizado')
          self.QtStack.setCurrentIndex(2)
          self.tela_cadastro.lineEdit_5.setText('')
          self.tela_cadastro.lineEdit_6.setText('')
          self.tela_cadastro.lineEdit_7.setText('')
          self.tela_cadastro.lineEdit_8.setText('')
      else:
        QMessageBox.information(None,'POOII','Todos os valores devem ser preenchidos')

    else:
      # (self.tela_cadastro.radioButton.isChecked() and self.tela_cadastro.radioButton_2.isChecked()):
      QMessageBox.information(None,'POOII','Voce deve escolher entre Cliente ou Funcionario')              

  def botaoLogar(self):
    """
        Função responsavel por confirmar dados do login do usuario
        ...
  
      Retornos
      __________
      Não possui um retorno

      Exeções
      __________
      Sem exeções

    """

    nome =      self.tela_login.lineEdit_8.text()
    cpf =       self.tela_login.lineEdit_5.text()
    senha =     self.tela_login.lineEdit_7.text()
      
    
    if (self.tela_login.radioButton.isChecked()):
      mensagem = f"LU{cpf}"
      client_socket.send(mensagem.encode()) #envia mensagem
      dados = client_socket.recv(1024).decode().split(',')
      if(cpf,nome,senha==dados[0],dados[1],dados[3]):
        self.tela_login.lineEdit_5.setText('')
        self.tela_login.lineEdit_7.setText('')
        self.tela_login.lineEdit_8.setText('')

        setlogado(nome)
        self.tela_login.label_9.setText('Olá '+nome)
        QMessageBox.information(None,'POOII',f'Bem vindo {nome}')
        self.QtStack.setCurrentIndex(0)
        self.tela_home.label_2.setText('Olá '+nome)

      else:
          QMessageBox.information(None,'POOII','valores incorretos encontrado')
      
    if (self.tela_login.radioButton_2.isChecked()):
      mensagem = f"LU{cpf}"
      client_socket.send(mensagem.encode()) #envia mensagem
      dados = client_socket.recv(1024).decode().split(',')
      if(cpf,nome,senha==dados[0],dados[1],dados[3]):
        self.tela_login.lineEdit_5.setText('')
        self.tela_login.lineEdit_7.setText('')
        self.tela_login.lineEdit_8.setText('')

        setlogado(nome)
        self.tela_login.label_9.setText('Olá '+nome)
        QMessageBox.information(None,'POOII',f'Bem vindo {nome}')
        self.QtStack.setCurrentIndex(0)
        self.tela_home.label_2.setText('Olá '+nome)

      else:
          QMessageBox.information(None,'POOII','valores incorretos encontrado')

  def botaoVoltar(self):
    """
      Função responsavel pelo botao que direciona o programa para tela home
  
    Retornos
    __________
    Não possui um retorno

    Exeções
    __________
    Sem exeções
  
    ...
    """
    self.QtStack.setCurrentIndex(0)

  def abrirTelaCompra(self):
    """
    Função da tela home responsavel por abrir tela de compra
    ...
  
    Retornos
    __________
    Não possui um retorno

    Exeções
    __________
    Sem exeções

    """
    if self.tela_home.label_2.text() == "Não logado":
      QMessageBox.information(None,'POOII','Voce precisa logar para completar essa etapa')
    else:
      self.QtStack.setCurrentIndex(3)
      self.tela_compra.comboBox.clear()
      self.tela_compra.comboBox.addItems(estoque.allprodutos())

  def abrirTelaVenda(self):
    """
    Função da tela home responsavel pelo botao que direciona para a tela de vendas
    ...
  
    Retornos
    __________
    Não possui um retorno

    Exeções
    __________
    Sem exeções

    """
    if self.tela_home.label_2.text() == "Não logado":
      QMessageBox.information(None,'POOII','Voce precisa logar para completar essa etapa')
    else:
      self.QtStack.setCurrentIndex(4)
      self.tela_vender.comboBox.clear()
      self.tela_vender.comboBox.addItems(estoque.allprodutos())
      
  def botaoCompra(self):
    """
    Função responsavel pelo botao que confirma a compra na tela de compras
    ...
  
    Retornos
    __________
    Não possui um retorno

    Exeções
    __________
    Sem exeções

    """
    self.tela_compra.label_9.setText(logadocom().nome)
    produto=self.tela_compra.comboBox.currentText()
    quantidade = self.tela_compra.lineEdit_5.text()
    produto = estoque.buscarProduto(produto)
    if (produto):
      print(produto,quantidade)
      if venda_produtos(produto,quantidade):
        estoque.AttLista()
        QMessageBox.information(None,'POOII',f'Operação concluida,  quantidade restante {estoque.qtd(produto)}')
      else:
        QMessageBox.information(None,'POOII',f'Quantidade maior que Disponivel total {estoque.qtd(produto)}')
    else:
      QMessageBox.information(None,'POOII','Foi vendido todo estoque desse produto')
    self.QtStack.setCurrentIndex(0)
    
  def botaoVender(self):
    """
    Função responsavel pelo botao que confirma a venda na tela de vendas
    ...
  
    Retornos
    __________
    Não possui um retorno

    Exeções
    __________
    Sem exeções

    """
    self.tela_vender.label_9.setText(logadocom().nome)
    produto=self.tela_vender.comboBox.currentText()
    quantidade = self.tela_vender.lineEdit_5.text()
    produto = estoque.buscarProduto(produto)
    if (produto):
      print(produto,quantidade)
      if venda_produtos(produto,quantidade):
        estoque.AttLista()
        QMessageBox.information(None,'POOII',f'Operação concluida,  quantidade restante {estoque.qtd(produto)}')
      else:
        QMessageBox.information(None,'POOII',f'Quantidade maior que Disponivel total {estoque.qtd(produto)}')
    else:
      QMessageBox.information(None,'POOII','Foi comprado todo estoque desse produto')
    self.QtStack.setCurrentIndex(0)

  def abrirTelaADM(self):
      """
      Função de varias telas responsavel pelo botao que direciona para a tela do administrador
      ...
    
      Retornos
      __________
      Não possui um retorno

      Exeções
      __________
      Sem exeções

      """
      if self.tela_home.label_2.text() == "Não logado":
        QMessageBox.information(None,'POOII','Voce precisa logar para completar essa etapa')
      else:
        self.QtStack.setCurrentIndex(5)
      
      # if is_funcionario(logadocom()):
      #   self.QtStack.setCurrentIndex(5)
      # else:
      #   QMessageBox.information(None,'POOII','Voce precisa estar logado como funcionario')

  def abrirTelaADM_adicionar(self):
      """
      Função de varias telas responsavel pelo botao que direciona para a tela de adicionar do administrador
      ...
    
      Retornos
      __________
      Não possui um retorno

      Exeções
      __________
      Sem exeções

      """
      self.QtStack.setCurrentIndex(6)
    
  def abrirTelaADM_remover(self):
      """
      Função de varias telas responsavel pelo botao que direciona para a tela remover do administrador
      ...
    
      Retornos
      __________
      Não possui um retorno

      Exeções
      __________
      Sem exeções

      """
      mensagem = f"LA"
      client_socket.send(mensagem.encode()) #envia mensagem
      array=client_socket.recv(1024)
      print(array)
      self.QtStack.setCurrentIndex(7)
      self.tela_adm_exclui.comboBox.clear()
      self.tela_adm_exclui.comboBox.addItems(array)
    
  def abrirTelaADM_exibir(self):
      """
      Função de varias telas responsavel pelo botao que direciona para a tela exibir do administrador
      ...
    
      Retornos
      __________
      Não possui um retorno

      Exeções
      __________
      Sem exeções

      """
      mensagem = f"LA"
      client_socket.send(mensagem.encode()) #envia mensagem
      array=client_socket.recv(1024)
      print(array)
      self.QtStack.setCurrentIndex(8)
      self.tela_adm_exibir.listWidget.clear()
      self.tela_adm_exibir.listWidget.addItems(array)
    
  def botao_adc_item(self):
    produto =           self.tela_adm_add.lineEdit_6.text()
    quantidade =        self.tela_adm_add.lineEdit_5.text()
  

    if (produto != '' and quantidade !=''):
        mensagem = f"IP{produto},{quantidade}"
        client_socket.send(mensagem.encode()) #envia mensagem
        print(client_socket.recv(1024).decode())
      
    #   if estoque.cadastrarProduto(produto,int(quantidade)):

    #     estoque.AttLista()
    #     QMessageBox.information(None,'POOII',f'Operação concluida, produto {produto} foi cadastrado com suceeso')
    #   else:
    #     QMessageBox.information(None,'POOII',f'Operação cancelada, produto {produto} já foi cadastrado no sistema')
    # else:
        QMessageBox.information(None,'POOII',f'Erro, um ou mais campos não foram preenchidos')
    self.tela_adm_add.lineEdit_6.setText('')
    self.tela_adm_add.lineEdit_5.setText('')
  
  def botao_remover(self):
    produto=self.tela_adm_exclui.comboBox.currentText()
    mensagem = f"LP{produto}"
    client_socket.send(mensagem.encode()) #envia mensagem
    (client_socket.recv(1024).decode())
    if (client_socket.recv(1024).decode() != '<!FAlSE>'):
      mensagem = f"RP{produto}"
      client_socket.send(mensagem.encode()) #envia mensagem
      print(client_socket.recv(1024).decode())
      # nome=estoque.buscarProduto(produto)
      # estoque.exluirProduto(produto)
      QMessageBox.information(None,'POOII',f'{produto} foi excuido com sucesso')


app = QApplication(sys.argv)
show_main = Main()
sys.exit(app.exec_())

