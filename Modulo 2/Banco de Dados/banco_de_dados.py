import sqlite3

try:
    con = sqlite3.connect("meu_banco.db")

    cur = con.cursor()

    # con.execute("CREATE TABLE pessoa(id, nome, idade, cpf)")
    # con.execute("INSERT INTO pessoa VALUES(1, 'Bernardo', 17, '123.456.789-10')")
    
    res = cur.execute("SELECT * FROM pessoa")
    pessoas = res.fetchone()

    print(pessoas)

    #cur.execute("DELETE FROM pessoa where id = 1")

    

    cur.close()

except ConnectionRefusedError as c:
    print('Erro de conexão com o banco')

