import csv
import socket 
import csv
import pandas as pd

def insere_User(value):
    print("inserindo User",value.split(','))
    id_,Nome,Ocupacao,Senha=value.split(',')
    with open('Pessoa.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([f'{id_}', f'{Nome}', f'{Ocupacao}',f'{Senha}'])

def insere_Poduto(value):
    print("inserindo produto",value.split(','))
    Nome,Quantidade=value.split(',')
    with open('Produtos.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([f'{Nome}', f'{Quantidade}'])

def exibe_User(value):
    print('request =',value)
    with open('Pessoa.csv', 'r', newline='') as file:
        linhas = csv.reader(file, delimiter=';')
        lst = list(linhas)
        for i in lst:
            print("i=",i)
            if (i!=[]):
                dados = str(i[0]).split(',')
                if (value == (dados[0])):
                    return con.send(i[0].encode()) 
        return '<!FAlSE>'

def exibe_Produto(value):
    print('request =',value)
    with open('Produtos.csv', 'r', newline='') as file:
        linhas = csv.reader(file, delimiter=';')
        lst = list(linhas)
        for i in lst:
            print("i=",i)
            if (i!=[]):
                dados = str(i[0]).split(',')
                if (value == (dados[0])):
                    return con.send(i[0].encode()) 
        return '<!FAlSE>'

def lista_Produtos(value):
    print('request =',value)
    with open('Produtos.csv', 'r', newline='') as file:
        linhas = csv.reader(file, delimiter=';')
        return list(linhas)


def Remover_produto(nome):
    lst = []
    with open('Produtos.csv', 'r', newline='') as file:
        linhas = csv.reader(file)
        lst = list(linhas) 
        for i in lst:
            dados = str(i[0]).split(',')
            if (nome == (dados[0])):
                lst.remove(i)
    pd.DataFrame(lst).to_csv('Produtos.csv')


host = 'localhost'
port = 8000
addr = (host,port)
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #reinicializa socket
serv_socket.bind(addr) #define quais endereços podem se conectar
serv_socket.listen(10) #define limite
print("Aguardadndo conexão...")
con,cliente = serv_socket.accept()
print('conectando')
mensagem = ''

while (mensagem!='<sair>'):
    recebe = con.recv(1024)
    if (recebe.decode()[0]=='I'):
        if(recebe.decode()[1]=='U'):
            insere_User(recebe.decode()[2:]) #insere um usuario no csv
            con.send("Usuario cadastrado".encode()) 

        if(recebe.decode()[1]=='P'):
            insere_Poduto(recebe.decode()[2:])
            con.send("Produto cadastrado".encode()) 

    if(recebe.decode()[0]=='L'):
        #Lista um dado no csv
        if(recebe.decode()[1]=='U'): 
            dados = str(exibe_User(recebe.decode()[2:]))  #Buscar usuarios e enviar com con.send("Dado".encode())
            con.send(dados.encode())   
        if(recebe.decode()[1]=='P'):
            dados = str(exibe_Produto(recebe.decode()[2:])) #Buscar produto e enviar com con.send("Dado".encode())
            con.send(dados.encode())  
        if(recebe.decode()[1]=='A'):
            dados = str(lista_Produtos()) #Buscar produto e enviar com con.send("Dado".encode())
            con.send(dados)
            
    if(recebe.decode()[0]=='R'):
        #Remove dado no csv
        if(recebe.decode()[1]=='P'): 
            Remover_produto(recebe.decode()[2:])#Buscar usuarios e enviar com con.send("Dado".encode())
            con.send("Feito".encode()) 


    
serv_socket.close()