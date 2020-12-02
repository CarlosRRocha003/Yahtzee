import mysql.connector
#Versao 1.1.0
#Ultimo modificacao: Aiko Ramalho

'''
Módulo que contém uma lista ordenada por ordem de criação de objetos rodada. 
O objeto rodada é um dicionário com chave ID e valor como um novo dicionário, 
com chave tentativas e valor número restante de tentativas. 
Exemplo: {01: { “tentivas”: 2 }}
'''

cnx = mysql.connector.connect(user='root', password='root', database='modular')
cursor = cnx.cursor()

MAX_RODADAS = 26 #define o numero maximo de rodadas (numero padrao de um jogo yahtzee)

__all__ = ["Cria_Rodada", "Verifica_Tentativa", "Atualiza_Tentativas", "Deleta_Rodadas", "Pega_Rodada"]


#funcao auxiliar pra retornar o numero de rodadas criadas pegando a info do bd
def count_numero_rodada():
    query = ("SELECT COUNT(*) FROM Rodadas")
    cursor.execute(query)
    return cursor.fetchall()

#funcao responsavel por criar o objeto rodada com 3 tentativas e dar append nele na lista
#Parâmetros: id_rodada (opcional somente para caso de teste)
#retorna 0 no sucesso
#retorna 1 caso numero de rodadas maxima tenha sido atingida
def Cria_Rodada(*args):
    numero_rodada = count_numero_rodada()[0][0]
    if(numero_rodada > MAX_RODADAS):
        return 1
    if(args and args[0]):
        params = (args[0],)
        add_rodada = ("INSERT INTO Rodadas "
                    "(RodadaId, Tentativas) "
                    "VALUES (%s, 3)")
        cursor.execute(add_rodada, params)
    else:
        add_rodada = ("INSERT INTO Rodadas "
                    "(Tentativas) "
                    "VALUES (3)")
        cursor.execute(add_rodada)
    cnx.commit()
    return 0
    
#funcao responsavel por verificar se ainda restam tentativas na ultima rodada criada
#retorna 0 caso tenham tentativas
#retorna 1 caso nao tenham tentativas
#retorna 2 caso nao tenham rodadas
def Verifica_Tentativa():
    numero_rodada = count_numero_rodada()[0][0]
    if(numero_rodada == 0):
        return 2
    query = ("SELECT Tentativas "
            "FROM Rodadas "
            "ORDER BY RodadaId DESC "
            "LIMIT 1")
    cursor.execute(query)
    num_tentivas = cursor.fetchall()[0][0]
    if(num_tentivas == 0):
        return 1
    return 0

#funcao responsavel por atualizar o numero de tentativas da ultima rodada
#retorna 0 caso sucesso
#retorn 1 caso o numero de tentativas do parametro n seja num_tentativas-1 ou zero
#retorna 2 caso o numero passado n esteja no range de tentativas
#retorn 3 caso o numero passado n seja int
#retorna 4 caso nao tenham rodadas
def Atualiza_Tentativas(num):
    numero_rodada = count_numero_rodada()[0][0]
    if(type(num) != type(0)):
        return 3
    if(num not in range(0, 4)): #range no python eh aberto no extremo da direita
        return 2
    if(numero_rodada == 0):
        return 4
    
    query = ("SELECT RodadaId, Tentativas "
            "FROM Rodadas "
            "ORDER BY RodadaId DESC "
            "LIMIT 1")
    cursor.execute(query)
    retorno = cursor.fetchall()
    num_tentativas = retorno[0][1]
    if(num != 0 and num != num_tentativas-1):
        return 1
    rodadaId = retorno[0][0]
    updateRodada = ("UPDATE Rodadas "
            "SET Tentativas = (%s) "
            "WHERE RodadaId = (%s)"
    )
    parametros = (num, rodadaId)
    cursor.execute(updateRodada, parametros)
    cnx.commit()
    return 0

#funcao que esvazia a lista de rodadas
#Paramêtros: None
#retorna 0 caso sucesso
#retorna 1 caso a lista ja esteja vazia
def Deleta_Rodadas():
    query = ("SELECT COUNT(*) FROM Rodadas")
    cursor.execute(query)
    qtdRodadas = cursor.fetchall()[0][0]
    if(qtdRodadas == 0):
        return 1
    sql = ("DELETE FROM RODADAS")
    cursor.execute(sql)
    cnx.commit()
    return 0

#funcao que retorna a ultima rodada
#retorna {1: None} caso nao hajam rodadsa
#retorna {0: Rodada} caso haja rodada
def Pega_Rodada():
    query = ("SELECT COUNT(*) FROM Rodadas")
    cursor.execute(query)
    numero_rodada = cursor.fetchall()[0][0]
    if(numero_rodada == 0):
        return {1: None}
    query = ("SELECT RodadaId, Tentativas "
            "FROM Rodadas "
            "ORDER BY RodadaId DESC "
            "LIMIT 1")
    cursor.execute(query)
    retorno = cursor.fetchall()
    return{0: {retorno[0][0]: {"tentativas": retorno[0][1]}}}
