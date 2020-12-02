from Jogador import Cria_Novo_Jogador
from Dados import Cria_Dados, Muda_Status, Muda_Face
from Rodada import Cria_Rodada, Atualiza_Tentativas
from Jogo import Cria_Novo_Jogo
from Tabuleiro import Cria_Tab, InserirPontuacao
from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement, Comment
from xml.dom import minidom


__all__ = ["salva_xml_status_partida", "retoma_jogo_arquivo_xml"]

listaAuxiliarPontuacoes = ['Ones', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes', 'Three_of_a_Kind',
'Four_of_a_Kind', 'Full_House', "Small_Straight", "Large_Straight", "Chance", "Yahtzee", "Total_Score"]

nomeArquivo = 'jogadores.xml'

def formata_saida(elem):
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

def coluna(matriz, coluna):
    return [linha[coluna] for linha in matriz]

def salva_xml_status_partida(jog1, jog2, matriz_pont, jogadorAtual, dados_jogo, rodada_atual, tentivas_rodada):
    pontuacao_jogador_1 = coluna(matriz_pont, 0)
    pontuacao_jogador_2 = coluna(matriz_pont, 1)
    jogadores = Element('jogadores')
    comment = Comment('Dados dos jogadores e suas pontuacoes')
    jogadores.append(comment)
    jogador_atual = SubElement(jogadores, 'jogador_atual_id')
    jogador_atual.text = str(jogadorAtual)
    rodada = SubElement(jogadores, 'rodada')
    rodada_numero = SubElement(rodada, 'rodada_numero')
    rodada_numero.text = str(rodada_atual)
    tentativas = SubElement(rodada, 'tentativas')
    tentativas.text = str(tentivas_rodada)
    if(len(dados_jogo)):
        dados = SubElement(jogadores, 'dados')
        for i in range(0, len(dados_jogo)):
            dado = SubElement(dados, 'dado')
            face = SubElement(dado, 'face')
            face.text = str(dados_jogo[i][i+1]["face"])
            congelado = SubElement(dado, 'congelado')
            congelado.text = str(dados_jogo[i][i+1]["congelado"])
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

def retoma_jogo_arquivo_xml():
    Cria_Tab()
    try:
        with open(nomeArquivo, 'rt') as f:
            tree = ElementTree.parse(f)
            root = tree.getroot()
    except:
        return 2
    #primeira iteracao pra criar os dois jogadores
    for jogador in root.findall('jogador'):
        Cria_Novo_Jogador(jogador.find('nome').text, int(jogador.find('id').text))

    #cria novo jogo com o jogador_atual
    Cria_Novo_Jogo(int(root.findall('jogador_atual_id')[0].text))

    if(len(root.findall('dados/dado')) > 0):
        for i in range(0, len(root.findall('dados/dado'))):
            dado = root.findall('dados/dado')[i]
            Cria_Dados()
            Muda_Face(i+1, int(dado.find('face').text))
            if(dado.find('congelado').text == 'True'):
                Muda_Status(i+1)
    else:
        for _ in range(5):
            Cria_Dados()

    rodada = root.findall('rodada')[0]
    rodada_num = int(rodada.find('rodada_numero').text)
    tentativas = int(rodada.find('tentativas').text)
    Cria_Rodada(rodada_num)
    Atualiza_Tentativas(tentativas)


    #depois iterar para inserir as pontuacoes
    for jogador in root.findall('jogador'):
        for item in listaAuxiliarPontuacoes:
            for tipo_pontuacao in jogador.iter(item):
                if(not tipo_pontuacao.text == 'None'):
                    InserirPontuacao(None, int(jogador.find('id').text), item.replace("_", " "), int(tipo_pontuacao.text))

