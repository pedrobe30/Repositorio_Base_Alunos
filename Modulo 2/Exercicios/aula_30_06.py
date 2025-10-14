import os

arquivo_path = "C:/Users/Aluno_Programador3/3D Objects/Pedro_Bernardo/"
recebido = print(input("Qual é o nome do arquivo:"))
arquivo_completo = (arquivo_path + recebido)
try:
     os.rmdir(arquivo_completo)
     print(f"apagada {arquivo_completo}")
except FileNotFoundError:
     print(f"{arquivo_completo} não encontrado")
except OSError:
     print(f"{arquivo_completo} é um arquivo, não uma pasta")

# try:
#   os.remove("C:/Users/Aluno_Programador3/3D Objects/Pedro_Bernardo/slk/texto.txt")
# except FileNotFoundError:
#   print("Não Encontrado")