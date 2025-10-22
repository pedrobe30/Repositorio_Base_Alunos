numbers = [-4.4, 54, -1.7, 12, 1.2, 0.50, 0.75, 8, 210, -10]

maior_que_dois = lambda y: y>2
verdadeiros = list(map(maior_que_dois, numbers))
# valores_reais = list(verdadeiros)

print(verdadeiros)
# for numeros in verdadeiros:
#     if numeros == True:
#         print(f"{valores_reais} é maior que 2")
#     if numeros == False:
#         print(f"{valores_reais} é menor que 2")

