numeros = []
numeros.append(1)
numeros.append(2)
numeros.append(3)
numeros.append(4)
numeros.append(5)

print(numeros)


lista_10_em_10 = [10, 20, 30]
lista_10_em_10.insert(1, 15)
print(lista_10_em_10)

alfabeto = ['a', 'b', 'c']
alfabeto[1] = 'x'
print(alfabeto)

lista_5_em_5 = [5, 10, 15, 20]
del lista_5_em_5[2]
print(lista_5_em_5)

frutas = ['maça', 'banana', 'laranja']
frutas.remove('banana')
print(frutas)

lista_100_em_100 = [100, 200, 300, 400]
lista_100_em_100.pop(3)
print(lista_100_em_100)

linguagens = ['python', 'java', 'c++']
linguagens.pop(1)
print(linguagens)

ordem_crescente = [1, 2, 3, 4, 5]
ordem_crescente.clear()
print(ordem_crescente)

letras = ['a', 'b', 'd']
letras.insert(2, 'c')
print(letras)
letras.remove('a')
print(letras)

divisivel_por_10 = [10, 20, 30, 40, 50]
divisivel_por_10.append(60)
print(divisivel_por_10)
divisivel_por_10.insert(1, 15)
print(divisivel_por_10)
divisivel_por_10.remove(30)
print(divisivel_por_10)
ultimo_elemento = divisivel_por_10.pop()
print(divisivel_por_10)
print(ultimo_elemento)