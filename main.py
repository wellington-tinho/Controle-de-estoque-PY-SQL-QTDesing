from Estoque import *
from Funcionario import *
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
from adm import Adm
from adm_adicionar import Adm_adicionar
from adm_exibir import Adm_exibir
from adm_remover import Adm_remover
from Banco import Banco

import mysql.connector as mysql
bd = Banco()
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
  # if is_funcionario(user):
  #   return f'Logado como funcionario: {user.nome}'
  # if is_cliente(user): 
  #   return f'Logado como Cliente: {user.nome}'
  # else:
  #   return 'Voce não esta logado'


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





logado = 'Não logado'
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
    
    # estoque.AttLista()



    #TELA HOME
    self.tela_home.pushButton_2.clicked.connect(self.abrirTelaCadastro)
    self.tela_home.pushButton_3.clicked.connect(self.abrirTelaCompra)
    self.tela_home.pushButton_4.clicked.connect(self.abrirTelaVenda)
    self.tela_home.pushButton_5.clicked.connect(self.abrirTelaADM)
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
    lista=[]
    for i in (bd.exibe_produtos()):
        lista.append(i[0])

    self.tela_compra.comboBox.addItems(lista)
    self.tela_compra.pushButton_8.clicked.connect(self.botaoCompra)
    self.tela_compra.pushButton_5.clicked.connect(self.botaoVoltar)

    #VENDER
    lista=[]
    for i in (bd.exibe_produtos()):
        lista.append(i[0])

    self.tela_vender.comboBox.addItems(lista)
    self.tela_vender.pushButton_8.clicked.connect(self.botaoVender)
    self.tela_vender.pushButton_5.clicked.connect(self.botaoVoltar)   
      
    #TELA_ADM
    self.tela_adm.pushButton_3.clicked.connect(self.abrirTelaADM_adicionar)
    self.tela_adm.pushButton_4.clicked.connect(self.abrirTelaADM_remover)
    self.tela_adm.pushButton_6.clicked.connect(self.abrirTelaADM_exibir)
    self.tela_adm.pushButton_7.clicked.connect(self.botaoVoltar)
    # self.tela_adm.pushButton

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
    lista=[]
    for i in (bd.exibe_produtos()):
        lista.append(str(i))
    self.tela_adm_exibir.listWidget.addItems(lista)

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
          bd.insert_cliente(nome,cpf,ocupacao,senha)
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
          bd.insert_Funcionario(nome,cpf,ocupacao,senha)
          QMessageBox.information(None,'StorageControl','Cadastro realizado')
          self.QtStack.setCurrentIndex(2)
          self.tela_cadastro.lineEdit_5.setText('')
          self.tela_cadastro.lineEdit_6.setText('')
          self.tela_cadastro.lineEdit_7.setText('')
          self.tela_cadastro.lineEdit_8.setText('')
      else:
        QMessageBox.information(None,'POOII','Todos os valores devem ser preenchidos') 

    elif not(self.tela_cadastro.radioButton.isChecked() and self.tela_cadastro.radioButton_2.isChecked()):
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

    
    cpf =       self.tela_login.lineEdit_5.text()
    senha =     self.tela_login.lineEdit_7.text()
      
  
    
    if (self.tela_login.radioButton.isChecked()):
      if(bd.Login(cpf,senha,'cliente')!=[] or bd.Login(cpf,senha,'cliente')!=False):
        nome = (bd.Login(cpf,senha,'cliente'))
        print(nome)
        if (nome == []):
            QMessageBox.information(None,'POOII','CPF não encontrado')
        else:
          self.tela_login.lineEdit_5.setText('')
          self.tela_login.lineEdit_7.setText('')
          nome=nome[1]
        

          setlogado(f'{nome},{cpf}')
          self.tela_login.label_9.setText('Olá '+logadocom())
          QMessageBox.information(None,'POOII',f'Bem vindo {nome}')
          self.QtStack.setCurrentIndex(0)
          self.tela_home.label_2.setText('Olá '+logadocom())

      
      
    if (self.tela_login.radioButton_2.isChecked()):
      if(bd.Login(cpf,senha,'funcionario')!=[] or bd.Login(cpf,senha,'funcionario')!=False):
        nome = (bd.Login(cpf,senha,'funcionario'))
        print(nome)
        if (nome == []):
            QMessageBox.information(None,'POOII','CPF não encontrado')
        else:
          self.tela_login.lineEdit_5.setText('')
          self.tela_login.lineEdit_7.setText('')
          nome=nome[1]
          setlogado(f'{nome},{cpf}')
          self.tela_login.label_9.setText('Olá '+logadocom())
          QMessageBox.information(None,'POOII',f'Bem vindo {nome}')
          self.QtStack.setCurrentIndex(0)
          self.tela_home.label_2.setText('Olá '+logadocom())
    elif (not(self.tela_login.radioButton.isChecked()) and not(self.tela_login.radioButton_2.isChecked())):
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
      self.tela_compra.comboBox.clear()
      lista=[]
      for i in (bd.exibe_produtos()):
          lista.append(i[0])
      self.tela_compra.comboBox.addItems(lista)

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
      lista=[]
      for i in (bd.exibe_produtos()):
          lista.append(i[0])
      self.tela_vender.comboBox.addItems(lista)
      
 
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
    if (produto):
      for i in (bd.exibe_produtos()):
        if(i[0]==produto):
          nome=i[0]
          qtd=int(i[1])- int(quantidade)
          if(qtd<0):
            QMessageBox.information(None,'POOII',f'Quantidade maior que Disponivel total {int(i[1])}')
          else:
            bd.exibe_produtos(nome)
            bd.insert_produto(nome,str(qtd))
          QMessageBox.information(None,'POOII',f'Operação concluida,  quantidade restante {qtd}')
      
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
    if (produto):
        for i in (bd.exibe_produtos()):
          if(i[0]==produto):
            nome=i[0]
            qtd=int(i[1])- int(quantidade)
            if(qtd<0):
              QMessageBox.information(None,'POOII',f'Quantidade maior que Disponivel total {int(i[1])}')
            else:
              bd.ExcluiProduto(nome)
              bd.insert_produto(nome,str(qtd))
            QMessageBox.information(None,'POOII',f'Operação concluida,  quantidade restante {qtd}')
        
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
      
      if(logadocom() != 'Não logado'):
        cpf= logadocom().split(',')
        cpf=cpf[1]
        connection = mysql.connect(host='localhost',db='banco',user='root',passwd='1234')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM funcionarios ")
        resultado = cursor.fetchall()
        connection.commit()
        connection.close()

        for i in resultado:
            if(i[0]==cpf):
                self.QtStack.setCurrentIndex(5)
        else:
          QMessageBox.information(None,'POOII','Voce precisa estar logado como funcionario')
        
       

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
      self.QtStack.setCurrentIndex(7)
      self.tela_adm_exclui.comboBox.clear()
      lista=[]
      for i in (bd.exibe_produtos()):
          lista.append(i[0])
      self.tela_adm_exclui.comboBox.addItems(lista)
    
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
      self.QtStack.setCurrentIndex(8)
      self.tela_adm_exibir.listWidget.clear()
      lista=[]
      for i in (bd.exibe_produtos()):
          lista.append(str(i))
      self.tela_adm_exibir.listWidget.addItems(lista)
    

    
  def botao_adc_item(self):
    produto =           self.tela_adm_add.lineEdit_6.text()
    quantidade =        self.tela_adm_add.lineEdit_5.text()
    if (produto != '' and quantidade !=''):
      if bd.insert_produto(produto,quantidade):
        QMessageBox.information(None,'POOII',f'Operação concluida, produto {produto} foi cadastrado com suceeso')
      else:
        QMessageBox.information(None,'POOII',f'Operação cancelada, produto {produto} já foi cadastrado no sistema')
    else:
        QMessageBox.information(None,'POOII',f'Erro, um ou mais campos não foram preenchidos')
    self.tela_adm_add.lineEdit_6.setText('')
    self.tela_adm_add.lineEdit_5.setText('')
  
  def botao_remover(self):
    produto=self.tela_adm_exclui.comboBox.currentText()
    if estoque.buscarProduto(produto):
      nome=estoque.buscarProduto(produto)
      bd.ExcluiProduto(produto)
      QMessageBox.information(None,'POOII',f'{nome} foi excuido com sucesso')


app = QApplication(sys.argv)
show_main = Main()
sys.exit(app.exec_())

