import csv
import socket 

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
        #Insere um Dado no csv
        if(recebe.decode()[1]=='U'):
            pass #insere um usuario no csv
        if(recebe.decode()[0]=='P'):
            pass #insere um produto no csv
    if(recebe.decode()[0]=='R'):
        #Requisita um dado no csv
        if(recebe.decode()[1]=='U'): 
            pass  #Buscar usuarios e enviar com con.send("Dado".encode())
        if(recebe.decode()[1]=='P'):
            pass  #Buscar produto e enviar com con.send("Dado".encode()) 
    print(recebe.decode())

    con.send("Dado".encode())
serv_socket.close()