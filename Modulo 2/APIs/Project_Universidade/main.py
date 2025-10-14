from utils import *
from sqlalchemy import *
from tabelas import *
from configurar_conexao import *

def criar_usuario(db_session, nome, sobrenome, email, senha, endereco):
    if not nome or not sobrenome or not email or not senha:
        raise ValueError("nome, sobrenome, email e senha são obrigatorios")
    
    if len(senha) < 6:
        raise  ValueError("SENHA DEVE TER PELO MENOS 6 CARACTERES")
    
    existing = db_session.query(Usuario).filter(Usuario.email == email).first()
    if existing:
        raise ValueError("Email já cadastrado")
    if not isinstance(endereco, dict) or any(k not in endereco for k in ("rua", "numero", "cep")):
        raise ValueError("endereco deve ser dict com rua, numero, cep")
    
    senha_hash = hash_password(senha)

    novo_usuario = Usuario(
        nome = nome, 
        sobrenome = sobrenome,
        email = email,
        senha_hash = senha_hash
    )

    novo_endereco = EnderecoUsuario(
        rua = endereco["rua"],
        numero = endereco["numero"],
        cep = endereco["cep"]
    )

    novo_usuario.enderecos = novo_endereco
    try:

        db_session.add(novo_usuario)
        db_session.commit()
        db_session.refresh(novo_usuario)

    except Exception as e:
        db_session.rollback()
        raise

    return {
        "id": novo_usuario.id,
        "nome": novo_usuario.nome,
        "sobrenome": novo_usuario.sobrenome,
        "email": novo_usuario.email,
        "endereco": {
            "rua": novo_endereco.rua,
            "numero": novo_endereco.numero,
            "cep": novo_endereco.cep
        }
    }

def login(db_session, email, senha):
    usuario = db_session.query(Usuario).filter(Usuario.email == email).first()

    if not usuario:
        return {"error": "Email ou Senha Invalidas"}
    
    senha_correta = verify_password(plain_password=senha, hashed_password=usuario.senha_hash)

    if not senha_correta:
        return {"error": "Email ou Senha Invalidas"}
    
    else:
         return {
        "id": usuario.id,
        "nome": usuario.nome,
        "sobrenome": usuario.sobrenome,
        "email": usuario.email,
        "endereco": {
            "rua": usuario.enderecos.rua if usuario.enderecos else None,
            "numero": usuario.enderecos.numero if usuario.enderecos else None,
            "cep": usuario.enderecos.cep if usuario.enderecos else None,
        }
    }


def deletar_usuario(db_session, user_id_logado, user_id_para_deletar):
    
    if user_id_logado != user_id_para_deletar:
        return {"error": "Você não tem permissão para deletar este usuario"}
    
    usuario = db_session.query(Usuario).filter(Usuario.id == user_id_para_deletar).first()

    if not usuario:
        return {"erro": "Usuario não encontrado"}
    
    try:
        db_session.delete(usuario)
        db_session.commit()
        return {"mensagem": "Usuario deletado com sucesso"}
    
    except Exception as e:
        db_session.rollback()
        raise


def add_polo(db_session, nome, telefone, polo_endereco):
    if not nome or not telefone or not polo_endereco:
        raise ValueError("erro:" "Está faltando preencher campos")
    
    if not isinstance(polo_endereco, dict) or any(k not in polo_endereco for k in ("rua", "numero", "cep", "cidade", "estado")):
        raise ValueError("endereco deve ser dict com rua, numero, cep")
    
    novo_polo = Polo(
        nome = nome,
        telefone = telefone
    )

    novo_endereco_polo = EnderecoPolo(
        rua = polo_endereco["rua"],
        numero = polo_endereco["numero"],
        cep = polo_endereco["cep"],
        cidade = polo_endereco["cidade"],
        estado = polo_endereco["estado"]
    )

    novo_polo.endereco = novo_endereco_polo


    try:
        db_session.add(novo_polo)
        db_session.commit()
        db_session.refresh(novo_polo)
    except Exception as e:
        db_session.rollback()
        raise

    return {
        "id": novo_polo.id,
        "nome": novo_polo.nome,
        "telefone": novo_polo.telefone,
        "endereco": {
            "rua": novo_endereco_polo.rua,
            "numero": novo_endereco_polo.numero,
            "cep": novo_endereco_polo.cep,
            "cidade": novo_endereco_polo.cidade,
            "estado": novo_endereco_polo.estado
        }
    }

