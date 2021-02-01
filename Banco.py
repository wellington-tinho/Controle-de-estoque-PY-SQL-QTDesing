import mysql.connector as mysql

class Banco:
    def __init__(self):
        """
        Função de iniciação do banco

        """

        connection = mysql.connect(host='localhost',db='banco',user='root',passwd='1234')
        cursor = connection.cursor()
        # sql = """ CREATE TABLE IF NOT EXISTS usuarios_senha(id integer AUTO_INCREMENT PRIMARY KEY, nome text NOT NULL,senha VARCHAR(32), email text NOT NULL);"""

        funcionarios = """ CREATE TABLE IF NOT EXISTS funcionarios(cpf VARCHAR(255) PRIMARY KEY, nome VARCHAR(255) NOT NULL, ocupacao VARCHAR(255) NOT NULL, senha VARCHAR(32));"""
        clientes =     """ CREATE TABLE IF NOT EXISTS clientes(cpf VARCHAR(255) PRIMARY KEY, nome VARCHAR(255) NOT NULL, ocupacao VARCHAR(255) NOT NULL, senha VARCHAR(32));"""
        produtos =     """ CREATE TABLE IF NOT EXISTS produtos(nome VARCHAR(255) NOT NULL, quantidade VARCHAR(32) NOT NULL);"""
        cursor.execute(funcionarios)
        cursor.execute(clientes)
        cursor.execute(produtos)
        connection.commit()
        connection.close()



    def insert_Funcionario(self,nome:str,cpf:str,ocupacao:str,senha:str):
        """
        Função resonsavel pelo cadastro do funcionário no banco.

        :param NomeFuncionario: Nome do funcionario a ser cadastrado -> type(str)
        :param CPF: CPF do funcionário -> type(str)
        :param ocupação: Cargo funcionario -> type(str)
        :param Senha: Senha do funcionario -> type(str)


        :return: A função retorna uma true se funcionário cadastrado, caso contrario ela retorna uma
        false
        """
        try:
            connection = mysql.connect(host='localhost',db='banco',user='root',passwd='1234')
            cursor = connection.cursor()

            cursor.execute('INSERT INTO funcionarios(cpf,nome,ocupacao,senha) VALUES (%s,%s,%s,MD5(%s))',(cpf,nome,ocupacao,senha))
            connection.commit()
            connection.close()
            return True
        except Exception as e:
            return False

    def insert_cliente(self,nome:str,cpf:str,ocupacao:str,senha:str):
        """
        Função resonsavel pelo cadastro do clientes no banco.

        :param Nome: Nome do clientes a ser cadastrado -> type(str)
        :param CPF: CPF do clientes -> type(str)
        :param ocupação: Cargo do clientes -> type(str)
        :param Senha: Senha do clientes -> type(str)


        :return: A função retorna uma true se clientes cadastrado, caso contrario ela retorna uma
        false
        """
        try:
            connection = mysql.connect(host='localhost',db='banco',user='root',passwd='1234')
            cursor = connection.cursor()

            cursor.execute('INSERT INTO clientes(cpf,nome,ocupacao,senha) VALUES (%s,%s,%s,MD5(%s))',(cpf,nome,ocupacao,senha))
            connection.commit()
            connection.close()
            return True
        except Exception as e:
            return False

    def insert_produto(self,nome:str,quantidade:int):
        """
        Função de cadastro de produtos no banco.

        :param NomeDoProduto: Nome do produto para ser cadastrado -> type(str)
        :param Quantidade: Quantidade do produto cadastrado -> type(str)

        :return: A função retorna o nome do produto quando o produto foi cadastrado, caso contrario
        o retorno é uma lista vazia.
        """
        try:
            connection = mysql.connect(host='localhost',db='banco',user='root',passwd='1234')
            cursor = connection.cursor()

            cursor.execute('INSERT INTO produtos(nome,quantidade) VALUES (%s,%s)',(nome,quantidade))
            connection.commit()
            connection.close()
            return True
        except Exception as e:
            return False

    def Login(self,cpf:str,senha:str,ocupacao:str):
        """
        Função responsável para a verificar se existe o funcionário solicitado com aquela senha.

        :param CPF: CPF do funcionário -> type (str)
        :param Senha: Senha do funcionário -> type (str)
        :param ocupação: Cargo do clientes -> type(str)


        :return: A função retorna um dicionário se encontrar aquele funcionário com aquela senha,
        caso contrario ele retorna uma lista vazia.
        """
        try:
            connection = mysql.connect(host='localhost',db='banco',user='root',passwd='1234')
            cursor = connection.cursor()
            if(ocupacao == 'cliente'):
                resultado = cursor.execute('SELECT * FROM cliente WHERE cpf= %s AND senha=MD5(%s)',(cpf,senha))
                teste = resultado.fetchall()
                connection.commit()
                connection.close()
                return teste

            if(ocupacao=='funcionario'):
                resultado = cursor.execute('SELECT * FROM funcionario WHERE cpf= %s AND senha=MD5(%s)',(cpf,senha))
                teste = resultado.fetchall()
                connection.commit()
                connection.close()
                return teste  
            return False
        except Exception as e:
            return []
        
    def exibe_produtos(self):
        """
        Esta função retorna todos os produtos cadastrado no banco.

        :return: A função retorna uma lista com todos os dados dos produtos
        cadastrados, caso contrario ela retorna uma lista vazia.
        """
        try:
            connection = mysql.connect(host='localhost',db='banco',user='root',passwd='1234')
            cursor = connection.cursor()
            cursor.execute('SELECT * from produtos ')

            resultado = cursor.fetchall()

            connection.commit()
            connection.close()
            return resultado
        except Exception as e:
            return []

    def ExcluiProduto(self,NomeDoProduto:str):
        """
        Função responsável por exclusão de um produto em uma loja determinada.

        :param NomeDoProduto: Nome do produto que deseja excluir -> type(str)
        :param id_loja: Identificador da loja na qual objetiva excluir o produto -> type(str)

        :return: A função retorna a String Exclusão quando foi o produto foi excluido do banco, caso contrário a função
        retorna None.
        """

        connection = mysql.connect(host='localhost',db='banco',user='root',passwd='1234')
        cursor = connection.cursor()
        sql = "DELETE FROM produtos WHERE nome = '{}'".format(NomeDoProduto)
        cursor.execute(sql)
        connection.commit()
        connection.close()
        print("Produto excluido")
        

    def AlterarDadosDoProduto(self,NomeDoProduto:str,Quantidade:str,PrecoUnitario:str,IdentificadorProduto:str,IdentificadorLoja:str):
        """
        Função responsavel pela alteração dos dados do produto!

        :param NomeDoProduto: Novo nome do produto -> type(str)
        :param Quantidade: Nova quantidade para o produto -> type(str)
        :param PrecoUnitario: Novo preço unitario para o produto -> type(str)
        :param IdentificadorProduto: Identificador do produto que deve ter seus dados alterados -> type(str)
        :param IdentificadorLoja: identificador da loja onde possui um produto que deve ser alterado os valores -> type(str)


        :return: A função retorna o Nome do produto caso tenha conseguido fazer a alteração, caso contrario
        a função retorna uma lista vazia!
        """
        try:
            connection = mysql.connect(host='localhost',db='banco',user='root',passwd='1234')
            cursor = connection.cursor()
            sql1 = "UPDATE Produto SET NomeDoProduto = '{0}',Quantidade = '{1}', PrecoUnitario = '{2}' WHERE IdentificadorProduto = '{3}' AND IdentificadorLoja = '{4}'".format(NomeDoProduto,Quantidade,PrecoUnitario,IdentificadorProduto,IdentificadorLoja)
            cursor.execute(sql1)
            connection.commit()
            connection.close()
            return NomeDoProduto
        except Exception as e:
            return []


banco = Banco()

# for i in range(5):
#     print(banco.insert_produto('maça'+str(i),str(i)))

# print(banco.exibe_produtos())

# banco.ExcluiProduto('maça1')
print(banco.exibe_produtos())
print(banco.insert_Funcionario('wellington2','1234','dev','1234'))