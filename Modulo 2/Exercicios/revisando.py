a = 3
b = 2
c = 4
d = 10

def aritmeticos(a, b, c, d):
    print("Exemplos de Operações Aritimeticas")
    print("-"*10)
    print(f"Soma = {a} + {a} = {a + a}")
    print(f"Subtração = {a} - {b} = {a - b}")
    print(f"Mutiplicação = {c} * {c} = {c * c}")
    print(f"Divisão = {c} / {d} = {c / d}")
    print(f"Divisão Inteira = {d} // {d} = {d // d}")
    print(f"Módulo = {d} % {c} = {d % c}")
    print(f"Exponeciação =  {b} ** {b} = {b ** b}")

def relacionais(a, b, c, d):
    print("Exemplos de Operadores Relacionais")
    print("-"*10)
    print(f"Maior = {a} > {b} : {a > b}")
    print(f"Maior ou Igual = {a} >= {b} : {a >= b}")
    print(f"Menor = {a} < {b} : {a < b}")
    print(f"Menor ou Igual = {a} <= {b} : {a <= b}")
    print(f"Igual = {c} == {c} : {c == c}")
    print(f"Diferente = {d} != {d} : {d != d}")

def logicos(a, b, c, d):
    print("Exemplos de Operadores Lógicos")
    print("-"*10)

    print("Exemplo do Operador (E) (and)")
    print(f" {a} > {b} and {b} < {a} : {a > b and b < a}")

    print("Exemplo do Operador (ou) (or)")
    print(f" {a} > {b} or {b} > {a} : {a > b or b > a}")

    print("Exemplo do Operador (não) (not)")
    print(f" {d} é = {d} : {not(d == d)}")

print("1 - Aritmeticos")
print("2 - Relacionais")
print("3 - Lógicos")
escolha = int(input("Qual operação deseja escolher: "))

if escolha == 1:
    aritmeticos(a, b, c, d)

elif escolha == 2:
    relacionais(a, b, c, d)

elif escolha == 3:
    logicos(a, b, c, d)

else:
    print("não foi possivel continuar")


