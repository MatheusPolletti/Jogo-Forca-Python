from tkinter import *
from unidecode import unidecode
from random import choice

# Código Lógico
'''
from os import system, name
from time import sleep

def limparConsole():
    return system("cls" if name in ("nt", "dos") else "clear")


def qualTipo() -> str:
    limparConsole()

    print("Modos de jogo: Frutas | Países | Animais | Aleatórios")

    while True:
        try:
            tipo = input("Escolha qual tipo você deseja usar para jogar: ").lower().strip()
            tipo = unidecode(tipo) 
            sleep(1)
        except:
            print('\033[31mErro ao escolher o tipo de jogo.\033[0m')
            sleep(1)
        finally:
            if tipo == 'frutas' or tipo == 'fruta':
                return 1
            elif tipo == 'paises' or tipo == 'pais':
                return 2
            elif tipo == 'animais' or tipo == 'animal':
                return 3
            elif tipo == 'aleatorios' or tipo == 'aleatorio':
                return 4


def palavraAdivinhar(_tipo: int) -> str:
    while True:
        try:
            opcao = _tipo

            if opcao == 1:
                with open('frutas.txt', 'r', encoding='utf-8') as arquivo: 
                    linhas = arquivo.readlines()
            elif opcao == 2:
                with open('paises.txt', 'r', encoding='utf-8') as arquivo: 
                    linhas = arquivo.readlines()
            elif opcao == 3:
                with open('animais.txt', 'r', encoding='utf-8') as arquivo:
                    linhas = arquivo.readlines()
            elif opcao == 4:
                with open('aleatorios.txt', 'r', encoding='utf-8') as arquivo:
                    linhas = arquivo.readlines()

            palavra_aleatoria = choice(linhas).strip()
            return palavra_aleatoria
        except:
            print('\033[31mErro ao abrir o arquivo.\033[0m')
            sleep(1)


def letraJogar() -> str:
    print('Digite a letra para adivinhar a palavra: ')

    while True:
        try:
            letra = unidecode(input()).strip().lower()

            if len(letra) > 1 or not letra.isalpha():
                print('\033[31mDigite algo válido.\033[0m')
                sleep(1)
            else:
                sleep(1)
                limparConsole()

                return letra
        except:
            print('\033[31mErro ao escolher a letra.\033[0m')
            sleep(1)


def Jogar():
    sleep(1)
    limparConsole()

    letras_jogadas = list()
    palavra_jogador = ''

    try:
        palavra_para_adivinhar = palavraAdivinhar()

        for item in palavra_para_adivinhar.split():
            palavra_jogador += f'{'_' * len(item)} '
        palavra_jogador = palavra_jogador.strip()

        chances = 5
        
        while chances != 0:
            sleep(1)
            limparConsole()

            print(f'Palavras jogadas: {", ".join(letras_jogadas)}')
            print(palavra_jogador)

            letra = letraJogar()

            if letra in letras_jogadas:
                print('Você já jogou essa letra.')
                sleep(1)
                limparConsole()
                continue

            letras_jogadas.append(letra)
            
            if letra in unidecode(palavra_para_adivinhar.lower()):
                for posicao, item in enumerate(unidecode(palavra_para_adivinhar.lower())):
                    if item == letra:
                        palavra_jogador = palavra_jogador[:posicao] + letra + palavra_jogador[posicao + 1:]
            else:
                print('\033[31mEssa letra não existe na palavra.\033[0m')
                chances -= 1

            if palavra_jogador == unidecode(palavra_para_adivinhar.lower()):
                print('\033[32mParabéns! Você acertou a palavra!\033[0m')
                print(palavra_para_adivinhar)
                break
        
            if chances == 0:
                print(f'\033[31mVocê perdeu, a palavra era {palavra_para_adivinhar}.\033[0m')
                break
    except:
        print('\033[31mErro ao rodar o jogo.\033[0m')
'''

