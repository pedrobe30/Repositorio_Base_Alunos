nome = input("Digite seu nome: ")
email = input("Qual é seu email: ")

with open("C:/Users/Aluno_Programador3/3D Objects/ArquivosCriados/pessoasCadastradas.txt", "a") as arquivo:
    arquivo.write(nome + ' | ' + email + "\n")