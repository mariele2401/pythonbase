print('*****************')
print('**** jogo de adivinhação*****')
print('*****************')

numero_secreto = 39

chute_str = input("Digite seu numero: ")

print("Seu numero é:",chute_str)

if (numero_secreto == chute_str):
    print("Você acertou!!")

else:
    print("Você errou  :(")