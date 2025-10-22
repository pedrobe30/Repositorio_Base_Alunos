n1 = float(input("Digite um numero: "))
n2 = float(input("Digite um numero: "))

somar = lambda num1, num2: num1 + num2
print(f"A soma entre {n1} + {n2} é igual a {somar(n1,n2)}")