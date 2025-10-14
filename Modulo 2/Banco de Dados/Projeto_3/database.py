import sqlite3

try:
    con = sqlite3.connect("deposito.db")
    con.execute("PRAGMA foreign_keys = ON")
    cur = con.cursor()

except ConnectionRefusedError as c:
        print('Erro de conexão com o banco')


def createEntidades():

    cur.execute("CREATE TABLE funcionario(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, codigo INTEGER NOT NULL UNIQUE, setor VARCHAR(255) NOT NULL)")
    cur.execute("CREATE TABLE pegar_chave(id_operacao INTEGER PRIMARY KEY AUTOINCREMENT, id_funcionario INTEGER NOT NULL, FOREIGN KEY (id_funcionario) REFERENCES funcionario(id) ON DELETE CASCADE ON UPDATE CASCADE)")
    cur.execute("CREATE TABLE devolver_chave(id_devolucao INTEGER PRIMARY KEY AUTOINCREMENT, operacao_id INTEGER NOT NULL, FOREIGN KEY (operacao_id) REFERENCES pegar_chave(id_operacao) ON DELETE CASCADE ON UPDATE CASCADE )")
    cur.execute("CREATE TABLE verificacao(funcionario_id INTEGER NOT NULL, codigo_acesso INTEGER NOT NULL, FOREIGN KEY (funcionario_id) REFERENCES funcionario(id), FOREIGN KEY (codigo_acesso) REFERENCES funcionario(codigo) ON DELETE CASCADE ON UPDATE CASCADE)")

    con.commit()


    
def CadastroFuncionario():
     
     nome = input("Digite seu nome: ")
     setor = input("Em qual sala Trabalha: ")
     codigo = int(input("Crie um codigo para fazer as operações: "))
     cur.execute(f"INSERT INTO funcionario (nome, codigo, setor) VALUES('{nome}', '{codigo}', '{setor}')")
     con.commit()
     funcionario_id = cur.lastrowid
     cur.execute(f"INSERT INTO verificacao (funcionario_id, codigo_acesso) VALUES('{funcionario_id}', '{codigo}')")
     con.commit()
     return "Funcionario Cadastrado com Sucesso"

def PegarChave():
    codigo_tentativa = int(input("Digite o codigo para pegar a chave: "))
    cur.execute(f"SELECT funcionario_id FROM verificacao where codigo_acesso = {codigo_tentativa}")
    resultado = cur.fetchone()

    if not resultado:
         return "Codigo Invalido. Acesso Negado"
    
    funcionario_id = resultado[0]

    cur.execute("SELECT COUNT(*) FROM pegar_chave WHERE id_operacao NOT IN ( SELECT operacao_id FROM devolver_chave)")
    chave_em_uso = cur.fetchone()[0]

    if chave_em_uso > 0:
         return "A chave já está em uso por outro funcionário"
    
    cur.execute(f"INSERT INTO pegar_chave (id_funcionario) VALUES ('{funcionario_id}')")
    con.commit()

    return "Chave retirada com sucesso"

def DevolverChave():
     codigo_tentativa = int(input("Digite o codigo para devolver a chave: "))
     cur.execute(f"SELECT funcionario_id FROM verificacao where codigo_acesso = {codigo_tentativa}")
     resultado = cur.fetchone()

     if not resultado:
          return "Codigo incorreto, Tente novamente."
     
     funcionario_id = resultado[0]

     cur.execute(f"SELECT id_operacao FROM pegar_chave WHERE id_funcionario = {funcionario_id} AND id_operacao NOT IN (SELECT operacao_id FROM devolver_chave)")
     operacao = cur.fetchone()

     if not operacao:
          return "Nenhuma Chave em seu nome está pendente para a devolução."
     
     id_operacao = operacao[0]

     cur.execute(f"INSERT INTO devolver_chave (operacao_id) VALUES({id_operacao})")
     con.commit()

     return "Chave Devolvida com Sucesso"

def BuscarChave():
     
     cur.execute("SELECT id_funcionario FROM pegar_chave WHERE id_operacao NOT IN (SELECT operacao_id FROM devolver_chave)")
     resultado = cur.fetchone()

     if resultado:
          funcionario_id = resultado[0]
          cur.execute(f"SELECT nome FROM funcionario WHERE id = {funcionario_id}")
          nome_resultado = cur.fetchone()

          if nome_resultado:
               nome = nome_resultado[0]
               return f"A chave está com {nome}"
          else:
               return f"Funcionario não encontrado no sistema"
     else:
          return "Nenhum funcionario está com a chave no momento"


# print(CadastroFuncionario())
#print(PegarChave())
#print(DevolverChave())
print(BuscarChave())
    




  