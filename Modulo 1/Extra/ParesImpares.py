numeros = []
impares = []
pares = []

def addNumbers():
    for numero in range(10):
     numero = int(input("Digite um numero inteiro, por favor: ")) 
     numeros.append(numero)
     if numero % 2 != 0:
        impares.append(numero)
     elif numero % 2 == 0:
        pares.append(numero)
        
    print(somaImpar())
    return(somaPar())
    
   
def somaPar():
   soma = 0
   for par in pares:
      soma += par
   print(f"A soma dos pares é de {soma}")
   
   
def somaImpar():
   soma = 0
   for impar in impares:
      soma += impar
   print(f"A soma dos numeros impares é de {soma}")
   
   
addNumbers()
print(f"Numeros Impares: {impares}")
print(f"Numeros Pares: {pares}")