def add_curso(db_session, nome, carga_horaria, modalidade, area, polos_ids=None):
    if not nome or not carga_horaria or not area or not modalidade:
        raise ValueError("nome, carga_horaria, modalidade e area são obrigatórios")
    
    try:
        modalidade_enum = ModalidadeEnum[modalidade]
        area_enum = AreaEnum[area]
    except KeyError:
        raise ValueError("Modalidade Invalida")

    if modalidade == "presencial" and (not polos_ids or len(polos_ids) == 0):
        raise ValueError("Cursos Presenciais precisam ter pelo menos um polo")

    if polos_ids:
        for polo_id in polos_ids:
            polo_existe = db_session.query(Polo).filter(Polo.id == polo_id).first()
            if not polo_existe:
                raise ValueError(f"Polo com id {polo_id} não encontrado")

    novo_curso = Curso(
        nome = nome,
        carga_horaria = carga_horaria,
        modalidade = modalidade_enum,
        area = area_enum
    )     

    try:
        db_session.add(novo_curso)
        db_session.commit()
        db_session.refresh(novo_curso)
    except Exception as e:
        db_session.rollback()
        raise

    if polos_ids:
        for polo_id in polos_ids:
            associacao = CursoPolo(id_curso=novo_curso.id, id_polo=polo_id)
            db_session.add(associacao)
        db_session.commit()
    
    return {
        "id": novo_curso.id,
        "nome": novo_curso.nome,
        "carga_horaria": novo_curso.carga_horaria,
        "modalidade": novo_curso.modalidade,
        "area": novo_curso.area,
        "polos": [{"id": cp.polo.id, "nome": cp.polo.nome} for cp in novo_curso.polos]
    }


def add_curso(db_session, nome, carga_horaria, modalidade, area, polos_ids=None):
    if not nome or not carga_horaria or not area or not modalidade:
        raise ValueError("nome, carga_horaria, modalidade e area são obrigatórios")
    
    try:
        modalidade_enum = ModalidadeEnum[modalidade]
        area_enum = AreaEnum[area]
    except KeyError:
        raise ValueError("Modalidade ou Area Invalida")

    if modalidade == "presencial" and (not polos_ids or len(polos_ids) == 0):
        raise ValueError("Cursos Presenciais precisam ter pelo menos um polo")

    if polos_ids:
        for polo_id in polos_ids:
            polo_existe = db_session.query(Polo).filter(Polo.id == polo_id).first()
            if not polo_existe:
                raise ValueError(f"Polo com id {polo_id} não encontrado")

    novo_curso = Curso(
        nome = nome,
        carga_horaria = carga_horaria,
        modalidade = modalidade_enum,
        area = area_enum
    )     

    try:
        db_session.add(novo_curso)
        db_session.commit()
        db_session.refresh(novo_curso)
    except Exception as e:
        db_session.rollback()
        raise

    if polos_ids:
        for polo_id in polos_ids:
            associacao = CursoPolo(id_curso=novo_curso.id, id_polo=polo_id)
            db_session.add(associacao)
        db_session.commit()
    
    return {
        "id": novo_curso.id,
        "nome": novo_curso.nome,
        "carga_horaria": novo_curso.carga_horaria,
        "modalidade": novo_curso.modalidade.value,
        "area": novo_curso.area.value,
        "polos": [{"id": cp.polo.id, "nome": cp.polo.nome} for cp in novo_curso.polos]
    }

def criar_matricula(db_session, user_id, id_curso):
  
  curso = db_session.query(Curso).filter(Curso.id == id_curso).first()
  if not curso:
      raise ValueError("Curso não encontrado")

  matricula = db_session.query(Matricula).filter(Matricula.id_usuario == user_id, Matricula.id_curso == id_curso).first()
  if matricula:
    raise ValueError("Você já está cadastrado neste curso")
  
  usuario = db_session.query(Usuario).filter(Usuario.id == user_id).first()
    
  nova_matricula = Matricula(
      id_usuario = user_id,
      id_curso = id_curso,
      status =  StatusMatriculaEnum.ativa
    )

  try:
     db_session.add(nova_matricula)
     db_session.commit()
     db_session.refresh(nova_matricula)
  except Exception as e:
     db_session.rollback()
     raise

  return {
      "id": nova_matricula.id,
      "usuario": {
      "id": usuario.id,
      "nome": usuario.nome,
      "sobrenome": usuario.sobrenome
      },
      "curso": {
      "id": curso.id,
      "nome": curso.nome
      },
      "data_matricula": nova_matricula.data_matricula.isoformat(),
      "status": nova_matricula.status.value  
}
    
        

def get_usuarios(db_session):
    return db_session.query(Usuario).all()

def get_polos(db_session):
    return db_session.query(Polo).all()

def get_cursos(db_session):
    return db_session.query(Curso).all()

def matricula_por_user(db_session, user_id):
    return db_session.query(Matricula).filter(Matricula.id_usuario == user_id).all()