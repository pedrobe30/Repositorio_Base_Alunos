def menu():
    print("--Bem vindo a sua agenda pessoal--")
    print("1. - Se Cadestre")
    print("2. - Lista de Usuarios")
    print("3. - Excluir Conta")
    print("0. - Sair")
    escolha = int(input("O que deseja fazer? "))
    if escolha == 1:
       cadastro()
    elif escolha == 2:
       lista_usuarios()
    
        










def cadastro(name):
  name =  input("Como se chama")
  print((f"{name} redirecionando para o menu"))
  return menu()

def lista_usuarios(lista):
   print("Lista de Usuarios")
   lista = []
   lista.append(__name__)

def excluir_conta(nome):
  nome = input("Digite seu nome para excluir sua conta: ")

     
  
  
  




# lista_pessoas = []
# lista_pessoas.append(nomes)
# print("Lista de Usuarios: ")
# print(lista_pessoas)


