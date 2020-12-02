#Autor: Carlos Ribeiro
#Versao: 2.0.0

from bd_config import cria_ambiente, reset_database

reset_database() 
cria_ambiente()

from tkinter import Tk, messagebox, Button, LabelFrame, Entry, Label, W, E, N, S, DISABLED, SUNKEN
from PIL import ImageTk,Image
from Jogador import Cria_Novo_Jogador, Destroi_Jogadores, Pega_Jogadores
import sys

from Dados import Cria_Dados, Muda_Status, Mostra_Dados, Destroi_Dados, Jogar_Dados, Muda_Face
from Rodada import Cria_Rodada, Verifica_Tentativa, Atualiza_Tentativas, Deleta_Rodadas, Pega_Rodada
from Jogo import Cria_Novo_Jogo, Atualiza_JogadorAtual, Destruir_Jogo, Pega_Jogo
from Pontuacao import Calcula_Pontuacao, Pega_Faces
from Tabuleiro import Cria_Tab, Destruir_Tab, InserirPontuacao, Verifica_Vencedor, Pega_Tabuleiro
from Salva_Jogo import salva_xml_status_partida, retoma_jogo_arquivo_xml

__all__ = ["Tela_Inicial", "Desenha_Tab"]



root = Tk()
root.title("Principal")
root.config(bg="green")

imgDado1 = ImageTk.PhotoImage(Image.open("Assets/dados/Dice-1.png"))
imgDado2 = ImageTk.PhotoImage(Image.open("Assets/dados/Dice-2E.png"))
imgDado3 = ImageTk.PhotoImage(Image.open("Assets/dados/Dice-3E.png"))
imgDado4 = ImageTk.PhotoImage(Image.open("Assets/dados/Dice-4.png"))
imgDado5 = ImageTk.PhotoImage(Image.open("Assets/dados/Dice-5.png"))
imgDado6 = ImageTk.PhotoImage(Image.open("Assets/dados/Dice-6E.png"))


button_Dado1 = Button(root,activebackground='red',command=lambda: Dado_clicado(button_Dado1,1))
button_Dado2 = Button(root,activebackground='red',command=lambda: Dado_clicado(button_Dado2,2))
button_Dado3 = Button(root,activebackground='red',command=lambda: Dado_clicado(button_Dado3,3))
button_Dado4 = Button(root,activebackground='red',command=lambda: Dado_clicado(button_Dado4,4))
button_Dado5 = Button(root,activebackground='red',command=lambda: Dado_clicado(button_Dado5,5))

button_Ones = Button(root, text="Ones",bg="green",disabledforeground="black",padx = 20,pady =10, command=InserirPontuacao, state=DISABLED)
button_Twos = Button(root, text="Twos",bg="green",disabledforeground="black",padx = 20,pady =10, command=InserirPontuacao, state=DISABLED)
button_Threes = Button(root, text="Threes",bg="green",disabledforeground="black",padx = 20,pady =10, command=InserirPontuacao, state=DISABLED)
button_Fours = Button(root, text="Fours",bg="green",disabledforeground="black",padx = 20,pady =10, command=InserirPontuacao, state=DISABLED)
button_Fives = Button(root, text="Fives",bg="green",disabledforeground="black",padx = 20,pady =10, command=InserirPontuacao, state=DISABLED)
button_Sixes = Button(root, text="Sixes",bg="green",disabledforeground="black",padx = 20,pady =10, command=InserirPontuacao, state=DISABLED)
button_ThreeOfAKind = Button(root, text="Three of a Kind",bg="green",disabledforeground="black",padx = 20,pady =10, command=InserirPontuacao, state=DISABLED)
button_FourOfAKind = Button(root, text="Four of a Kind",bg="green",disabledforeground="black",padx = 20,pady =10, command=InserirPontuacao, state=DISABLED)
button_FullHouse = Button(root, text="Full House",bg="green",disabledforeground="black",padx = 20,pady =10, command=InserirPontuacao, state=DISABLED)
button_SmallStraight = Button(root, text="Small Straight",bg="green",disabledforeground="black",padx = 20,pady =10, command=InserirPontuacao, state=DISABLED)
button_LargeStraight = Button(root, text="Large Straight",bg="green",disabledforeground="black",padx = 20,pady =10, command=InserirPontuacao, state=DISABLED)
button_Chance = Button(root, text="Chance",bg="green",disabledforeground="black",padx = 20,pady =10, command=InserirPontuacao, state=DISABLED)
button_Yahtzee = Button(root, text="Yahtzee",bg="green",disabledforeground="black",padx = 20,pady =10, command=InserirPontuacao, state=DISABLED)


def Comeca_Jogo(jogador1,jogador2,frame_inicial):

    ret_jog1 = Cria_Novo_Jogador(jogador1.get(),1)
    ret_jog2 = Cria_Novo_Jogador(jogador2.get(),2)
    if ret_jog1 == 1:
        if ret_jog2 == 0:
            Destroi_Jogadores()
        messagebox.showwarning("Erro", "Nao foi possivel criar jogador 1, ja existem 2 jogadores")
        return
    elif ret_jog1 == 2:
        if ret_jog2 == 0:
            Destroi_Jogadores()
        messagebox.showwarning("Erro", "Nome do jogador nao passado corretamente")
        return
    if ret_jog2 == 1:
        if ret_jog1 == 0:
            Destroi_Jogadores()
        messagebox.showwarning("Erro", "Nao foi possivel criar jogador 2, ja existem 2 jogadores")
        return
    elif ret_jog2 == 2:
        if ret_jog1 == 0:
            Destroi_Jogadores()
        messagebox.showwarning("Erro", "Nome do jogador nao passado corretamente")
        return
    Cria_Rodada()
    Cria_Novo_Jogo(1)
    Cria_Tab()
    Cria_Dados()

    frame_inicial.pack_forget()
    frame_inicial.destroy()

    Desenha_Tab()

    return

