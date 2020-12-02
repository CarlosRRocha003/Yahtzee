#Versao 1.2.3
#Ultima modificacao: Carlos Ribeiro

from collections import Counter
import Dados, Jogador

__all__ = ["Calcula_Pontuacao", "Pega_Faces"]



#Modulo no qual computamos a pontuacao de cada jogador a partir dos
#dados gerados e fazemos o calculo baseado na sua pontuacao

#Calcula a pontuacao baseada no nome da pontuacao escolhida pelo jogador
#Parametro: dados, nomePontuacao, idJogadorAtual
#retorna {0: pont} Caso tenha sucesso ao calcular a pontuacao
#retorna {1: None} Caso nomePontuacao nao seja string
#retorna {2: None} Caso o nomePontuacao nao esteja presente
#na lista de pontuacoes possiveis
#retorna {3:None} Caso o dado nao seja uma lista de tamanho 5
#retorna {4:None} Caso o idjogador nao seja int

def Calcula_Pontuacao(dados, nomePontuacao, idJogadorAtual):
    if ((type(dados) != type([])) or (len(dados) != 5)):
        return {3:None}
    if type(idJogadorAtual) != type(0):
        return {4: None}
    jog1, jog2 = Jogador.Pega_Jogadores()[0]
    id_jog1 = list(jog1.keys())[0]
    id_jog2 = list(jog2.keys())[0]
    if(idJogadorAtual != id_jog1 and idJogadorAtual != id_jog2):
        return {5: None}
    pont = 0 #pontuacao a ser calculada
    faces = Pega_Faces(dados)
    
    if nomePontuacao == "Ones":
        for i in faces:
            if i == 1:
                pont = pont + 1 #A cada dado com valor 1, soma-se 1.
    elif nomePontuacao == "Twos":
        for i in faces:
            if i == 2:
                pont = pont + 2 #A cada dado com valor 2, soma-se 2.
    elif nomePontuacao == "Threes":
        for i in faces:
            if i == 3:
                pont = pont + 3 #A cada dado com valor 3, soma-se 3.
    elif nomePontuacao == "Fours":
        for i in faces:
            if i == 4:
                pont = pont + 4 #A cada dado com valor 4, soma-se 4.
    elif nomePontuacao == "Fives":
        for i in faces:
            if i == 5:
                pont = pont + 5 #A cada dado com valor 5, soma-se 5.
    elif nomePontuacao == "Sixes":
        for i in faces:
            if i == 6:
                pont = pont + 6 #A cada dado com valor 6, soma-se 6.
    elif nomePontuacao == "Three of a Kind":
        if max(iter(Counter(faces).values()))>=3:
            pont = sum(faces) #pontuacao eh a soma de todos os dados (n somente os iguais)
    elif nomePontuacao == "Four of a Kind":
        if max(iter(Counter(faces).values()))>=4:
            pont = sum(faces) #pontuacao eh igual a todos os dados nao somente os iguais
    elif nomePontuacao == "Full House":
        if(list(iter(Counter(faces).values()))[0]==3 and list(iter(Counter(faces).values()))[1]==2) or (list(iter(Counter(faces).values()))[0]==2 and list(iter(Counter(faces).values()))[1]==3):
            pont = 25 #Caso 3 dados tenham valores iguais e os outros 2 tenham outros valores iguais, pontua 25.
    elif nomePontuacao == "Small Straight":
        s = min(faces)
        if(s+1 in faces and s+2 in faces and s+3 in faces):
            pont = 30 #Caso 4 dados formem um sequencia numerica, pontua 30.
    elif nomePontuacao == "Large Straight":
        s=min(faces)
        if s+1 in faces and s+2 in faces and s+3 in faces and s+4 in faces:
            pont = 40 #Caso 5 dados formem uma sequencia numerica, pontua 40.
    elif nomePontuacao == "Chance":
        for i in faces:
            pont = pont + i #Pode se usar a qualquer momento, soma-se todos os dados.
    elif nomePontuacao == "Yahtzee":
        if(max(iter(Counter(faces).values()))==5):
            pont = 50 #Caso 6 dados tenham valores iguais, pontua 50.
    
    return {0: pont}

#Modulo que pega as faces do dado
#Parametro: o objeto dados
#Retorna a lista de faces caso sucesso
#retorna {1:[]} caso o dado nao seja um objeto dado
def Pega_Faces(dados):
    retorno_mostra_dados=Dados.Mostra_Dados()
    if(type(dados)==list):
        if dados[0]!= retorno_mostra_dados[0][0]:
            return {1:[]}
    else:
        if type(dados)!= type(retorno_mostra_dados):
            return {1:[]}
    listFaces = []
    k=0
    for i in dados:
        k=k+1
        listFaces.append(i[k]['face'])

    return listFaces

