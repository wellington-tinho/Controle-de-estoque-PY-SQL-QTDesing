from ..model.Estoque import *
from ..model.Funcionario import *
from ..view.menu import menu
from ..model.Pessoa import *
from ..model.Produto import *
from ..main import main 

from ..controller.Database_Pessoas import Database_Pessoas

def login_cadastro(logado):
  _,menu_escolha_user,menu_entrar_cliente,menu_entrar_Funcionario,_,_,_ = menu()
  #escolha se é cliente ou Funcionario 1,2
  escolha=input(menu_escolha_user)

  #login_Cliente
  if(escolha == '1'):
      escolha=input(menu_entrar_cliente).split(',')

      #login
      if (len(escolha) == 1):
          user=Database_Pessoas.id_existe(escolha[0],Database_Pessoas. clientes)
          if(Database_Pessoas.is_cliente(user)):
            logado = user
            print("Logado com Sucesso")
          else:
              print("ID not Found")

      #cadastro
      if (len(escolha) == 2): 
        user=Database_Pessoas.cadastro_usuario(escolha[0],escolha[1])
        logado = user
        print("Cadastro com Sucesso")
      else:
        print("voce escolheu sair")
      
      main(logado)

  #login_funcionario
  if(escolha == '2'):
    escolha=input(menu_entrar_Funcionario).split(',')
    

    if(len(escolha) == 2):
      user=Database_Pessoas.id_existe(escolha[1], Database_Pessoas.funcionarios)
      if(Database_Pessoas.is_funcionario(user)):
        logado = user
        print("Logado com Sucesso")
      else:
          print("ID not Found")

    if(len(escolha) == 3):
      user=Database_Pessoas.cadastro_funcionario(escolha[0],escolha[2],escolha[1])
      logado = user
      print("Cadastro com Sucesso")
    else:
      print("voce escolheu sair")
    
    main(logado)

  if(escolha == '3'):
    main()
  else:
    exit()