def Carrega_jogo(frame_inicial):
    retorno = retoma_jogo_arquivo_xml()
    if(retorno == 2):
        messagebox.showwarning("Erro", "Nao ha registro salvo de jogo, favor criar novo jogo")
        return
    frame_inicial.pack_forget()
    frame_inicial.destroy()
    Desenha_Tab(True)
    return

def Tela_Inicial():

    frame_inicial = LabelFrame(root, padx=5,pady=5, bg="green")
    frame_inicial.pack(padx=5,pady=5)

    label_Yahtzee = Label(frame_inicial, text="YAHTZEE!", bg="green",fg="white")
    label_Yahtzee.configure(font="Arial 20 bold")
    label_Yahtzee.grid(row=0,column=0,columnspan=2)

    label_Jogador1 = Label(frame_inicial, text="Nome do jogador 1: ", bg="green", fg="white")
    label_Jogador1.configure(font="Arial 9 bold")
    label_Jogador1.grid(row=1,column=0)
    jogador1 = Entry(frame_inicial,width=25,borderwidth=3)
    jogador1.grid(row=1,column=1)

    label_Jogador2 = Label(frame_inicial, text="Nome do jogador 2: ", bg="green", fg="white")
    label_Jogador2.configure(font="Arial 9 bold")
    label_Jogador2.grid(row=2,column=0)
    jogador2 = Entry(frame_inicial,width=25,borderwidth=3)
    jogador2.grid(row=2,column=1)

    comecar_button=Button(frame_inicial, text="Comecar o jogo", command=lambda: Comeca_Jogo(jogador1,jogador2,frame_inicial))
    comecar_button.grid(row=3,column=0,columnspan=2,pady=5)

    button_load_game = Button(frame_inicial, text='Carregar ultimo jogo', command=lambda: Carrega_jogo(frame_inicial))
    button_load_game.grid(row=4, column=0, columnspan=2, pady=5)

    
    return

def Insere(nomePontuacao):
    global button_Ones
    global button_Twos
    global button_Threes
    global button_Fours
    global button_Fives
    global button_Sixes
    global button_ThreeOfAKind
    global button_FourOfAKind
    global button_FullHouse
    global button_SmallStraight
    global button_LargeStraight
    global button_Chance
    global button_Yahtzee
    dados = Mostra_Dados()[0]
    idJogador = list(Pega_Jogo().values())[0]["jogador_atual"]
    RodadaNumero=list(Pega_Rodada()[0].keys())[0]
    InserirPontuacao(dados, idJogador, nomePontuacao, None)

    #Para nao aparecer novamente disponivel apos insercao de pontuacao
    button_Ones.grid_forget()
    #button_Ones = Button(root, text="Ones",bg="green",disabledforeground="black",padx = 20,pady =10, command=InserirPontuacao, state=DISABLED)
    button_Ones['state','disabledforeground']=DISABLED,"black"
    button_Ones.grid(row=2,column=0,sticky=W+E)

    button_Twos.grid_forget()
    button_Twos = Button(root, text="Twos",bg="green",disabledforeground="black",padx = 20,pady =10, command=InserirPontuacao, state=DISABLED)
    button_Twos.grid(row=3,column=0,sticky=W+E)

    button_Threes.grid_forget()
    button_Threes = Button(root, text="Threes",bg="green",disabledforeground="black",padx = 20,pady =10, command=InserirPontuacao, state=DISABLED)
    button_Threes.grid(row=4,column=0,sticky=W+E)

    button_Fours.grid_forget()
    button_Fours = Button(root, text="Fours",bg="green",disabledforeground="black",padx = 20,pady =10, command=InserirPontuacao, state=DISABLED)
    button_Fours.grid(row=5,column=0,sticky=W+E)

    button_Fives.grid_forget()
    button_Fives = Button(root, text="Fives",bg="green",disabledforeground="black",padx = 20,pady =10, command=InserirPontuacao, state=DISABLED)
    button_Fives.grid(row=6,column=0,sticky=W+E)

    button_Sixes.grid_forget()
    button_Sixes = Button(root, text="Sixes",bg="green",disabledforeground="black",padx = 20,pady =10, command=InserirPontuacao, state=DISABLED)
    button_Sixes.grid(row=7,column=0,sticky=W+E)

    button_ThreeOfAKind.grid_forget()
    button_ThreeOfAKind = Button(root, text="Three of a Kind",bg="green",disabledforeground="black",padx = 20,pady =10, command=InserirPontuacao, state=DISABLED)
    button_ThreeOfAKind.grid(row=8,column=0,sticky=W+E)
    
    button_FourOfAKind.grid_forget()
    button_FourOfAKind = Button(root, text="Four of a Kind",bg="green",disabledforeground="black",padx = 20,pady =10, command=InserirPontuacao, state=DISABLED)
    button_FourOfAKind.grid(row=9,column=0,sticky=W+E)

    button_FullHouse.grid_forget()
    button_FullHouse = Button(root, text="Full House",bg="green",disabledforeground="black",padx = 20,pady =10, command=InserirPontuacao, state=DISABLED)
    button_FullHouse.grid(row=10,column=0,sticky=W+E)

    button_SmallStraight.grid_forget()
    button_SmallStraight = Button(root, text="Small Straight",bg="green",disabledforeground="black",padx = 20,pady =10, command=InserirPontuacao, state=DISABLED)
    button_SmallStraight.grid(row=11,column=0,sticky=W+E)

    button_LargeStraight.grid_forget()
    button_LargeStraight = Button(root, text="Large Straight",bg="green",disabledforeground="black",padx = 20,pady =10, command=InserirPontuacao, state=DISABLED)
    button_LargeStraight.grid(row=12,column=0,sticky=W+E)

    button_Chance.grid_forget()
    button_Chance = Button(root, text="Chance",bg="green",disabledforeground="black",padx = 20,pady =10, command=InserirPontuacao, state=DISABLED)
    button_Chance.grid(row=13,column=0,sticky=W+E)

    button_Yahtzee.grid_forget()
    button_Yahtzee = Button(root, text="Yahtzee",bg="green",disabledforeground="black",padx = 20,pady =10, command=InserirPontuacao, state=DISABLED)
    button_Yahtzee.grid(row=14,column=0,sticky=W+E)

    if idJogador == 1:
        idJogador = 2
        Atualiza_JogadorAtual(2)
    elif idJogador == 2:
        idJogador = 1
        Atualiza_JogadorAtual(1)

    RodadaNumero = RodadaNumero + 1
    Cria_Rodada()
    
    Desenha_Tab(idJogador)
    
    for i in range(0, len(dados)): #loop para mudar o status dos dados congelados apos insercao de pontuacao
        if dados[i][i+1]["congelado"] == True:
            Muda_Status(i+1)
        
    
    button_Dado1.grid_forget()
    button_Dado2.grid_forget()
    button_Dado3.grid_forget()
    button_Dado4.grid_forget()
    button_Dado5.grid_forget()
    Destroi_Dados()
    Cria_Dados()

    return

