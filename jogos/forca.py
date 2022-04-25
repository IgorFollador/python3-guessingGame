import random


def iniciar():
    imprime_mensagem_abertura()
    palavra_secreta = sorteia_palavra("palavras.txt")
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    tentativas = 7  # Define o valor de tentativas que o usuário pode errar
    enforcou = False
    acertou = False
    erros = 0

    while not enforcou and not acertou:
        chute = le_chute()

        if chute in palavra_secreta:
            salva_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros, tentativas)
        enforcou = erros == tentativas
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)
    print("Fim do jogo")


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros, tentativas):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()
    print("Ops, você errou! Faltam {} tentativas.".format(tentativas - erros))
    print()


def salva_chute_correto(chute, letras_acertadas, palavra):
    index = 0
    for letra in palavra:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1


def le_chute():
    chute = input("Qual a letra?\n")
    chute = chute.strip().upper()
    return chute


def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]  # Add um caracter a cada letra da palavra


def sorteia_palavra(documento: str):
    palavras = []

    with open(documento) as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip().upper())

    index = random.randrange(0, len(palavras))  # Sorteia o número referente ao local da palavra no array
    return palavras[index].upper()  # Retorna a palavra sorteada e realiza a conversão da mesma para caixa alta


def imprime_mensagem_abertura():
    print("*********************************")
    print("Bem vindo ao jogo da Forca!")
    print("*********************************")


if __name__ == "__main__":
    iniciar()
