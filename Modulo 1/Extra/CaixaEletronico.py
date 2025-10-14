saldoInicial = 1000

print("Caixa Eletronico")


def menu():
    while True:
     print("Menu de opções")
     print(" 1-- Ver seu saldo")
     print(" 2-- Saque seu Dinheiro")
     print(" 3-- Sair")
     escolha = int(input("\n----Escolha uma das opções acima----"))
    
     if escolha == 1:
            print(f"Seu saldo atual é de {saldoInicial}")
     elif escolha == 2:
            sacar()
     elif escolha == 3:
            break
     else:
          print("Opção não encontrada, voltando para o menu")
           
    


def sacar():
    dinRetirado = float(input("Qual valor deseja sacar?: "))
    novoSaldo = saldoInicial - dinRetirado
    if dinRetirado > saldoInicial:
        print("Valor maior que seu saldo atual")
    elif dinRetirado < 1:
        print("Operação Impossível")
    else:
        print(f"Seu novo saldo é de {novoSaldo}")

menu()
    
