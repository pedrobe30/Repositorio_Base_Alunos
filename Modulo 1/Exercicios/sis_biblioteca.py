titulo = []
autor = []
ano = []
genero = []

def menu():
   while True:
    print("\nSeja Bem vindo--Sistema Bibliotecario")
    print("1 -- Cadastrar Livros")
    print('2 -- Ver todos os livros')
    print("3 -- Buscar Livro")
    print("4 -- Remover um LIvro")
    print("5 -- Sair")
    escolha = int(input("O que deseja fazer: "))
    if escolha == 1:
      cadastro()
    elif escolha == 2:
      ler()


def cadastro():
  title = input("Titulo do Livro: ")
  titulo.append(title)
  nome = input(f"Autor do Livro {title} : ")
  autor.append(nome)
  year = input(f"Ano em que foi puplicado {title}: ")
  ano.append(year)
  tipo = input(f"Qual é o genero do Livro {title}: ")
  genero.append(tipo)
  

def ler():
  print("Livros da nossa biblioteca")
  if titulo == 0:
    print("Não há livros cadastrados")
  else:
    for i in range(len(titulo)):
      print(f"Titulo: {titulo[i]} Autor: {autor[i]} Ano: {ano[i]} Gênero: {genero[i]} ")
      
      
def buscar():
  print("Procure o Livro por Autor: ")
