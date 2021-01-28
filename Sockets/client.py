# import socket
# #ip = input('Digite i ip de conexão')
# ip = 'localhost'
# port = 8000
# addr = ((ip,port)) # define a tupla de endereço
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket.connect(addr) #realiza conexao
# mensagem = ''


# menu = """
#     1 - cadastrar novo user
#     2 - cadastrar novo produto
#     3 - visualizar users
#     4 - visualizar produtos 
#     <sair> - SAIR
#     """

# while (mensagem!='<sair>'):
#     opc = input(menu)
#     if(opc=='1'):
#         nome =input("Digite nome:  ")
#         _id =input("Digite _id,:  ")
#         senha= input("Digite senha:  ")
#         ocupacao=input("Digite ocupacao:  ")
#         # user=Usuario(nome,_id,senha,ocupacao)
#         mensagem = f"IU{_id},{nome},{ocupacao},{senha}"
#         client_socket.send(mensagem.encode()) #envia mensagem
#         print(client_socket.recv(1024).decode())

       
#     if(opc=='2'):
#         nome=input("Digite nome: ")
#         quantidade=input("Digite quantidade: ")
#         # produto=Produtos(nome,quantidade)
#         mensagem = f"IP{nome},{quantidade}"
#         client_socket.send(mensagem.encode()) #envia mensagem
#         print(client_socket.recv(1024).decode())


#     if(opc=='3'):
#         id_=input("Digite id: ")
#         print("listar users: ")
#         mensagem = f"LU{id_}"
#         client_socket.send(mensagem.encode()) #envia mensagem
#         print(client_socket.recv(1024).decode())

 
#     if(opc=='4'):
#         nome=input("Digite nome: ")
#         print("listar produto: ")
#         mensagem = f"LP{nome}"
#         client_socket.send(mensagem.encode()) #envia mensagem
#         print(client_socket.recv(1024).decode())
#     if (opc == '<sair>'):
#         mensagem='<sair>'


# client_socket.close() #fecha conexão
