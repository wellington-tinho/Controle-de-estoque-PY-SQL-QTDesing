# import csv
# import pandas as pd

# with open('Pessoa.csv', 'a', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['ID_______2', "Nome", "Ocupacao","Senha"])
 

# lst = []
# with open('Pessoa.csv', 'r', newline='') as file:
#     linhas = csv.reader(file)
#     lst = list(linhas) 
#     for i in lst:
#         dados = str(i[0]).split(',')
#         if ('ID_______' == (dados[0])):
#             lst.remove(i)
#   pd.DataFrame(lst).to_csv('Pessoa.csv')

#
# import csv

# lst = []
# with open('Pessoa.csv', 'r', newline='') as file:
#     linhas = csv.reader(file, delimiter=';')
#     lst = list(linhas)
#     for i in lst:
#         dados = str(i[0]).split(',')
#         if ('ID_______' == (dados[0])):
#             lst.remove(i)

   
   

# with open('Pessoa.csv', 'w') as file:
#     writer = csv.writer(file)
#     writer.writerows(lst)

# def insere_Poduto(value):
#     print("inserindo",value.split(','))
#     Nome,Quantidade=value.split(',')
#     with open('Produtos.csv', 'a', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow([f'{Nome}', f'{Quantidade}'])

# a=input(": ")
# insere_Poduto(a)


# def exibe_Produto(value):
#     with open('Produtos.csv', 'r', newline='') as file:
#         linhas = csv.reader(file, delimiter=';')
#         lst = list(linhas)
#         for i in lst:
#             dados = str(i[0]).split(',')
#             if (value == (dados[0])):
                
#             #     lst.remove(i)

