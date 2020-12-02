#Versao 1.6
#Autor: Ana Carolina Coscarella
#Ultima modificacao: Aiko Ramalho
import mysql.connector
__all__ = ["Cria_Novo_Jogo",  "Atualiza_JogadorAtual", "Pega_Jogo"]

cnx = mysql.connector.connect(user='root', password='root', database='modular')
cursor = cnx.cursor()

def verifica_ja_existe_jogo():
    sql = ("SELECT COUNT(*) FROM JOGO")
    cursor.execute(sql)
    return cursor.fetchall()

#Descrição: Cria um novo objeto jogo. Retorna 0 se conseguiu criar o objeto Jogo corretamente, caso já tenha objeto Jogo criado, retorna 1.
#Parâmetros: jogador_id - id do jogador / args - parametro opcional indicando o id do jogo (feito exclusivamente pra testes)
#Retorno: 
#0 - Caso o jogo seja criado corretamente
#1 - caso o parametro jogador_id nao seja um numero

def Cria_Novo_Jogo(jogador_id, *args):
    if(type(jogador_id) != type(0)):
        return 1
    if(args and args[0]):
        params = (args[0], jogador_id)
        add_jogo = ("INSERT INTO Jogo "
                    "(JogoId, jogador_atual) "
                    "VALUES (%s, %s)"
        )
    else:
        params = (jogador_id,)
        add_jogo = ("INSERT INTO Jogo "
                    "(jogador_atual) "
                    "VALUES (%s)")
    cursor.execute(add_jogo, params)
    cnx.commit()
    return 0

#Descrição: Função que recebe a lista dos dois jogadores e o jogador_atual.
#Como são só dois jogadores no jogo, ele simplesmente atualiza o valor jogador_atual para o outro jogador. 
#Parâmetros:
#-novoJogadorAtual_id = id do novo jogador atual
#Retorno: 
#0 - Caso tenha sucesso ao atualizar o jogador,retorna dicionário com 0 e o novo jogador da vez
#1 - Caso o parâmetro novoJogadorAtual_id não seja um int
#2 - Caso novoJogadorAtual_id seja um numero que nao seja um dos ids no jogo

def Atualiza_JogadorAtual(novoJogadorAtual_id):
    if(type(novoJogadorAtual_id) != type(0)):
        return 1
    retorno = Pega_Jogo()
    sql = ("UPDATE Jogo "
        "SET jogador_atual = (%s) "
        "WHERE JogoId = (%s) "
    )
    params = (novoJogadorAtual_id, list(retorno.keys())[0])
    cursor.execute(sql, params)
    cnx.commit()
    return 0

#Funcao que retorna o Jogo

#Retorna o Id do jogo criado e o id do jogador_atual
def Pega_Jogo():
    sql = ("SELECT * "
        "FROM Jogo "
        "ORDER BY JogoId DESC "
        "LIMIT 1"
    )
    cursor.execute(sql)
    retorno = cursor.fetchall()
    return {retorno[0][0]: {"jogador_atual": retorno[0][1]}}

#funcao que destroi o modulo jogo
#retorna 0 caso sucesso
#retorna 1 caso jogo nao exista jogo
def Destruir_Jogo():
    qtdJogos = verifica_ja_existe_jogo()[0][0]
    if(qtdJogos == 0):
        return 1
    sql = ("DELETE FROM Jogo")
    cursor.execute(sql)
    cnx.commit()
    return 0
