from unidecode import unidecode
from os import system, name
from time import sleep
from random import choice

def limparConsole():
    return system("cls" if name in ("nt", "dos") else "clear")


def qualTipo():
    limparConsole()

    print("Modos de jogo: Frutas | Países | Animais | Aleatórios")
    
    try:
        tipo = input("Escolha qual tipo você deseja usar para jogar: ").lower().strip()
        tipo = unidecode(tipo)
    
        print(tipo)
        sleep(2)
    except:
        print('\033[31mErro ao escolher o tipo de jogo.\033[0m')
        sleep(1)

        qualTipo()
    print('aqui')
    if tipo == 'frutas':
        return 1
    elif tipo == 'paises':
        return 2
    elif tipo == 'animais':
        return 3
    elif tipo == 'aleatorios':
        return 4
    else:
        qualTipo()


def palavraAdivinhar():
    try:
        opcao = qualTipo()
        if opcao != int:
            raise ValueError()
        print(opcao)

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
        palavraAdivinhar()


def letraJogar():
    print('Digite a letra para adivinhar a palavra: ')

    try:
        letra = unidecode(input()).strip().lower()

        if len(letra) > 1 or not letra.isalpha():
            print('\033[31mDigite algo válido.\033[0m')
            sleep(1)

            letraJogar()
        else:
            sleep(1)
            limparConsole()

            return letra
    except:
        print('\033[31mErro ao escolher a letra.\033[0m')
        sleep(1)
        letraJogar()

def Jogar():
    sleep(1)
    limparConsole()
    try:
        palavra_para_adivinhar = palavraAdivinhar()
        palavra_jogador = '_' * len(palavra_para_adivinhar)
        chances = 5

        print(palavra_para_adivinhar)
        
        while chances != 0:
            print(palavra_jogador)

            letra = letraJogar()
            
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
        
        if chances == 0:
            print(f'\033[31mVocê perdeu, a palavra era {palavra_para_adivinhar}.\033[0m')
    except:
        Jogar()

Jogar()
