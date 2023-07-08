import random

def bem_vindo():
    print('-' * 40)
    print('Seja Bem-Vindo ao jogo da forca!!!')
    print('-' * 40)

def carregar_palavra_secreta():
    with open('./Resultado Final/palavras.txt', 'r') as arquivo:
        palavras = []

        for linha in arquivo :
            linha = linha.strip()
            palavras.append(linha)
    
    arquivo.close()

    numero = random.randrange(0, len(palavras) + 1)

    palavra_secreta = palavras[numero].upper()

    return palavra_secreta

def inicializa_letras_acertas(palavra_secreta):
    tamanho = len(palavra_secreta)
    print(f'A palavra tem {tamanho} letras.')
    letras_acertadas = ['_'] * tamanho
    print(letras_acertadas)
    return letras_acertadas

def chute_do_jogador():
    chute = input('Qual é a letra? \n')
    chute = chute.strip().upper()
    return chute

def adicionar_chute_acertado(chute, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:            
        if chute == letra:
            letras_acertadas[index] = letra 
        index += 1

def mostrar_palavra_secreta(palavra_secreta):
    print(f'A palavra secreta é {palavra_secreta}\n')

def mensagem_de_vencedor():
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

def mensagem_de_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print(f"A palavra era {palavra_secreta}")
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

def desenha_forca(erro):
    print("  _______     ")
    print(" |/      |    ")

    if(erro == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erro == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erro == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erro == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erro == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erro == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erro == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def jogar():

    bem_vindo()
    palavra_secreta = carregar_palavra_secreta()

    letras_acertadas = inicializa_letras_acertas(palavra_secreta)

    enforcou = False
    acertou = False
    erro = 0
    while not enforcou and not acertou:

        chute = chute_do_jogador()
        
        if chute in palavra_secreta:
            adicionar_chute_acertado(chute, palavra_secreta, 
            letras_acertadas)
        else:
            erro += 1
            desenha_forca(erro)

        enforcou = erro == 7
        acertou = '_' not in letras_acertadas

        print(letras_acertadas)

    if acertou:
        mensagem_de_vencedor()
    else:    
        mensagem_de_perdedor(palavra_secreta)

if __name__ == '__main__':
    jogar()