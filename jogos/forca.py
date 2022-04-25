import random

def iniciar():
    print("*********************************")
    print("Bem vindo ao jogo da Forca!")
    print("*********************************")

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip().upper()
        palavras.append(linha)
    arquivo.close()

    index = random.randrange(0, len(palavras)) #Sorteia o número referente ao local da palavra no array
    palavra_secreta = palavras[index].upper() #Seleciona a palavra sorteada e realiza a conversão da mesma para caixa alta
    letras_acertadas = ["_" for letra in palavra_secreta] #Add um caracter a cada letra da palavra

    enforcou = False
    acertou = False
    erros = 0
    tentativas = 6

    print(letras_acertadas)

    while not enforcou and not acertou:
        chute = input("Qual a letra?\n")
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print("Ops, você errou! Faltam {} tentativas.".format(tentativas - erros))
        enforcou = erros == tentativas
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        print("Você ganhou!")
    else:
        print("Você perdeu!")
    print("Fim do jogo")


if __name__ == "__main__":
    iniciar()
