from Jogador import Cria_Novo_Jogador, Destroi_Jogadores, Pega_Jogadores
from bd_config import cria_ambiente, reset_database
from Dados import Cria_Dados, Muda_Status, Mostra_Dados, Destroi_Dados, Jogar_Dados, Muda_Face
from Rodada import Cria_Rodada, Verifica_Tentativa, Atualiza_Tentativas, Deleta_Rodadas, Pega_Rodada
from Jogo import Cria_Novo_Jogo, Atualiza_JogadorAtual, Destruir_Jogo, Pega_Jogo
from Pontuacao import Calcula_Pontuacao, Tipo_Pontuacao,Pega_Faces
from Tabuleiro import Cria_Tab, Destruir_Tab, InserirPontuacao, Verifica_Vencedor, Pega_Tabuleiro
from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement, Comment
from xml.dom import minidom

listaAuxiliarPontuacoes = ['Ones', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes', 'Three_Of_A_Kind',
'Four_Of_A_Kind', 'Full_House', "Small_Straight", "Large_Straight", "Chance", "Yahtzee", "Total_Score"]

ARQUIVO_XML_NOME = 'jogadores.xml'

reset_database() 
cria_ambiente()

ARQUIVO_XML_NOME = 'jogadores.xml'

def formata_saida(elem):
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

def coluna(matriz, coluna):
    return [linha[coluna] for linha in matriz]

def salva_xml_status_partida(nomeArquivo, jog1, jog2, pontuacao_jogador_1, pontuacao_jogador_2, jogadorAtual):
    jogadores = Element('jogadores')
    comment = Comment('Dados dos jogadores e suas pontuacoes')
    jogadores.append(comment)
    jogador_atual = SubElement(jogadores, 'jogador_atual_id')
    jogador_atual.text = str(jogadorAtual)
    jogador = SubElement(jogadores, 'jogador')
    id_ = SubElement(jogador, 'id')
    id_.text = str(list(jog1.keys())[0])
    nome = SubElement(jogador, 'nome')
    nome.text = list(jog1.values())[0]
    pontuacao = SubElement(jogador, 'pontuacao')
    for i in range(0, len(listaAuxiliarPontuacoes)):
        tag = SubElement(pontuacao, listaAuxiliarPontuacoes[i])
        tag.text = str(pontuacao_jogador_1[i])
    jogador = SubElement(jogadores, 'jogador')
    id_ = SubElement(jogador, 'id')
    id_.text = str(list(jog2.keys())[0])
    nome = SubElement(jogador, 'nome')
    nome.text = list(jog2.values())[0]
    pontuacao = SubElement(jogador, 'pontuacao')
    for j in range(0, len(listaAuxiliarPontuacoes)):
        tag = SubElement(pontuacao, listaAuxiliarPontuacoes[j])
        tag.text = str(pontuacao_jogador_2[j])
    nome_arquivo = nomeArquivo
    with open(nome_arquivo, 'w') as file_object:
        file_object.write(formata_saida(jogadores))

def retoma_jogo_arquivo_xml(ARQUIVO_XML_NOME):
    Cria_Tab()
    with open(ARQUIVO_XML_NOME, 'rt') as f:
        tree = ElementTree.parse(f)
        root = tree.getroot()
    #primeira iteracao pra criar os dois jogadores
    for jogador in root.findall('jogador'):
        Cria_Novo_Jogador(jogador.find('nome').text, int(jogador.find('id').text))

    #cria novo jogo com o jogador_atual
    Cria_Novo_Jogo(int(root.findall('jogador_atual_id')[0].text))

    #depois iterar para inserir as pontuacoes
    for jogador in root.findall('jogador'):
        for item in listaAuxiliarPontuacoes:
            for tipo_pontuacao in jogador.iter(item):
                if(not tipo_pontuacao.text == 'None'):
                    InserirPontuacao(None, int(jogador.find('id').text), item, int(tipo_pontuacao.text))

#Criar Jogadores
Cria_Novo_Jogador('Aiko', None)
Cria_Novo_Jogador('Ana', None)

jog1, jog2 = Pega_Jogadores()[0]
id_jog1 = list(jog1.keys())[0]
id_jog2 = list(jog2.keys())[0]
print('jog1 ', jog1)
print('jog2 ', jog2)

#Cria_Rodada
Cria_Rodada()

Verifica_Tentativa()

#Criar Dados
Cria_Dados()

#Criar tabuleiro
Cria_Tab()

#Cria jogo
Cria_Novo_Jogo(list(jog1.keys())[0])

#modifiquei a funcao joga_dados pra que sempre o primeiro dado dê 1, para poder pontuar em ones
Jogar_Dados()
#atualiza as tentativas (jogou o dado 1 vez, ainda tem 2 restando)
Atualiza_Tentativas(2)
dados = Mostra_Dados()[0]

InserirPontuacao(dados, id_jog1, 'Ones', None)
#destruo o dados (jog1 ja pontuou)
Destroi_Dados()

#atualizo o jogo para que o jogador_atual seja o jog2
Atualiza_JogadorAtual(list(jog2.keys())[0])
#Criar Dados dnv
Cria_Dados()
#crio uma nova rodada (hora do segundo jogador jogar)
Cria_Rodada()
#Rodo os dados novamente
Jogar_Dados()
#atualiza as tentativas (jogou o dado 1 vez, ainda tem 2 restando)
Atualiza_Tentativas(2)
dados = Mostra_Dados()[0]
InserirPontuacao(dados, id_jog2, 'Twos', None)
#pego o id do jogador atual
jogadorAtual = list(Pega_Jogo().values())[0]["jogador_atual"]

#pego as pontuacoes dos jogadores p/ salvar no arquivo
matriz = Pega_Tabuleiro()[0]
pontuacao_jogador_1 = coluna(matriz, 0)
pontuacao_jogador_2 = coluna(matriz, 1)
print('pontuacao_jogador_1 ', pontuacao_jogador_1)
print('pontuacao_jogador_2 ', pontuacao_jogador_2)

salva_xml_status_partida(ARQUIVO_XML_NOME, jog1, jog2, pontuacao_jogador_1, pontuacao_jogador_2, jogadorAtual)

#Como a informacao que estamos interessados sao a cartela e o jogo e o jogadores, apago os três para poder criar a partir do arquivo
Destruir_Jogo()
Destroi_Jogadores()
Destruir_Tab()

#retoma o jogo
retoma_jogo_arquivo_xml(ARQUIVO_XML_NOME)

#printa tudo que foi retomado para ter certeza que esta coerente
matriz = Pega_Tabuleiro()[0]
pontuacao_jogador_1 = coluna(matriz, 0)
pontuacao_jogador_2 = coluna(matriz, 1)
print('pontuacao_jogador_1 ', pontuacao_jogador_1)
print('pontuacao_jogador_2 ', pontuacao_jogador_2)
