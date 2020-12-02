import mysql.connector
#Versao 1.2.3
#Ultima modificacao: Aiko Ramalho
__all__ = ["Cria_Novo_Jogador", "Pega_Jogadores", "Destroi_Jogadores"]

#Modulo que diz respeito aos jogadores do Yahtzee.Nele cadastramos e pegamos
#o nome dos jogadores.
#Dentro deste modulo existe uma lista de objetos jogadores.
#A lista pode ter tamanho maximo 2. O objeto jogador tem um dicionario
#com ID(int) e Nome(string),
#exemplo: {01: Aiko}, {02: Carol}, {03: Carlos}.

cnx = mysql.connector.connect(user='root', password='root', database='modular')
cursor = cnx.cursor()

#Recebe o nome do jogador por parâmetro e cadastra na lista de jogadores.
#Paramêtros: nomeJogador, id (opcional para caso de carregar partida por xml)
#retorna 0 caso o jogador tenha sido criado corretamente
#retorna 1 caso ja existam 2 jogadores(limite maximo)
#retorna 2 caso o nome nao tenha sido passado corretamente
def Cria_Novo_Jogador(nomeJogador, id_):
    qtdJogadores = 2 - list(Pega_Jogadores().keys())[0]
    if(qtdJogadores == 2):
        return 1
    if(len(nomeJogador) == 0):
        return 2
    if(id_ == None):
        add_jogador = ("INSERT INTO Jogadores "
                    "(nome) "
                    "VALUES (%s)")
        data_jogador = (nomeJogador,)
    else:
        add_jogador = ("INSERT INTO Jogadores "
                    "(jogadorId, nome) "
                    "VALUES (%s, %s)")
        data_jogador = (id_, nomeJogador)
    cursor.execute(add_jogador, data_jogador)
    cnx.commit()
    return 0


#Funcao que retorna a lista dos jogadores.
#Paramêtros: None
#Retorna {0: [Jogador1, Jogador2]} caso obtido sucesso
#Retorna {1: []} caso falte um jogador a ser cadastrado
#retorna {2: []} caso faltem dois jogadores para serem cadastrados
def Pega_Jogadores():
    query = ("SELECT * FROM Jogadores ")
    cursor.execute(query)
    lista = cursor.fetchall()
    qtdJogadores = len(lista)
    if(qtdJogadores == 2):
        jogadores = [{lista[0][0]: lista[0][1]}, {lista[1][0]: lista[1][1]}]
        return {0: jogadores}
    elif(qtdJogadores == 1):
        return {1: []}
    return {2: []}

#funcao que esvazia a lista de jogadores
#Paramêtros: None
#retorna 0 caso sucesso
#retorna 1 caso a lista ja esteja vazia
def Destroi_Jogadores():
    qtdJogadores = 2 - list(Pega_Jogadores().keys())[0]
    if(qtdJogadores == 0):
        return 1
    sql = ("DELETE FROM Jogadores")
    cursor.execute(sql)
    cnx.commit()
    return 0