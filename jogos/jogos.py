import forca
import adivinhacao

print("*********************************")
print("*******Escolha o seu jogo!*******")
print("*********************************")

while 1:
    print("(1) Forca | (2) Adivinhação")

    jogo = int(input("Digite o número referente ao jogo: "))

    if jogo == 1:
        print("Abrindo o jogo da FORCA...", end="\n\n")
        forca.iniciar()
    elif jogo == 2:
        print("Abrindo o jogo da ADVINHAÇÃO...", end="\n\n")
        adivinhacao.iniciar()
    else:
        print("Insira um valor válido")
    print()