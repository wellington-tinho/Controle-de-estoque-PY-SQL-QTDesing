from Estoque import *
from Funcionario import *
from menu import menu
from Pessoa import *
from Produto import *

import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication, QFileDialog
from PyQt5.QtCore import QCoreApplication

from sign_up import Sign_Up
from login import Login
from home import Home
from comprar import Comprar
from vender import Vender




estoque = Estoque()

clientes = [
  Usuario("Joao", "1"), 
]

funcionarios = [
  Funcionario("Ricardo","Vendendor", "1"), 
]

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
    user=Usuario(nome,cpf)
    clientes.append(user)
    return user
  

  
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
  user=Funcionario(nome,ocupacao,cpf)
  funcionarios.append(user)
  return user


def id_existe(Id,lista):
  """
    Função que verifica se um valor enviado existe na lista enviada tambem.

    Parametros
    ___________
    Id : valor do type String
    lista : valor do type list

    Retornos
    __________
    returna um valor objeto instanciado na lista ou um boolean False caso não houver item na lista

    Exeções
    __________
    Sem exeções

    Exemplo
    __________
    for i in lista:
    if (i.id == Id):
      return i
    return False
    """   
  
  for i in lista:
    if (i.id == Id):
      return i
  return False

def mostra_login(user):
  """
  Função que verifica se um valor enviado existe na lista enviada tambem.

  Parametros
  ___________
  Id : valor do type String
  lista : valor do type list

  Retornos
  __________
  returna uma string exibindo se o usuario esta logado ou não

  Exeções
  __________
  Sem exeções

  Exemplo
  __________
  if is_funcionario(user):
    return f'Logado como funcionario: {user.nome}'
  if is_cliente(user): 
    return f'Logado como Cliente: {user.nome}'
  else:
    return 'Voce não esta logado'

  """   
  if is_funcionario(user):
    return f'Logado como funcionario: {user.nome}'
  if is_cliente(user): 
    return f'Logado como Cliente: {user.nome}'
  else:
    return 'Voce não esta logado'



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



logado="Não logado"
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
    
    #TELA HOME
    self.tela_home.pushButton_2.clicked.connect(self.abrirTelaCadastro)
    self.tela_home.pushButton_5.clicked.connect(self.botaoVoltar)

    self.tela_home.pushButton_3.clicked.connect(self.abrirTelaCompra)
    self.tela_home.pushButton_4.clicked.connect(self.abrirTelaVenda)

    self.tela_home.label_2.setText(logadocom())

    
    
    
    #TELA LOGIN
    self.tela_login.pushButton_8.clicked.connect(self.botaoLogar)
    self.tela_login.pushButton_5.clicked.connect(self.botaoVoltar)
    self.tela_login.label_9.setText(logadocom())

    

    #TELA CADASTRO
    self.tela_cadastro.pushButton.clicked.connect(self.abrirTelaLogin)
    self.tela_cadastro.pushButton_8.clicked.connect(self.botaoCadastra)
    self.tela_cadastro.pushButton_5.clicked.connect(self.botaoVoltar)
    self.tela_cadastro.label_9.setText(logadocom())


    #COMPRAR
    estoque.AttLista()
    self.tela_compra.comboBox.addItems(estoque.allprodutos())
    self.tela_compra.pushButton_8.clicked.connect(self.botaoCompra)
    self.tela_compra.pushButton_5.clicked.connect(self.botaoVoltar)

    #VENDER
    estoque.AttLista()
    self.tela_vender.comboBox.addItems(estoque.allprodutos())
    self.tela_vender.pushButton_8.clicked.connect(self.botaoVender)
    self.tela_vender.pushButton_5.clicked.connect(self.botaoVoltar)   
      #TELA HOME


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
    if not(self.tela_cadastro.radioButton.isChecked() and self.tela_cadastro.radioButton_2.isChecked()):
      QMessageBox.information(None,'POOII','Voce deve escolher entre Cliente ou Funcionario')

    if (self.tela_cadastro.radioButton.isChecked()):
      if not(nome == '' or ocupacao == '' or cpf == '' or senha == ''):
          cadastro_usuario(nome,ocupacao,cpf,senha)
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
          cadastro_funcionario(nome,ocupacao,cpf,senha)
          QMessageBox.information(None,'StorageControl','Cadastro realizado')
          self.QtStack.setCurrentIndex(2)
          self.tela_cadastro.lineEdit_5.setText('')
          self.tela_cadastro.lineEdit_6.setText('')
          self.tela_cadastro.lineEdit_7.setText('')
          self.tela_cadastro.lineEdit_8.setText('')
      else:
        QMessageBox.information(None,'POOII','Todos os valores devem ser preenchidos')              

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
      user=id_existe(cpf, clientes)
      if(is_cliente(user)):
        self.tela_login.lineEdit_5.setText('')
        self.tela_login.lineEdit_7.setText('')
        self.tela_login.lineEdit_8.setText('')

        setlogado(user.nome)
        self.tela_login.label_9.setText('Olá '+logadocom())
        QMessageBox.information(None,'POOII',f'Bem vindo {user.nome}')
        self.QtStack.setCurrentIndex(0)
        self.tela_home.label_2.setText('Olá '+user.nome)

      else:
          QMessageBox.information(None,'POOII','CPF não encontrado')
      
    if (self.tela_login.radioButton_2.isChecked()):
      user=id_existe(cpf, funcionarios)
      if(is_funcionario(user)):
        setlogado(user.nome)
        self.tela_login.label_9.setText('Olá '+logadocom())
        QMessageBox.information(None,'POOII',f'Bem vindo {user.nome}')
        self.QtStack.setCurrentIndex(0)
        self.tela_home.label_2.setText('Olá '+user.nome)

      else:
          QMessageBox.information(None,'POOII','CPF não encontrado')

    # if not(self.tela_cadastro.radioButton.isChecked() and self.tela_cadastro.radioButton_2.isChecked()):
    else:
        QMessageBox.information(None,'POOII','Voce deve escolher entre Cliente ou Funcionario')

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
    self.tela_compra.label_9.setText(logadocom())
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
    self.tela_vender.label_9.setText(logadocom())
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




app = QApplication(sys.argv)
show_main = Main()
sys.exit(app.exec_())

