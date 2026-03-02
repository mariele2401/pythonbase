import random 


#Cores no terminal PY
VERMELHO = "\033[31m"
VERDE = "\033[32m"
AMARELO = "\033[33m"
AZUL = "\033[34m"
RESET = "\033[0m"


print('*********************************')
print('*******Jogo de Adivinhação*******')
print('*********************************')

print("Escolha o nível de dificuldade:")
print("1 Fácil (10 tentativas)")
print("2 Médio (9 tentativas)")
print("3 Difícil (5 tentativas)")

nivel = int(input("Digite o nível: "))

if nivel == 1:
    numero_maximo = 10
    total_tentativas = 10
elif nivel == 2:
    numero_maximo = 40
    total_tentativas = 7
elif nivel == 3:
    numero_maximo = 90
    total_tentativas = 5
else:
    print("Nível inválido,escolha outro")

numero_secreto = random.randrange(1, numero_maximo + 1)
rodada = 1

for rodada in range (1, total_tentativas +1):
    print("Tentativa {} de {}.".format(rodada, total_tentativas))
    chute_str = input("Digite seu número: ")
    chute = int(chute_str)
    print("Seu número é: ", chute_str)
    
    if(chute < 1 or chute > numero_maximo):
        print("Você deve digitar um número entre 1 e {}".format(numero_maximo))
        continue
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto
    
    if(acertou):
        print("Você acertou! ")
        break
    else:
        if(maior):
            print("O seu chute foi maior que o número secreto")
        elif(menor):
            print("O seu chute foi menor que o número secreto")
    
    rodada = rodada + 1

print("Fim de jogo!")