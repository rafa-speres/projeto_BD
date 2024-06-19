import oracledb

def conectar_bd():
    connection = oracledb.connect(
        user="a13692380",
        password="123456",
        dsn="orclgrad1.icmc.usp.br:1521/pdb_elaine.icmc.usp.br"
    )
    return connection
