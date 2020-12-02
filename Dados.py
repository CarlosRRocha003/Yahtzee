#Versao 1.0.10
#Ultima modificacao: Carlos Ribeiro
import random
__all__ = ["Cria_Dados", "Muda_Status", "Mostra_Dados", "Destroi_Dados", "Jogar_Dados", "Muda_Face"]

dados = []
#Modulo que implementa a criacao dos Dados,o ato de jogar os dados,
#e mostrar a face dos dados. O modulo tem como atributo uma lista de tamanho
#cinco de objetos Dado. Cada Objeto dado eh um dicionario com ID(int) e um outro
#dicionario com seus atributos, face (valor inteiro de 1 ate 6),
#e congelado (booleano),que representa se o jogador escolheu por nao jogar
#aquele dado especifico naquela arremesso.Exemplo de objeto Dado: {01: {congelado: False, face: 6}}.

#Funcao que cria uma lista de cinco objetos dados. 
#No caso de dessa funçao, cada objeto Dado criado tera seu valor “face” igual a zero, 
#pois ainda nao foi arremessado por algum jogador, seu valor “congelado”, portanto, sera False
#Parametro: NULL
#retorna 0 caso de sucesso
#retorna 1 caso ja exista dado criado (tentativa de recriaçao)
def Cria_Dados():
    qtdDados = len(dados)
    if(qtdDados == 5):
        return 1
    for i in range(1, 6):
        dados.append({ i: {"face": 0, "congelado": False} })
    return 0


#Muda o valor da chave congelado do objeto dado.
#Parametro:ID (id do dado criado para identificacao)
#retorna 0 quando sucesso na mudanca de estado
#retorna 1 caso esse id nao tenha dado correspondente
#retorna 2 caso o tipo de parametro passado nao seja int
#retorna 3 caso a lista de objetos Dado seja vazia(ainda nao criados)
def Muda_Status(id):
    if(type(id) != type(0)):
        return 2
    if(id not in range(1,6)):
        return 1
    if(len(dados) == 0):
        return 3
    state = dados[id-1][id]["congelado"]
    dados[id-1][id]["congelado"] = not state
    return 0

# Funcao responsavel por verificar se todos os dados estao congelados
#retorna True quando todos os dados estao congelados
#retorna False quando algum dado nao esta mais congelado.
#n eh funcao de acesso, somente eh uma funcao auxiliar para funcao Joga_Dados
def verifica_dados_estao_todos_congelados():
    qtdDadosCongelados = 0
    i = 1
    while(i < 6):
        if(dados[i-1][i]["congelado"]):
            qtdDadosCongelados+=1
        i+=1
    if(qtdDadosCongelados == 5):
        return True
    return False
#Funcao responsavel por atribuir, em cada dado com chave congelado de
#valor False, um novo valor randomico
#retorna 0 quando sucesso
#retorna 1 quando nao ha dados criados
#retorna 2 quando todos os dados tem chave "congelado" com valor True
def Jogar_Dados():
    qtdDados = len(dados)
    i = 1
    if(qtdDados == 0):
        return 1 
    if(verifica_dados_estao_todos_congelados()):
        return 2
    while(i < 6):
        if dados[i-1][i]["congelado"] == False:
            dados[i-1][i]["face"] = random.randint(1,6)
        i+=1
    return 0

#Funcao que retorna um dicionario contendo um codigo como chave
#e uma lista de objetos dado
#Parametros: None
#codigo tem valor 0 quando sucesso
#valor 1 caso nao hajam dados criados
#valor 2 caso os dados ainda nao tenhma sido arremessados
def Mostra_Dados():
    qtdDados = len(dados)
    if(qtdDados == 0):
        return {1: []}
    if(dados[0][1]["face"] == 0):
        return {2: []}
    return {0: dados}

#Funcao que altera a face de um dado especifico
#Parametros: idDado, numFace
#retorna 0 caso sucesso
#retorna 1 caso idDado nao seja int
#retorna 2 caso id dado nao corresponda a nenhum dos dados
#retorna 3 caso numFace nao seja int
#retorna 4 caso o numFace seja diferente de 1, 2, 3, 4, 5 ou 6
def Muda_Face(idDado,numFace):
    
    if type(idDado) != int:
        return 1
    if idDado > 5 or idDado < 1:
        return 2
    if type(numFace) != int:
        return 3
    if numFace < 1 or numFace > 6:
        return 4

    dados[idDado-1][idDado]["face"] = numFace
    return 0

#funcao auxiliar para destruir os dados
#Parametros: None
#retorna 0 caso sucesso
#retorna 1 caso a lista ja esteja vazia
def Destroi_Dados():
    qtdDados = len(dados)
    if(qtdDados == 0):
        return 1
    dados.clear()
    return 0
