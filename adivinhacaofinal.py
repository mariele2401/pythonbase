import random 
#Cores no terminal PY
VERMELHO = "\033[31m"
VERDE = "\033[32m"
AMARELO = "\033[33m"
AZUL = "\033[34m"
RESET = "\033[0m"

def escolher_nivel():
    print("\nEscolha o nível: ")
    print("1 Fácil (10 tentativas)")
    print("2 Médio (5 tentativas)")
    print("3 Difícil (3 tentativas)")

    while True:
        nivel_str = input("Digite apenas números (1,2,3): ")
        if not nivel_str.isdigit():
            print(VERMELHO+"Digite apenas números"+RESET)
            continue 
        nivel = int(nivel_str)
        if nivel == 1:
            return 10 
        elif nivel == 2:
            return 5
        elif nivel == 3:
            return 3
        else:
            print(AMARELO+"Escolha apenas 1, 2 ou 3"+RESET)


def jogar():

    print(AZUL+'*********************************'+RESET)
    print(AZUL+'*******Jogo de Adivinhação*******'+RESET)  
    print(AZUL+'*********************************'+RESET)

    total_tentativas = escolher_nivel()
    numero_secreto = random.randrange(1,31)
    pontos = 100
    historico = []

    for tentativa in range(1, total_tentativas + 1):
        print ("Tentativa {rodada} de {total_tetativas}".format(rodada, total_tentativas))
        chute_src = input("Digite um número entra 1 e 100:  ")

    