def palavraAdivinhar(tipo) -> str:
    while True:
        try:
            opcao = tipo

            if opcao == 1:
                with open('frutas.txt', 'r', encoding='utf-8') as arquivo: 
                    linhas = arquivo.readlines()
            elif opcao == 2:
                with open('paises.txt', 'r', encoding='utf-8') as arquivo: 
                    linhas = arquivo.readlines()
            elif opcao == 3:
                with open('animais.txt', 'r', encoding='utf-8') as arquivo:
                    linhas = arquivo.readlines()
            elif opcao == 4:
                with open('aleatorios.txt', 'r', encoding='utf-8') as arquivo:
                    linhas = arquivo.readlines()

            palavra_aleatoria = choice(linhas).strip()
            return palavra_aleatoria
        except:
            print('\033[31mErro ao abrir o arquivo.\033[0m')

jogoForca = Tk()

jogoForca.title('Jogo da Forca.')

LARGURA_JANELA = 820
ALTURA_JANELA = 520

jogoForca.geometry(f'{LARGURA_JANELA}x{ALTURA_JANELA}')
jogoForca.config(bg='#000000')
jogoForca.resizable(False, False)

icone = PhotoImage(file='forca.png')
jogoForca.iconphoto(True, icone)

criador = Label(jogoForca, text='Criado por Matheus Polletti', font=('Helvetica', 12), bg='black', foreground='white')
criador.pack(anchor=CENTER)

canvas = Canvas(jogoForca, width=LARGURA_JANELA, height=ALTURA_JANELA, bg='white')
canvas.pack()

def telaInicial():
    def comandoFruta():
        fruta = palavraAdivinhar(1)

        canvas.delete('all')
        botao_fruta.destroy()
        botao_paises.destroy()
        botao_animais.destroy()
        botao_aleatorios.destroy()

        jogo(fruta)


    def comandoPaises():
        paises = palavraAdivinhar(2)

        canvas.delete('all')
        botao_fruta.destroy()
        botao_paises.destroy()
        botao_animais.destroy()
        botao_aleatorios.destroy()

        jogo(paises)


    def comandoAnimais():
        animais = palavraAdivinhar(3)

        canvas.delete('all')
        botao_fruta.destroy()
        botao_paises.destroy()
        botao_animais.destroy()
        botao_aleatorios.destroy()

        jogo(animais)


    def comandoAleatorios():
        aleatorios = palavraAdivinhar(4)

        canvas.delete('all')
        botao_fruta.destroy()
        botao_paises.destroy()
        botao_animais.destroy()
        botao_aleatorios.destroy()
        
        jogo(aleatorios)


    canvas.create_text((430, 40), text='Escolha o seu modo de jogo: ', font='Helvetica 24')

    botao_fruta = Button(canvas, text='Frutas', width=14, height=4, bg='#FFA500', fg='#000000', font=('Helvetica 12'), command=comandoFruta)
    botao_fruta.place(x=40, y=100)

    botao_paises = Button(canvas, text='Países', width=14, height=4, bg='#FFA500', fg='#000000', font=('Helvetica 12'), command=comandoPaises)
    botao_paises.place(x=240, y=100)

    botao_animais = Button(canvas, text='Animais', width=14, height=4, bg='#FFA500', fg='#000000', font=('Helvetica 12'), command=comandoAnimais)
    botao_animais.place(x=440, y=100)

    botao_aleatorios = Button(canvas, text='Aleatórios', width=14, height=4, bg='#FFA500', fg='#000000', font=('Helvetica 12'), command=comandoAleatorios)
    botao_aleatorios.place(x=640, y=100)

    botao_deletar = Button(canvas, text='Sair', width=4, height=1, bg='red', fg='#000000', font=('Helvetica 8'), command=jogoForca.destroy)
    botao_deletar.place(anchor=NW)


