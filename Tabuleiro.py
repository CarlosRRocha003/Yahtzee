#Versao 1.1.5
#Ultima modificacao: Carlos Ribeiro

import Jogador

__all__ = ["Cria_Tab", "Destruir_Tab", "InserirPontuacao", "Verifica_Vencedor", "Pega_Tabuleiro"]

tabuleiro = []

listaPont = []

pontuacaoAux = {
    "Ones": 0,
    "Twos": 1,
    "Threes": 2,
    "Fours": 3,
    "Fives": 4,
    "Sixes": 5,
    "Three of a Kind": 6,
    "Four of a Kind": 7,
    "Full House": 8,
    "Small Straight": 9,
    "Large Straight": 10,
    "Chance": 11,
    "Yahtzee": 12,
    "Total Score": 13,
    }

#Modulo no qual eh desenvolvido e implementado a criacao do Tabuleiro do
#Jogo Yahtzee.Ele eh criado quando o Jogo se inicia e atualizado a cada
#jogada com as devidas pontuacoes dos jogadores.Ele armazena uma matriz
#14x2 onde cada linha representa um tipo de pontuacao diferente e cada
#coluna um dos dois jogadores.
#As linhas sao: Ones, Twos, Threes, Fours, Fives, Sixes, Three of a Kind,
#Four of a Kind, Full House, Small Straight, Large Straight, Chance,
#Yahtzee e Total Score, respectivamente.

#Cria o Tabuleiro vazio inicializado, onde serao inseridas as pontuacoes.
#Parametros: None
#retorna 0 caso o Tabuleiro seja criado com sucesso
#retorna 1 caso ja exista um Tabuleiro (tentativa de recriacao)
def Cria_Tab():
    
    if len(tabuleiro)>0:
        return 1
    
    for _ in range(0,14):
        tabuleiro.append([None,None]) #Caso use 0,0 sera necessario fazer uma verificacao futura        
    
    return 0

#Funcao responsavel por destruir e zerar a matriz do tabuleiro
#Parametros: None
#retorna 0 Caso o Tabuleiro seja destruido com sucesso
#retorna 1 Caso nao exista Tabuleiro a ser destruido
def Destruir_Tab():

    if len(tabuleiro)==0:
        return 1

    tabuleiro.clear()
    
    return 0

#Insere a pontuacao atual na devida casa do tabuleiro e incrementa
#a pontuacao total na matriz.
#Parametros: pontuacao_atual,jogadorAtual(ID),tipoPontuacao
#retorna 0 Caso a insercao da pontuacao tenha ocorrido com sucesso
#retorna 1 Caso o parametro pontuacao_atual nao seja int
#retorna 2 Caso idJogadorAtual nao seja um int
#retorna 3 Caso tipoPontucao nao seja string.
#retorna 4 Caso o parametro jogadorAtual nao corresponda com nenhum
#dos jogadores presentes no jogo
#retorna 5 Caso tipoPontuacao nao corresponda com nenhum tipo
#de pontuacao
#retorna 6 Caso a casa ja esteja preenchida
def InserirPontuacao(dados, idJogadorAtual, tipoPontuacao, pontuacao):
    import Pontuacao
    id_primeiro_jogador = list(Jogador.Pega_Jogadores()[0][0].keys())[0]
    achado = 0
    achadoJogador = 0
    listaA = Jogador.Pega_Jogadores()
    listaJogadores = listaA[0]
    if(pontuacao != None):
        pontuacao_atual = pontuacao
    else:
        pontuacao_atual = Pontuacao.Calcula_Pontuacao(dados, tipoPontuacao, idJogadorAtual)[0]

    if type(pontuacao_atual) != int:
        return 1
    if type(idJogadorAtual) != int:
        return 2
    if type(tipoPontuacao) != str:
        return 3
    for k in listaJogadores:
        for j in k:
            if idJogadorAtual == j:
                achadoJogador = 1
    if achadoJogador != 1:
        return 4

    for i in pontuacaoAux:
        if tipoPontuacao == i: #Procura se a pontuacao esta no dicionario auxiliar
            linha = pontuacaoAux[i]
            pontuacao = tabuleiro[linha]
            achado = 1 
            if idJogadorAtual == id_primeiro_jogador:
                if pontuacao[0] == None:
                    pontuacao[0] = pontuacao_atual
                    totalLinha = tabuleiro[13]
                    if totalLinha[0] == None:
                        totalLinha[0] = pontuacao_atual
                    else:
                        totalLinha[0] = totalLinha[0] + pontuacao_atual
                else:
                    return 6
            else:
                if pontuacao[1] == None:
                    pontuacao[1] = pontuacao_atual
                    totalLinha = tabuleiro[13]
                    if totalLinha[1] == None:
                        totalLinha[1] = pontuacao_atual
                    else:
                        totalLinha[1] = totalLinha[1] + pontuacao_atual
                else:
                    return 6

    if achado != 1:
        return 5
    
    return 0

#Funcao que sera chamada no modulo Jogo retornando o ID do Jogador
#Vencedor comparando as devidas pontuacoes comparando as duas ultimas
#linhas entre as colunas da matriz
#Parametro: None
#retorna {0: ID} - Caso a verificacao tenha ocorrido com sucesso.
#retorna {1: None} - Caso o tabuleiro esteja vazio.
#retorna {2: None} - Caso nao haja tabuleiro criado.
#retorna {3: None} - Caso o tabuleiro nao esteja completo
def Verifica_Vencedor():
    cont = 0

    if len(tabuleiro) == 0:
        return {2: None}
    for k in tabuleiro:
        if k == [None,None]:
            cont = cont +1
    if cont == 14:
        
        return {1: None}
    elif cont != 0 :
        return {3: None}

    linhaTotal = tabuleiro[13]
    if linhaTotal[0]>linhaTotal[1]:
        return {0: 1}
    elif linhaTotal[0]<linhaTotal[1]:
        return {0: 2}

#Funcao que retorna o tabuleiro criado
#Parametro: None
#retorna {0: tabuleiro} caso de sucesso
#retorna {1: []} caso nao haja tabuleiro
def Pega_Tabuleiro():
    qtdTab = len(tabuleiro)
    if qtdTab == 0:
        return {1: []}
    return {0: tabuleiro}


