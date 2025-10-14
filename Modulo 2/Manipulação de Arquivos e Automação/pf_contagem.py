import csv

name_file = 'OCORRENCIAS_2025.csv'

try:
    file = open(name_file)
    leitor = csv.reader(file, delimiter=';', dialect='excel')

    

    contagem_carabina = 0
    contagem_cara_cart = 0
    contagem_cara_espi = 0
    contagem_cara_fuzil = 0
    contagem_espingarda = 0
    contagem_fuzil = 0
    contagem_garrucha = 0
    contagem_garrucao = 0
    contagem_pistola = 0
    contagem_pistolao = 0
    contagem_revolver = 0
    contagem_rifle = 0

    for linha in leitor:
        if linha[4].strip().lower() == 'carabina':
            contagem_carabina += 1

        elif linha[4].strip().lower() == 'carabina/cartucheira':
            contagem_cara_cart += 1

        elif linha[4].strip().lower() == 'carabina/espingarda':
             contagem_cara_espi += 1

        elif linha[4].strip().lower() == 'carabina/fuzil':
             contagem_cara_fuzil += 1
             
        elif linha[4].strip().lower() == 'espingarda':
             contagem_espingarda += 1

        elif linha[4].strip().lower() == 'fuzil':
             contagem_fuzil += 1

        elif linha[4].strip().lower() == 'garrucha':
             contagem_garrucha += 1

        elif linha[4].strip().lower() == 'garruchao':
             contagem_garrucao += 1

        elif linha[4].strip().lower() == 'pistola':
             contagem_pistola += 1

        elif linha[4].strip().lower() == 'pistolao':
             contagem_pistolao += 1

        elif linha[4].strip().lower() == 'revolver':
             contagem_revolver += 1

        elif linha[4].strip().lower() == 'rifle':
             contagem_rifle += 1

    print(f"A palavra 'Carabina' aparece {contagem_carabina} vezes")
    print(f"A palavra 'Carabina/cartucheira' aparece {contagem_cara_cart} vezes")
    print(f"A palavra 'Carabina/espingarda' aparece {contagem_cara_espi} vezes")
    print(f"A palavra 'Carabina/Fuzil' aparece {contagem_cara_fuzil} vezes")
    print(f"A palavra 'Espingarda' aparece {contagem_espingarda} vezes")
    print(f"A palavra 'Fuzil' aparece {contagem_fuzil} vezes")
    print(f"A palavra 'Garrucha' aparece {contagem_garrucha} vezes")
    print(f"A palavra 'Garruchao' aparece {contagem_garrucao} vezes")
    print(f"A palavra 'Pistola' aparece {contagem_pistola} vezes")
    print(f"A palavra 'Pistolao' aparece {contagem_pistolao} vezes")
    print(f"A palavra 'Revolver' aparece {contagem_revolver} vezes")
    print(f"A palavra 'Rifle' aparece {contagem_rifle} vezes")

except FileNotFoundError:
    print('Errorr')