def Pontuacoes_Disponiveis():
    global button_Ones
    global button_Twos
    global button_Threes
    global button_Fours
    global button_Fives
    global button_Sixes
    global button_ThreeOfAKind
    global button_FourOfAKind
    global button_FullHouse
    global button_SmallStraight
    global button_LargeStraight
    global button_Chance
    global button_Yahtzee

    dados = Mostra_Dados()[0]
    idJogadorAtual = list(Pega_Jogo().values())[0]["jogador_atual"]
    tabuleiro = Pega_Tabuleiro()[0]
    
    #Para nao aparecer novamente caso nao escolha nenhuma pontuacao
    button_Ones.grid_forget()
    button_Ones = Button(root, text="Ones",bg="green",disabledforeground="black",padx = 20,pady =10, command=InserirPontuacao, state=DISABLED)
    button_Ones.grid(row=2,column=0,sticky=W+E)

    button_Twos.grid_forget()
    button_Twos = Button(root, text="Twos",bg="green",disabledforeground="black",padx = 20,pady =10, command=InserirPontuacao, state=DISABLED)
    button_Twos.grid(row=3,column=0,sticky=W+E)

    button_Threes.grid_forget()
    button_Threes = Button(root, text="Threes",bg="green",disabledforeground="black",padx = 20,pady =10, command=InserirPontuacao, state=DISABLED)
    button_Threes.grid(row=4,column=0,sticky=W+E)

    button_Fours.grid_forget()
    button_Fours = Button(root, text="Fours",bg="green",disabledforeground="black",padx = 20,pady =10, command=InserirPontuacao, state=DISABLED)
    button_Fours.grid(row=5,column=0,sticky=W+E)

    button_Fives.grid_forget()
    button_Fives = Button(root, text="Fives",bg="green",disabledforeground="black",padx = 20,pady =10, command=InserirPontuacao, state=DISABLED)
    button_Fives.grid(row=6,column=0,sticky=W+E)

    button_Sixes.grid_forget()
    button_Sixes = Button(root, text="Sixes",bg="green",disabledforeground="black",padx = 20,pady =10, command=InserirPontuacao, state=DISABLED)
    button_Sixes.grid(row=7,column=0,sticky=W+E)

    button_ThreeOfAKind.grid_forget()
    button_ThreeOfAKind = Button(root, text="Three of a Kind",bg="green",disabledforeground="black",padx = 20,pady =10, command=InserirPontuacao, state=DISABLED)
    button_ThreeOfAKind.grid(row=8,column=0,sticky=W+E)
    
    button_FourOfAKind.grid_forget()
    button_FourOfAKind = Button(root, text="Four of a Kind",bg="green",disabledforeground="black",padx = 20,pady =10, command=InserirPontuacao, state=DISABLED)
    button_FourOfAKind.grid(row=9,column=0,sticky=W+E)

    button_FullHouse.grid_forget()
    button_FullHouse = Button(root, text="Full House",bg="green",disabledforeground="black",padx = 20,pady =10, command=InserirPontuacao, state=DISABLED)
    button_FullHouse.grid(row=10,column=0,sticky=W+E)

    button_SmallStraight.grid_forget()
    button_SmallStraight = Button(root, text="Small Straight",bg="green",disabledforeground="black",padx = 20,pady =10, command=InserirPontuacao, state=DISABLED)
    button_SmallStraight.grid(row=11,column=0,sticky=W+E)

    button_LargeStraight.grid_forget()
    button_LargeStraight = Button(root, text="Large Straight",bg="green",disabledforeground="black",padx = 20,pady =10, command=InserirPontuacao, state=DISABLED)
    button_LargeStraight.grid(row=12,column=0,sticky=W+E)

    button_Chance.grid_forget()
    button_Chance = Button(root, text="Chance",bg="green",disabledforeground="black",padx = 20,pady =10, command=InserirPontuacao, state=DISABLED)
    button_Chance.grid(row=13,column=0,sticky=W+E)

    button_Yahtzee.grid_forget()
    button_Yahtzee = Button(root, text="Yahtzee",bg="green",disabledforeground="black",padx = 20,pady =10, command=InserirPontuacao, state=DISABLED)
    button_Yahtzee.grid(row=14,column=0,sticky=W+E)
    
    if tabuleiro[0][idJogadorAtual-1] == None:
        button_Ones = Button(root, text="Ones",bg="green",fg="white",padx = 20,pady =10, command=lambda: Insere("Ones"))

        pontuacao = Calcula_Pontuacao(dados,"Ones", idJogadorAtual)[0]
        if idJogadorAtual == 1:
            label_Ones1 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white",fg="red")
            label_Ones1.grid(row=2,column=1,sticky=N+S+E+W)
        elif idJogadorAtual == 2:
            label_Ones2 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white",fg="red")
            label_Ones2.grid(row=2,column=2,sticky=N+S+E+W)
        
        button_Ones.grid(row=2,column=0,sticky=W+E)
    if tabuleiro[1][idJogadorAtual-1] == None:
        button_Twos = Button(root, text="Twos",bg="green",fg="white",padx = 20,pady =10, command=lambda: Insere("Twos"))

        pontuacao = Calcula_Pontuacao(dados,"Twos", idJogadorAtual)[0]
        if idJogadorAtual == 1:
            label_Twos1 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white",fg="red")
            label_Twos1.grid(row=3,column=1,sticky=N+S+E+W)
        elif idJogadorAtual == 2:
            label_Twos2 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white",fg="red")
            label_Twos2.grid(row=3,column=2,sticky=N+S+E+W)
        
        button_Twos.grid(row=3,column=0,sticky=W+E)
    if tabuleiro[2][idJogadorAtual-1] == None:
        button_Threes = Button(root, text="Threes",bg="green",fg="white",padx = 20,pady =10, command=lambda: Insere("Threes"))

        pontuacao = Calcula_Pontuacao(dados,"Threes", idJogadorAtual)[0]
        if idJogadorAtual == 1:
            label_Threes1 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white",fg="red")
            label_Threes1.grid(row=4,column=1,sticky=N+S+E+W)
        elif idJogadorAtual == 2:
            label_Threes2 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white",fg="red")
            label_Threes2.grid(row=4,column=2,sticky=N+S+E+W)
        
        button_Threes.grid(row=4,column=0,sticky=W+E)
    if tabuleiro[3][idJogadorAtual-1] == None:
        button_Fours = Button(root, text="Fours",bg="green",fg="white",padx = 20,pady =10, command=lambda: Insere("Fours"))

        pontuacao = Calcula_Pontuacao(dados,"Fours", idJogadorAtual)[0]
        if idJogadorAtual == 1:
            label_Fours1 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white",fg="red")
            label_Fours1.grid(row=5,column=1,sticky=N+S+E+W)
        elif idJogadorAtual == 2:
            label_Fours2 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white",fg="red")
            label_Fours2.grid(row=5,column=2,sticky=N+S+E+W)
        
        button_Fours.grid(row=5,column=0,sticky=W+E)
    if tabuleiro[4][idJogadorAtual-1] == None:
        button_Fives = Button(root, text="Fives",bg="green",fg="white",padx = 20,pady =10, command=lambda: Insere("Fives"))

        pontuacao = Calcula_Pontuacao(dados,"Fives", idJogadorAtual)[0]
        if idJogadorAtual == 1:
            label_Fives1 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white",fg="red")
            label_Fives1.grid(row=6,column=1,sticky=N+S+E+W)
        elif idJogadorAtual == 2:
            label_Fives2 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white",fg="red")
            label_Fives2.grid(row=6,column=2,sticky=N+S+E+W)
        
        button_Fives.grid(row=6,column=0,sticky=W+E)
    if tabuleiro[5][idJogadorAtual-1] == None:
        button_Sixes = Button(root, text="Sixes",bg="green",fg="white",padx = 20,pady =10, command=lambda: Insere("Sixes"))

        pontuacao = Calcula_Pontuacao(dados,"Sixes", idJogadorAtual)[0]
        if idJogadorAtual == 1:
            label_Sixes1 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white",fg="red")
            label_Sixes1.grid(row=7,column=1,sticky=N+S+E+W)
        elif idJogadorAtual == 2:
            label_Sixes2 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white",fg="red")
            label_Sixes2.grid(row=7,column=2,sticky=N+S+E+W)
        
        button_Sixes.grid(row=7,column=0,sticky=W+E)
    if tabuleiro[6][idJogadorAtual-1] == None:
        button_ThreeOfAKind = Button(root, text="Three of a Kind",bg="green",fg="white",padx = 20,pady =10, command=lambda: Insere("Three of a Kind"))

        pontuacao = Calcula_Pontuacao(dados,"Three of a Kind", idJogadorAtual)[0]
        if idJogadorAtual == 1:
            label_ThreeOfAKind1 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white",fg="red")
            label_ThreeOfAKind1.grid(row=8,column=1,sticky=N+S+E+W)
        elif idJogadorAtual == 2:
            label_ThreeOfAKind2 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white",fg="red")
            label_ThreeOfAKind2.grid(row=8,column=2,sticky=N+S+E+W)
        
        button_ThreeOfAKind.grid(row=8,column=0,sticky=W+E)
    if tabuleiro[7][idJogadorAtual-1] == None:
        button_FourOfAKind = Button(root, text="Four of a Kind",bg="green",fg="white",padx = 20,pady =10, command=lambda: Insere("Four of a Kind"))

        pontuacao = Calcula_Pontuacao(dados,"Four of a Kind", idJogadorAtual)[0]
        if idJogadorAtual == 1:
            label_FourOfAKind1 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white",fg="red")
            label_FourOfAKind1.grid(row=9,column=1,sticky=N+S+E+W)
        elif idJogadorAtual == 2:
            label_FourOfAKind2 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white",fg="red")
            label_FourOfAKind2.grid(row=9,column=2,sticky=N+S+E+W)
        
        button_FourOfAKind.grid(row=9,column=0,sticky=W+E)
    if tabuleiro[8][idJogadorAtual-1] == None:
        button_FullHouse = Button(root, text="Full House",bg="green",fg="white",padx = 20,pady =10, command=lambda: Insere("Full House"))

        pontuacao = Calcula_Pontuacao(dados,"Full House", idJogadorAtual)[0]
        if idJogadorAtual == 1:
            label_FullHouse1 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white",fg="red")
            label_FullHouse1.grid(row=10,column=1,sticky=N+S+E+W)
        elif idJogadorAtual == 2:
            label_FullHouse2 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white",fg="red")
            label_FullHouse2.grid(row=10,column=2,sticky=N+S+E+W)
        
        button_FullHouse.grid(row=10,column=0,sticky=W+E)
    if tabuleiro[9][idJogadorAtual-1] == None:
        button_SmallStraight = Button(root, text="Small Straight",bg="green",fg="white",padx = 20,pady =10, command=lambda: Insere("Small Straight"))

        pontuacao = Calcula_Pontuacao(dados,"Small Straight", idJogadorAtual)[0]
        if idJogadorAtual == 1:
            label_SmallStraight1 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white",fg="red")
            label_SmallStraight1.grid(row=11,column=1,sticky=N+S+E+W)
        elif idJogadorAtual == 2:
            label_SmallStraight2 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white",fg="red")
            label_SmallStraight2.grid(row=11,column=2,sticky=N+S+E+W)
        
        button_SmallStraight.grid(row=11,column=0,sticky=W+E)   
    if tabuleiro[10][idJogadorAtual-1] == None:
        button_LargeStraight = Button(root, text="Large Straight",bg="green",fg="white",padx = 20,pady =10, command=lambda: Insere("Large Straight"))

        pontuacao = Calcula_Pontuacao(dados,"Large Straight", idJogadorAtual)[0]
        if idJogadorAtual == 1:
            label_LargeStraight1 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white",fg="red")
            label_LargeStraight1.grid(row=12,column=1,sticky=N+S+E+W)
        elif idJogadorAtual == 2:
            label_LargeStraight2 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white",fg="red")
            label_LargeStraight2.grid(row=12,column=2,sticky=N+S+E+W)
        
        button_LargeStraight.grid(row=12,column=0,sticky=W+E)
    if tabuleiro[11][idJogadorAtual-1] == None:
        button_Chance = Button(root, text="Chance",bg="green",fg="white",padx = 20,pady =10, command=lambda: Insere("Chance"))

        pontuacao = Calcula_Pontuacao(dados,"Chance", idJogadorAtual)[0]
        if idJogadorAtual == 1:
            label_Chance1 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white",fg="red")
            label_Chance1.grid(row=13,column=1,sticky=N+S+E+W)
        elif idJogadorAtual == 2:
            label_Chance2 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white",fg="red")
            label_Chance2.grid(row=13,column=2,sticky=N+S+E+W)
        
        button_Chance.grid(row=13,column=0,sticky=W+E)
    if tabuleiro[12][idJogadorAtual-1] == None:
        button_Yahtzee = Button(root, text="Yahtzee",bg="green",fg="white",padx = 20,pady =10, command=lambda: Insere("Yahtzee"))

        pontuacao = Calcula_Pontuacao(dados,"Yahtzee", idJogadorAtual)[0]
        if idJogadorAtual == 1:
            label_Yahtzee1 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white",fg="red")
            label_Yahtzee1.grid(row=14,column=1,sticky=N+S+E+W)
        elif idJogadorAtual == 2:
            label_Yahtzee2 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white",fg="red")
            label_Yahtzee2.grid(row=14,column=2,sticky=N+S+E+W)
        
        button_Yahtzee.grid(row=14,column=0,sticky=W+E)
    return

