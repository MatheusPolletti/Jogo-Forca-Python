from tkinter import *
from unidecode import unidecode
from os import system, name
from time import sleep
from random import choice

def limparConsole():
    return system("cls" if name in ("nt", "dos") else "clear")


def qualTipo():
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


def palavraAdivinhar():
    while True:
        try:
            opcao = 1#qualTipo()

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


def letraJogar():
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

jogoForca = Tk()

LARGURA_JANELA = 820
ALTURA_JANELA = 520

jogoForca.title('Jogo da Forca.')

jogoForca.geometry(f'{LARGURA_JANELA}x{ALTURA_JANELA}')
jogoForca.config(bg='#000000')
jogoForca.resizable(False, False)

icone = PhotoImage(file='forca.png')
jogoForca.iconphoto(True, icone)

criador = Label(jogoForca, text='Criado por Matheus Polletti', font=('Helvetica', 12), bg='black', foreground='white')
criador.pack(anchor=CENTER)

canvas = Canvas(jogoForca, width=LARGURA_JANELA, height=ALTURA_JANELA, bg='white')
canvas.pack()

opcao = 0

def comandoFruta():
    global opcao
    opcao= 1


def comandoPaises():
    global opcao
    opcao = 2


def comandoAnimais():
    global opcao
    opcao = 3


def comandoAleatorios():
    return 4


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

print(comandoAleatorios)


'''
def chave_digitada(evento):
    if (evento.char.isalpha()):
        print(evento.char)

# x1, y1, x2, y1    
canvas.create_line(20, ALTURA_JANELA - 80, 180, ALTURA_JANELA - 80, width=10)
canvas.create_line(95, ALTURA_JANELA - 80, 95, 80, width=10)
canvas.create_line(90, 80, 360, 80, width=10)
canvas.create_line(355, 85, 355, 160, width=6, fill='brown')

palavra = palavraAdivinhar()
print(palavra)

# x, y
canvas.create_text((540, 370), text='_ ' * len(palavra), font='Helvetica 24')

canvas.create_text((620, 298), text='Digite a letra:', font='Helvetica 20')
caixa_texto = Entry(canvas, font=('Arial', 24), bg='lightgray')
canvas.create_window(720, 301, height=20, width=20, window=caixa_texto)
caixa_texto.bind("<KeyPress>", chave_digitada)
'''
jogoForca.mainloop()