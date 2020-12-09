import repackage
repackage.up(3)

from ..view.menu import *
from ..model.Estoque import *
from ..model.Pessoa import *
from ..model.Produto import *
from ..controller.login_cadastro import *
from ..controller.compra_venda import *
from ..controller.administracao import *
from ..controller.primeira_vez import *



def main(logado=False):
  estoque = Estoque()
  home_menu,_,_,_,_,_,_ = menu()

  logado=logado

  print("_______________________________________________________________________________ \n", Database_Pessoas.mostra_login(logado))
  escolha=input(home_menu)

  #thead_escolha_1
  if(escolha == '1'):
    login_cadastro(logado)
    
  if(escolha == '2'):
    compra_venda(logado,estoque)
 
  if(escolha == '3'):
    primeira_vez(estoque)

  if(escolha == '4'):
    administracao(logado,estoque)
    
main()