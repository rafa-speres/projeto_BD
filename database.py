import oracledb

def conectar_bd():
    connection = oracledb.connect(
        user="a13692380",
        password="123456",
        dsn="orclgrad1.icmc.usp.br:1521/pdb_elaine.icmc.usp.br"
    )
    return connection

def cadastrar_usuario_bd(usuario, senha, tipo_usuario):
    conn = conectar_bd()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO USERS (USUARIO, SENHA, TIPO_USUARIO) VALUES (:usuario, :senha, :tipo_usuario)",
            [usuario, senha, tipo_usuario]
        )
        conn.commit()
    except Exception as e:
        print(f"Erro ao cadastrar usuário: {e}")
    finally:
        cursor.close()
        conn.close()

#TODO: param -- username, senha
#return -- tipo, check (bool se existe ou nao o usuario)
def validacao_user():
    pass