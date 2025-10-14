nomes = []
idades = []
categorias = []
def infoCadastro():
    while True:
     nome = input("Qual é seu nome: ")
     nomes.append(nome)

     idade = int(input("Sua idade: "))
     if idade < 18:
        print(f" {nome} Infelizmnete você não pode tirar carteira, menor de idade ")
        break
     else:
        idades.append(idade)

     categoria = input("Tipo de carteira que deseja tirar: (A) (B) (AB): ")
     categoria_masc = categoria.upper()
     if categoria_masc in ("A", "B", "AB"):
       categorias.append(categoria_masc)
     else:
        print(f"Categoria{categoria_masc} não encontrada, tente novamente!")


     deseja = input("Deseja cadastrar outro aluno? (s/n)")
     deseja_min = deseja.lower()
     if deseja_min in ('sim', 's'):
      continue
     else:
        break
      
     



def exibicao():
   print("---Alunos Cadastrados----")
   for i in range(len(nomes)):
      print(f"Nome: {nomes[i]}, Idade: {idades[i]}, Categoria: {categorias[i]}")

infoCadastro()
exibicao()  