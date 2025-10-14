# idade = 30
# print("[%d]" % idade)
# print("%5f" % 5)

# nome = "Pedro"
# idade = 17
# grana = 21.50
# print("%s tem %d anos e R$%5.2f no bolso" % (nome, idade, grana))

import sys, os 

print("NUmeros de Parametros: %d" % len(sys.argv))
for n, p in enumerate(sys.argv):
 print("Parametro %d = %s" % (n,p))
 try:
  os.mkdir(p)
 except:
  print("erro") 
 try:
  escolha = input("Agora Deseja Apagar qual pasta?")
  escolha = n
  os.rmdir(escolha)
 except:
  print("Não Foi")


