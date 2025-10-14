import csv, os, time

name_file = 'testando.csv'

try:
    file = open(name_file)
    leitor = csv.reader(file, delimiter='|', dialect='excel')

    for linha in leitor:
        print('Linha #%s <%s>' % (leitor.line_num, linha))

    file.close()
except FileNotFoundError:
    try:
        print('Arquivo não encontrado')
        print("Criando a pasta...")
        with open(name_file, 'a') as arquivo:
            pass
        time.sleep(1)
        print('Arquivo Criado, Rode o sistema Novamente')
    except IOError:
        print('Error')
    