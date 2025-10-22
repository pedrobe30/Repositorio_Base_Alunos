# # Exe 1
lado = float(input("Digite seu numero: "))
med_quadrado = lambda lado_quadrado: lado_quadrado**2
print(f"A area relacionada ao seu quadrado é de {med_quadrado(lado)}")

#Exe 2
salario_fun= float(input("Querido funcionario qual é o seu salario atual: "))
salario = lambda salario_atual: 0.15 * salario_atual
print(f"Seu novo salário com o aumento é de: {salario(salario_fun)}")

#Exe 3
print("--- Vamos Calcular a area de um triangulo ---")
altura = float(input("Qual é altura? "))
base = float(input("e a base? "))
triangulo = lambda b, h: (b*h) / 2
print(f"A area deste triangulo é de {triangulo(altura, base)}")

#Exe 4
print("----Bem vindo ao Calculador de Celsius para Farenheit----")
temp_celsius = float(input("Qual é a temperatura em celsius: "))
fahrenheit = lambda celsius: (9*celsius) / 5
print(f"A quantidade em fahrenheit é de {fahrenheit(temp_celsius)}")

# #Exe 5
print("Volume de um paralelepípedo!")
largura = float(input("Largura: "))
comprimento = float(input("Altura: "))
alt = float(input("Altura: "))
paralelepido = lambda l, c, a: l*a*c
print(f"O volume do paralelepípedo é de {paralelepido(largura, comprimento, alt)}")

#Exe 6
print("---Simulação Rendimento Concebido---")
periodo = int(input("Quantos meses de rendimento deseja simular? "))
valor = float(input("Valor para simulação: "))
juros = lambda valor: (valor * 0.013*periodo ) + valor
print(f"O valor após {periodo} mes de rendimeto foi de: {juros(valor)}")

# #Exe 7
soma = lambda v1, v2: (v1**2) + (v2**2)
print (f"A soma dos quadrados entre estes dois numeros é: {soma(2,3)}")

# #Exe 8
numbers = lambda n1, n2: (n1*-1 - n2*-1) 
print (f"A diferença destes valores é de: {numbers(10, 15)}")