def jogo(_fruta):
    palavras_digitas = []
    chances = 6

    def desenharBoneco(_quantia):
        if (_quantia == 5):
            #cabeça
            canvas.create_oval(313, 160, 393, 220, width=5)
        if (_quantia == 4):
            #corpo
            canvas.create_line(353, 220 , 353, 300, width=5)
        if (_quantia == 3):
            #perna direita
            canvas.create_line(353, 296 , 380, 350, width=5)
        if (_quantia == 2):
            #perna esquerda
            canvas.create_line(353, 296 , 326, 350, width=5)
        if (_quantia == 1):
            #braço direito
            canvas.create_line(353, 220 , 380, 250, width=5)
        if (_quantia == 0):
            #braco esquerdo
            canvas.create_line(353, 220 , 326, 250, width=5)


    def chave_digitada(evento):
        nonlocal chances
        nonlocal palavra_jogador
        nonlocal palavra_adivinhar
        nonlocal letras_digitadas
        nonlocal caixa_texto
        nonlocal texto_digitar

        letra = unidecode(evento.char).lower()
        canvas.itemconfig(digitou_letra, text='')
    
        if (letra.isalpha()) and (letra not in palavras_digitas):
            palavras_digitas.append(letra)
            canvas.itemconfig(letras_digitadas, text=f'{", ".join(palavras_digitas)}')

            if (letra in unidecode(palavra_adivinhar.lower())):
                for posicao, item in enumerate(unidecode(palavra_adivinhar.lower())):
                    if item == letra:
                        palavra_jogador[posicao] = letra

                canvas.itemconfig(texto_palavra, text=palavra_jogador)
                
                if (''.join(palavra_jogador) == unidecode(palavra_adivinhar.lower()).replace(' ', '_')):
                    canvas.destroy()
                    jogoForca.config(bg='#FFFFFF')

                    vencedor = Label(jogoForca, text='Parabéns! Você venceu.', font=('Helvetica', 40), foreground='green', bg='#FFFFFF')
                    vencedor.pack(anchor=CENTER)
            else:
                chances -= 1
    
        elif (evento.char in palavras_digitas):
            canvas.itemconfig(digitou_letra, text='Você já digitou essa letra!')

        if (chances <= 0):
            canvas.delete(texto_digitar)
            canvas.delete(texto_palavra)
            canvas.delete(letras_digitadas)
            caixa_texto.destroy()

            desenharBoneco(chances)

            canvas.create_text((530, 380), text='Você perdeu!', font='Helvetica 24', fill='red')
            canvas.create_text((530, 410), text=f'A palavra correta era {palavra_adivinhar}', font='Helvetica 24')

        caixa_texto.delete(0, END)
        desenharBoneco(chances)


    letras_digitadas = canvas.create_text((500, 450), text='', font='Helvetica 24')
  
    canvas.create_line(20, ALTURA_JANELA - 80, 180, ALTURA_JANELA - 80, width=10)
    canvas.create_line(95, ALTURA_JANELA - 80, 95, 80, width=10)
    canvas.create_line(90, 80, 360, 80, width=10)
    canvas.create_line(355, 85, 355, 160, width=6, fill='brown')

    print(_fruta)
    palavra_adivinhar = _fruta
    palavra_jogador = ['_'] * len(palavra_adivinhar)

    texto_palavra = canvas.create_text((540, 370), text=f"{' '.join(palavra_jogador)}", font='Helvetica 24')
    digitou_letra = canvas.create_text((600, 250), font='Helvetica 20', fill='red')

    texto_digitar = canvas.create_text((620, 298), text='Digite a letra:', font='Helvetica 20')
    caixa_texto = Entry(canvas, font=('Arial', 24), bg='lightgray')

    canvas.create_window(720, 301, height=30, width=36, window=caixa_texto)
    caixa_texto.bind("<KeyPress>", chave_digitada)


telaInicial()

jogoForca.mainloop()
