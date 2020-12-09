from ..model.Estoque import *
from ..model.Funcionario import *
from ..model.Pessoa import *
from ..model.Produto import *
from ..controller.login_cadastro import *
from ..controller.compra_venda import *
from ..controller.administracao import *
from ..controller.primeira_vez import *

from ..controller.Database_Pessoas import Database_Pessoas



class Database_Pessoas():
    def __init__(self):
        self.clientes =[
            Usuario("Joao", "1"), 
            Usuario("Maria", "4"), 
            Usuario("Pedro", "232")
        ]
        self.funcionarios = [
            Funcionario("Ricardo","Vendendor", "1"), 
            Funcionario("Paula","Vendendor" ,"4"), 
            Funcionario("Maria","Vendendor", "232")
        ]

    def is_funcionario(pessoa):
        return isinstance(pessoa, Funcionario)

    def is_cliente(pessoa):
        return (isinstance(pessoa, Usuario) and not(Database_Pessoas.is_funcionario(pessoa)))

    def cadastro_usuario(self,nome,Id):
        user=Usuario(nome,Id)
        self.clientes.append(user)
        return user
    
    def cadastro_funcionario(self,nome,Id,ocupacao):
        user=Funcionario(nome,ocupacao,Id)
        self.funcionarios.append(user)
        return user


    def id_existe(Id,lista):
        for i in lista:
            if (i.id == Id):
                return i
        return False

    def mostra_login(user):
        if Database_Pessoas.is_funcionario(user):
            return f'Logado como funcionario: {user.nome}'

        if Database_Pessoas.is_cliente(user): 
            return f'Logado como Cliente: {user.nome}'
        else:
            return 'Voce não esta logado'