def Mostra_Dados_Jogo_Carregado():
    global button_Ones, button_Twos, button_Threes, button_Fours, button_Fives, button_Sixes, button_ThreeOfAKind, button_FullHouse, button_SmallStraight,\
    button_LargeStraight, button_Chance, button_Yahtzee, button_Dado1, button_Dado2, button_Dado3, button_Dado4, button_Dado5
    dados = Mostra_Dados()[0]
    RodadaNumero=list(Pega_Rodada()[0].keys())[0]
    tent = Pega_Rodada()[0][RodadaNumero]['tentativas']
    Pontuacoes_Disponiveis()
    listaFaces = Pega_Faces(dados)
    
    #Possiveis faces do Primeiro Dado
    if dados[0][1]['congelado'] == False:
        button_Dado1['bg'] = 'green'
    elif dados[0][1]['congelado'] == True:
        button_Dado1['bg'] = 'gray'
    #Possiveis faces do Primeiro Dado
    if listaFaces[0] == 1:
        button_Dado1['image'] = imgDado1
    elif listaFaces[0] == 2:
        button_Dado1['image'] = imgDado2
    elif listaFaces[0] == 3:
        button_Dado1['image'] = imgDado3
    elif listaFaces[0] == 4:
        button_Dado1['image'] = imgDado4
    elif listaFaces[0] == 5:
        button_Dado1['image'] = imgDado5
    elif listaFaces[0] == 6:
        button_Dado1['image'] = imgDado6

    #Possiveis faces do Segundo Dado   
    if dados[1][2]['congelado'] == False:
        button_Dado2['bg'] = 'green'
    elif dados[1][2]['congelado'] == True:
        button_Dado2['bg'] = 'gray'
    #Possiveis faces do Segundo Dado   
    if listaFaces[1] == 1:
        button_Dado2['image'] = imgDado1
    elif listaFaces[1] == 2:
        button_Dado2['image'] = imgDado2
    elif listaFaces[1] == 3:
        button_Dado2['image'] = imgDado3
    elif listaFaces[1] == 4:
        button_Dado2['image'] = imgDado4
    elif listaFaces[1] == 5:
        button_Dado2['image'] = imgDado5
    elif listaFaces[1] == 6:
        button_Dado2['image'] = imgDado6

    #Possiveis faces do Terceiro Dado
    if dados[2][3]['congelado'] == False:
        button_Dado3['bg'] = 'green'
    elif dados[2][3]['congelado'] == True:
        button_Dado3['bg'] = 'gray'
    #Possiveis faces do Terceiro Dado
    if listaFaces[2] == 1:
        button_Dado3['image'] = imgDado1
    elif listaFaces[2] == 2:
        button_Dado3['image'] = imgDado2
    elif listaFaces[2] == 3:
        button_Dado3['image'] = imgDado3
    elif listaFaces[2] == 4:
        button_Dado3['image'] = imgDado4
    elif listaFaces[2] == 5:
        button_Dado3['image'] = imgDado5
    elif listaFaces[2] == 6:
        button_Dado3['image'] = imgDado6

    #Possiveis faces do Quarto Dado
    if dados[3][4]['congelado'] == False:
        button_Dado4['bg'] = 'green'
    elif dados[3][4]['congelado'] == True:
        button_Dado4['bg'] = 'gray'
    #Possiveis faces do Quarto Dado
    if listaFaces[3] == 1:
        button_Dado4['image'] = imgDado1
    elif listaFaces[3] == 2:
        button_Dado4['image'] = imgDado2
    elif listaFaces[3] == 3:
        button_Dado4['image'] = imgDado3
    elif listaFaces[3] == 4:
        button_Dado4['image'] = imgDado4
    elif listaFaces[3] == 5:
        button_Dado4['image'] = imgDado5
    elif listaFaces[3] == 6:
        button_Dado4['image'] = imgDado6

    #Possiveis faces do Quinto Dado
    if dados[4][5]['congelado'] == False:
        button_Dado5['bg'] = 'green'
    elif dados[4][5]['congelado'] == True:
        button_Dado5['bg'] = 'gray'
    #Possiveis faces do Quinto Dado
    if listaFaces[4] == 1:
        button_Dado5['image'] = imgDado1
    elif listaFaces[4] == 2:
        button_Dado5['image'] = imgDado2
    elif listaFaces[4] == 3:
        button_Dado5['image'] = imgDado3
    elif listaFaces[4] == 4:
        button_Dado5['image'] = imgDado4
    elif listaFaces[4] == 5:
        button_Dado5['image'] = imgDado5
    elif listaFaces[4] == 6:
        button_Dado5['image'] = imgDado6
        
    button_Dado1.grid(row=16,column=0,columnspan=2,sticky=W)
    button_Dado2.grid(row=16,column=0,columnspan=2,sticky=N)
    button_Dado3.grid(row=16,column=1,columnspan=2,sticky=W)
    button_Dado4.grid(row=16,column=1,columnspan=2,sticky=N)
    button_Dado5.grid(row=16,column=2,sticky=E)
    label_tentativas = Label(root,text = "Faltam " + str(tent) + " tentativas", bg = "green",fg="white", bd=1, relief=SUNKEN, anchor=W)
    label_tentativas.grid(row = 21, column=0, columnspan = 3,sticky=W+E)

