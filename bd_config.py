import mysql.connector
from mysql.connector import errorcode
DB_NAME = 'modular'
cnx = mysql.connector.connect(user='root', password='root')
cursor = cnx.cursor()
TABLES = {}
TABLES['rodadas'] = (
    "CREATE TABLE `Rodadas` ("
    "  `RodadaId` int(2) NOT NULL AUTO_INCREMENT,"
    "  `Tentativas` int(1) NOT NULL,"
    "   PRIMARY KEY (`RodadaId`)"
    ") ENGINE=InnoDB")
TABLES['jogadores'] = (
    "CREATE TABLE `Jogadores` ("
    "  `JogadorId` int(1) NOT NULL AUTO_INCREMENT,"
    "  `Nome` varchar(40) NOT NULL,"
    "  PRIMARY KEY(`JogadorId`)"
    ") ENGINE=InnoDB")
TABLES['jogo'] = (
    "CREATE TABLE `Jogo` ("
    "  `JogoId` int(1) NOT NULL AUTO_INCREMENT,"
    "  `jogador_atual` int,"
    "  PRIMARY KEY(`JogoId`),"
    "  CONSTRAINT `FK_jogador_atual` FOREIGN KEY (`jogador_atual`) "
    "     REFERENCES `Jogadores` (`JogadorId`) ON DELETE CASCADE"
    ") ENGINE=InnoDB")

__all__ = ['cria_ambiente', 'reset_database']

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

#prints db
def cria_ambiente():
    try:
        cursor.execute("USE {}".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Database {} nao existe. -- tentando criar".format(DB_NAME))
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database(cursor)
            print("Database {} criado com sucesso.".format(DB_NAME))
            cnx.database = DB_NAME
        else:
            print(err)
            exit(1)

    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print("criando tabela {}: ".format(table_name), end='')
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("ja existe.")
            else:
                print(err.msg)
        else:
            print("OK")

def reset_database():
    print('droping database')
    sql = ("DROP DATABASE modular")
    try:
        cursor.execute(sql)
    except:
        print('database ja resetado')
    cnx.commit()
    print('database dropped')
