import oracledb

def conectar_bd():
    connection = oracledb.connect(
        user="seu_usuario",
        password="sua_senha",
        dsn="seu_dsn"
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