def Dado_clicado(butao,numDado):
    
    dados = Mostra_Dados()[0]
    if dados[numDado-1][numDado]['congelado'] == False: 
        butao['bg'] = 'gray'
    else:
        butao['bg'] = 'green'


    Muda_Status(numDado)

    return

def Desenha_Dados():
    global button_Ones, button_Twos, button_Threes, button_Fours, button_Fives, button_Sixes, button_ThreeOfAKind, button_FullHouse, button_SmallStraight,\
    button_LargeStraight, button_Chance, button_Yahtzee, button_Dado1, button_Dado2, button_Dado3, button_Dado4, button_Dado5
    Jogar_Dados()
    dados = Mostra_Dados()[0]
    Pontuacoes_Disponiveis()
    listaFaces = Pega_Faces(dados)
    RodadaNumero=list(Pega_Rodada()[0].keys())[0]

    tent = Pega_Rodada()[0][RodadaNumero]['tentativas']
    Atualiza_Tentativas(tent-1)
    tent = Pega_Rodada()[0][RodadaNumero]['tentativas']

    #Possiveis faces do Primeiro Dado
    if dados[0][1]['congelado'] == False:
        button_Dado1['bg'] = 'green'
    elif dados[0][1]['congelado'] == True:
        button_Dado1['bg'] = 'gray'
    #Possiveis faces do Primeiro Dado
    if listaFaces[0] == 1:
        button_Dado1['image'] = imgDado1
    elif listaFaces[0] == 2:
        button_Dado1['image'] = imgDado2
    elif listaFaces[0] == 3:
        button_Dado1['image'] = imgDado3
    elif listaFaces[0] == 4:
        button_Dado1['image'] = imgDado4
    elif listaFaces[0] == 5:
        button_Dado1['image'] = imgDado5
    elif listaFaces[0] == 6:
        button_Dado1['image'] = imgDado6

    #Possiveis faces do Segundo Dado   
    if dados[1][2]['congelado'] == False:
        button_Dado2['bg'] = 'green'
    elif dados[1][2]['congelado'] == True:
        button_Dado2['bg'] = 'gray'
    #Possiveis faces do Segundo Dado   
    if listaFaces[1] == 1:
        button_Dado2['image'] = imgDado1
    elif listaFaces[1] == 2:
        button_Dado2['image'] = imgDado2
    elif listaFaces[1] == 3:
        button_Dado2['image'] = imgDado3
    elif listaFaces[1] == 4:
        button_Dado2['image'] = imgDado4
    elif listaFaces[1] == 5:
        button_Dado2['image'] = imgDado5
    elif listaFaces[1] == 6:
        button_Dado2['image'] = imgDado6

    #Possiveis faces do Terceiro Dado
    if dados[2][3]['congelado'] == False:
        button_Dado3['bg'] = 'green'
    elif dados[2][3]['congelado'] == True:
        button_Dado3['bg'] = 'gray'
    #Possiveis faces do Terceiro Dado
    if listaFaces[2] == 1:
        button_Dado3['image'] = imgDado1
    elif listaFaces[2] == 2:
        button_Dado3['image'] = imgDado2
    elif listaFaces[2] == 3:
        button_Dado3['image'] = imgDado3
    elif listaFaces[2] == 4:
        button_Dado3['image'] = imgDado4
    elif listaFaces[2] == 5:
        button_Dado3['image'] = imgDado5
    elif listaFaces[2] == 6:
        button_Dado3['image'] = imgDado6

    #Possiveis faces do Quarto Dado
    if dados[3][4]['congelado'] == False:
        button_Dado4['bg'] = 'green'
    elif dados[3][4]['congelado'] == True:
        button_Dado4['bg'] = 'gray'
    #Possiveis faces do Quarto Dado
    if listaFaces[3] == 1:
        button_Dado4['image'] = imgDado1
    elif listaFaces[3] == 2:
        button_Dado4['image'] = imgDado2
    elif listaFaces[3] == 3:
        button_Dado4['image'] = imgDado3
    elif listaFaces[3] == 4:
        button_Dado4['image'] = imgDado4
    elif listaFaces[3] == 5:
        button_Dado4['image'] = imgDado5
    elif listaFaces[3] == 6:
        button_Dado4['image'] = imgDado6

    #Possiveis faces do Quinto Dado
    if dados[4][5]['congelado'] == False:
        button_Dado5['bg'] = 'green'
    elif dados[4][5]['congelado'] == True:
        button_Dado5['bg'] = 'gray'
    #Possiveis faces do Quinto Dado
    if listaFaces[4] == 1:
        button_Dado5['image'] = imgDado1
    elif listaFaces[4] == 2:
        button_Dado5['image'] = imgDado2
    elif listaFaces[4] == 3:
        button_Dado5['image'] = imgDado3
    elif listaFaces[4] == 4:
        button_Dado5['image'] = imgDado4
    elif listaFaces[4] == 5:
        button_Dado5['image'] = imgDado5
    elif listaFaces[4] == 6:
        button_Dado5['image'] = imgDado6
        
    button_Dado1.grid(row=16,column=0,columnspan=2,sticky=W)
    button_Dado2.grid(row=16,column=0,columnspan=2,sticky=N)
    button_Dado3.grid(row=16,column=1,columnspan=2,sticky=W)
    button_Dado4.grid(row=16,column=1,columnspan=2,sticky=N)
    button_Dado5.grid(row=16,column=2,sticky=E)

    verTentativa = Verifica_Tentativa()

    if verTentativa == 0:
        button_JogarDados = Button(root, text="Jogar Dados",padx = 60,pady =10, command=lambda: Desenha_Dados())
    elif verTentativa == 1:
        button_JogarDados = Button(root, text="Jogar Dados",padx = 60,pady =10, command=lambda: Desenha_Dados(),state=DISABLED)

    button_JogarDados.grid(row=19,column=0,columnspan=3,sticky=W+E)

    label_tentativas = Label(root,text = "Faltam " + str(tent) + " tentativas", bg = "green",fg="white", bd=1, relief=SUNKEN, anchor=W)
    label_tentativas.grid(row = 21, column=0, columnspan = 3,sticky=W+E)
    return

