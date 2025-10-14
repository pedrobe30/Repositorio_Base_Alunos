# Conversor de Moedas USD/BRL - Versão Simplificada para Iniciantes
# Definição da taxa de câmbio fixa (1 dólar = 5 reais)
TAXA_DOLAR_PARA_REAL = 5
# Loop principal do programa

def DolarReal(vdolar):
    valor_real = vdolar * TAXA_DOLAR_PARA_REAL
    print(f"US$ {valor_dolar:.2f} = R$ {valor_real:.2f}")
    
def RealDolar(vreal):
   valor_dolar = vreal / TAXA_DOLAR_PARA_REAL
   print(f"R$ {valor_real:.2f} = US$ {valor_dolar:.2f}")

while True:
    # Menu de opções
    print("\n=== Conversor de Moedas ===")
    print("1 - Converter Dólar para Real")
    print("2 - Converter Real para Dólar")
    print("0 - Sair do programa")
    # Recebe a escolha do usuário
    opcao = input("Digite sua opção: ")
      # Opção 1: Converter Dólar para Real
    if opcao == "1":
          valor_dolar = input("Digite o valor em dólares (USD): ")
          valor_dolar = float(valor_dolar) # Converte para número decimal
          DolarReal(valor_dolar)
          
      # Opção 2: Converter Real para Dólar
    elif opcao == "2":
          valor_real = input("Digite o valor em reais (BRL): ")
          valor_real = float(valor_real) # Converte para número decimal
          RealDolar(valor_real)
      # Opção 0: Sair do programa
    elif opcao == "0":
          print("Obrigado por usar o conversor. Até mais!")
          break # Encerra o loop while
      # Tratamento de opção inválida
    else:
         print("Opção inválida! Por favor, digite 1, 2 ou 0.")