def on_closing():
    tabuleiro = Pega_Tabuleiro()[0]
    jogador1, jogador2 = Pega_Jogadores()[0]
    dados = list(Mostra_Dados().values())[0]
    jogadorAtual = list(Pega_Jogo().values())[0]["jogador_atual"]
    rodada = Pega_Rodada()[0]
    rodada_atual = list(rodada.keys())[0]
    tentativas = list(rodada.values())[0]["tentativas"]
    if messagebox.askokcancel("Fechar", "Seu jogo sera salvo"):
        salva_xml_status_partida(jogador1, jogador2, tabuleiro, jogadorAtual, dados, rodada_atual, tentativas)
        try:
            root.destroy()
        except:
            print('aplicao destruida')

def Desenha_Tab(*args):
    idJogadorAtual = list(Pega_Jogo().values())[0]["jogador_atual"]
    jogadores = Pega_Jogadores()[0]
    tabuleiro = Pega_Tabuleiro()[0]

    RodadaNumero=list(Pega_Rodada()[0].keys())[0]
    tent = Pega_Rodada()[0][RodadaNumero]['tentativas']

    jogador1 = jogadores[0][1]
    jogador2 = jogadores[1][2]

    labelJogador1 = Label(root,text=jogador1, bg = "green",fg="white")
    labelJogador2 = Label(root,text=jogador2, bg = "green",fg="white")

    pontuacao = tabuleiro[0][0]
    label_Ones1 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white")
    pontuacao = tabuleiro[0][1]
    label_Ones2 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white")
    pontuacao = tabuleiro[1][0]
    label_Twos1 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white")
    pontuacao = tabuleiro[1][1]
    label_Twos2 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white")
    pontuacao = tabuleiro[2][0]
    label_Threes1 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white")
    pontuacao = tabuleiro[2][1]
    label_Threes2 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white")
    pontuacao = tabuleiro[3][0]
    label_Fours1 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white")
    pontuacao = tabuleiro[3][1]
    label_Fours2 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white")
    pontuacao = tabuleiro[4][0]
    label_Fives1 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white")
    pontuacao = tabuleiro[4][1]
    label_Fives2 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white")
    pontuacao = tabuleiro[5][0]
    label_Sixes1 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white")
    pontuacao = tabuleiro[5][1]
    label_Sixes2 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white")
    pontuacao = tabuleiro[6][0]
    label_ThreeOfAKind1 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white")
    pontuacao = tabuleiro[6][1]
    label_ThreeOfAKind2 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white")
    pontuacao = tabuleiro[7][0]
    label_FourOfAKind1 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white")
    pontuacao = tabuleiro[7][1]
    label_FourOfAKind2 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white")
    pontuacao = tabuleiro[8][0]
    label_FullHouse1 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white")
    pontuacao = tabuleiro[8][1]
    label_FullHouse2 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white")
    pontuacao = tabuleiro[9][0]
    label_SmallStraight1 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white")
    pontuacao = tabuleiro[9][1]
    label_SmallStraight2 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white")
    pontuacao = tabuleiro[10][0]
    label_LargeStraight1 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white")
    pontuacao = tabuleiro[10][1]
    label_LargeStraight2 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white")
    pontuacao = tabuleiro[11][0]
    label_Chance1 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white")
    pontuacao = tabuleiro[11][1]
    label_Chance2 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white")
    pontuacao = tabuleiro[12][0]
    label_Yahtzee1 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white")
    pontuacao = tabuleiro[12][1]
    label_Yahtzee2 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white")

    label_Total = Label(root, text="Total",bg="green",fg="black",relief="raised",padx = 20,pady =10)
    
    pontuacao = tabuleiro[13][0]
    label_Total1 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white")
    pontuacao = tabuleiro[13][1]
    label_Total2 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white")
    
    labelJogador1.grid(row=1,column=1)
    labelJogador2.grid(row=1,column=2)

    labelJogador1.configure(font="Arial 12 bold")
    labelJogador2.configure(font="Arial 12 bold")

    if idJogadorAtual == 1:
        labelJogador1.configure(font="Arial 12 bold underline")
    elif idJogadorAtual == 2:
        labelJogador2.configure(font="Arial 12 bold underline")

    button_Ones.grid(row=2,column=0,sticky=W+E)
    label_Ones1.grid(row=2,column=1,sticky=N+S+E+W)
    label_Ones2.grid(row=2,column=2,sticky=N+S+E+W)

    button_Twos.grid(row=3,column=0,sticky=W+E)
    label_Twos1.grid(row=3,column=1,sticky=N+S+E+W)
    label_Twos2.grid(row=3,column=2,sticky=N+S+E+W)

    button_Threes.grid(row=4,column=0,sticky=W+E)
    label_Threes1.grid(row=4,column=1,sticky=N+S+E+W)
    label_Threes2.grid(row=4,column=2,sticky=N+S+E+W)

    button_Fours.grid(row=5,column=0,sticky=W+E)
    label_Fours1.grid(row=5,column=1,sticky=N+S+E+W)
    label_Fours2.grid(row=5,column=2,sticky=N+S+E+W)

    button_Fives.grid(row=6,column=0,sticky=W+E)
    label_Fives1.grid(row=6,column=1,sticky=N+S+E+W)
    label_Fives2.grid(row=6,column=2,sticky=N+S+E+W)

    button_Sixes.grid(row=7,column=0,sticky=W+E)
    label_Sixes1.grid(row=7,column=1,sticky=N+S+E+W)
    label_Sixes2.grid(row=7,column=2,sticky=N+S+E+W)

    button_ThreeOfAKind.grid(row=8,column=0,sticky=W+E)
    label_ThreeOfAKind1.grid(row=8,column=1,sticky=N+S+E+W)
    label_ThreeOfAKind2.grid(row=8,column=2,sticky=N+S+E+W)

    button_FourOfAKind.grid(row=9,column=0,sticky=W+E)
    label_FourOfAKind1.grid(row=9,column=1,sticky=N+S+E+W)
    label_FourOfAKind2.grid(row=9,column=2,sticky=N+S+E+W)

    button_FullHouse.grid(row=10,column=0,sticky=W+E)
    label_FullHouse1.grid(row=10,column=1,sticky=N+S+E+W)
    label_FullHouse2.grid(row=10,column=2,sticky=N+S+E+W)

    button_SmallStraight.grid(row=11,column=0,sticky=W+E)
    label_SmallStraight1.grid(row=11,column=1,sticky=N+S+E+W)
    label_SmallStraight2.grid(row=11,column=2,sticky=N+S+E+W)

    button_LargeStraight.grid(row=12,column=0,sticky=W+E)
    label_LargeStraight1.grid(row=12,column=1,sticky=N+S+E+W)
    label_LargeStraight2.grid(row=12,column=2,sticky=N+S+E+W)

    button_Chance.grid(row=13,column=0,sticky=W+E)
    label_Chance1.grid(row=13,column=1,sticky=N+S+E+W)
    label_Chance2.grid(row=13,column=2,sticky=N+S+E+W)

    button_Yahtzee.grid(row=14,column=0,sticky=W+E)
    label_Yahtzee1.grid(row=14,column=1,sticky=N+S+E+W)
    label_Yahtzee2.grid(row=14,column=2,sticky=N+S+E+W)

    label_Total.grid(row=15,column=0,sticky=W+E)
    label_Total1.grid(row=15,column=1,sticky=W+E)
    label_Total2.grid(row=15,column=2,sticky=W+E)

    verTentativa = Verifica_Tentativa()
    if verTentativa == 0:
        if(args and args[0] and Pega_Rodada()[0][RodadaNumero]['tentativas'] < 3):
            Mostra_Dados_Jogo_Carregado()
        button_JogarDados = Button(root, text="Jogar Dados",padx = 60,pady =10, command=lambda: Desenha_Dados())
    elif verTentativa == 1:
        if(args and args[0]):
            Mostra_Dados_Jogo_Carregado()   
        button_JogarDados = Button(root, text="Jogar Dados",padx = 60,pady =10, command=lambda: Desenha_Dados(),state=DISABLED)

    button_JogarDados.grid(row=19,column=0,columnspan=3,sticky=W+E)


    if RodadaNumero == 27:
        vencedor=Verifica_Vencedor()[0]
        jogVencedor=Pega_Jogadores()[0][vencedor-1][vencedor]
        messagebox.showinfo("Vencedor", "Jogador Vencedor: " + jogVencedor)
        root.destroy()
        sys.exit()
    else:
        status = Label(root,text = "Rodada " + str(RodadaNumero) + " de 26",bg = "green",fg="white", bd=1, relief=SUNKEN, anchor=E)
        status.grid(row = 20, column=0, columnspan = 3,sticky=W+E)
        if(tent == 3):
            label_tentativas = Label(root,text = "Faltam " + str(tent) + " tentativas", bg = "green",fg="white", bd=1, relief=SUNKEN, anchor=W)
            label_tentativas.grid(row = 21, column=0, columnspan = 3,sticky=W+E)
    
    return


Tela_Inicial()

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()

